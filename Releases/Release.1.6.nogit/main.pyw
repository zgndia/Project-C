from time import sleep
import pygetwindow as gw
import pyautogui

# Banned words list
banned_words = [
    "akdo", "ali471", "amentu", "ati", "ati242", "aykut closer", "batuflex", 
    "ben fero", "blok3", "cakal", "canbay & wolker", "cistak", "cıstak", "çakal", 
    "deha", "düğün dernek", "elmusto", "era7capone", "heijan", "jeff redd", "kaptan", 
    "kefo", "khontkar", "lvbel c5", "mero", "mini terorista", "motive", 
    "murda", "no cap", "no.1", "o adam", "organize", "pişt", 
    "red bull", "red bull rap trivia", "sagoluyorum", "sehinsah", "şehinşah", 
    "şanışer", "sönen sigaralar", "çakal", "uzi"
]

# List of system applications to ignore
system_apps = ["Microsoft Text Input Application"]

def get_matching_windows(open_windows):
    """Identify windows containing banned words, excluding system apps."""
    matching_windows = []
    for window in open_windows:
        window_lower = window.lower()
        if any(f' {banned_word.lower()} ' in f' {window_lower} ' for banned_word in banned_words):
            if not any(app.lower() in window_lower for app in system_apps):
                matching_windows.append(window)
                print(window)
    return matching_windows

def close_window(window_title):
    """Attempt to close a window by its title."""
    windows = gw.getWindowsWithTitle(window_title)
    if windows:
        try:
            window = windows[0]
            window.activate()
            pyautogui.hotkey('ctrl', 'w')
        except Exception:
            pass  # Silently pass on errors

def close_tabs():
    """Main function to check and close windows with banned words."""
    while True:
        open_windows = gw.getAllTitles()
        matching_windows = get_matching_windows(open_windows)
        
        # Close windows only if there's a match
        if matching_windows:
            for window in matching_windows:
                close_window(window)
            # After closing windows, wait a bit longer to avoid immediate re-check
            sleep(1)

def main():
    try:
        close_tabs()
    except KeyboardInterrupt:
        pass  # Handle script termination without output
    finally:
        pass  # No need to print anything here either

if __name__ == "__main__":
    main()