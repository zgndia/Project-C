from time import sleep
import pygetwindow as gw
import pyautogui
import psutil

# Banned words list
banned_words = [
    "ali471", "amentu", "ati242", "aykut closer", "batuflex", 
    "ben fero", "blok3", "cakal", "canbay & wolker", "cıstak", "cistak", "çakal", 
    "deha", "elmusto", "era7capone", "heijan", "jeff redd",
    "kefo", "khontkar", "lvbel c5", "mero", "motive", "murda",
    "red bull rap trivia", "sehinsah", "şehinşah", "şanışer",
    "çakal", "uzi", "- youtube music", "spotify -","- spotify",
    "barcelona", "real madrid", "bayern münih", "bayern munich",
    "manchester united", "tottenham", "young boys", "rc strasbourg",
    "chelsea", "arsenal", "porto", "milan", "juventus", "inter",
    "valencia", "liverpool", "benfica", "atletico madrid", "sevilla",
    "borussia dortmund", "lyon", "manchester city", "galatasaray",
    "fenerbahçe", "beşiktaş", "wolfsburg", "west ham united",
    "monaco", "karabağ", "başakşehir fk", "union berlin", "hoffenheim",
    "trabzonspor", "esenler erokspor", "augsburg", "eray067", "realmadrid",
    "era7", "wegh", "ege!", "spotify"
]

blacklisted_words = [
    "- youtube music"
]

# List of system applications to ignore
system_apps = ["Microsoft Text Input Application"]

def is_window_playing_sounds():
    """Simulated check for whether a window is playing sounds."""
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if 'youtube' in proc.info['name'].lower():  # Check if 'youtube' is in the process name
            return True
    return False

def get_matching_windows(open_windows):
    """Identify windows containing banned words, excluding system apps."""
    matching_windows = []
    for window in open_windows:
        window_lower = window.lower()
        filter_out = """.,/'"&%()[]-_*~`|"""
        raw_text = window_lower  # Change with window name
        filtered_text = raw_text
        for word in filter_out:
            if word in raw_text:
                filtered_text = filtered_text.replace(word, '')
        filtered_text = filtered_text.lower().split()
        fixed_window_text = " ".join(filtered_text)
        if any(f' {banned_word.lower()} ' in f' {fixed_window_text} ' for banned_word in banned_words):
            if not any(app.lower() in fixed_window_text for app in system_apps):
                matching_windows.append(window)
    return matching_windows

def close_window(window_title, Forced=False):
    """Attempt to close a window by its title."""
    windows = gw.getWindowsWithTitle(window_title)
    if windows:
        try:
            window = windows[0]
            window.activate()
            if Forced:
                pyautogui.hotkey('ctrl', 'w')
                sleep(0.1)
                pyautogui.hotkey('enter')
            else:
                pyautogui.hotkey('ctrl', 'w')
        except Exception:
            pass  # Silently pass on errors

def close_tabs():
    """Main function to check and close windows with banned words."""
    while True:
        open_windows = gw.getAllTitles()
        matching_windows = get_matching_windows(open_windows)
        
        # Check for the "youtube" window and press "i" if it's playing sounds
        for window in matching_windows:
                if not any(f' {blacklisted_word.lower()} ' in f' {window.lower()} ' for blacklisted_word in blacklisted_words):
                    close_window(window, False)
                else:
                    close_window(window, True)
        sleep(1)    

def main():
    try:
        close_tabs()
    except KeyboardInterrupt:
        pass  # Handle script termination without output

if __name__ == "__main__":
    main()
