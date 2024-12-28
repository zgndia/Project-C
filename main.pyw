from time import sleep
import pygetwindow as gw
import pyautogui

banned_words = ["elmusto", "organize", "organıze", "jeff redd", "ati242", "blok3", "heijan", "batuflex", "era7capone", "lvbel c5", "ali471", "şehinşah", "sehinsah", "motive", "deha", "ben fero", "aykut closer", "akdo", "mero", "uzi", "cistak", "cıstak"]

def close_tabs():
    while True:
        # Check for all open windows
        open_windows = gw.getAllTitles()
        
        # Initialize a list to store matching windows
        matching_windows = []
        
        # Check for banned words in open window titles
        for banned_word in banned_words:
            for window in open_windows:
                if banned_word.lower() in window.lower():
                    matching_windows.append(window)
        
        # Close all matching windows
        for window_title in matching_windows:
            try:
                # Focus the matching window
                window = gw.getWindowsWithTitle(window_title)[0]
                window.activate()
                
                # Close the window using the keyboard shortcut (e.g., Ctrl+W)
                pyautogui.hotkey('ctrl', 'w')
                sleep(1)

            except Exception as e:
                print(f"Error closing window {window_title}: {e}")

if __name__ == "__main__":
    close_tabs()
