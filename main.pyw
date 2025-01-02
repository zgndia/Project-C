from time import sleep
import pygetwindow as gw
import pyautogui
import requests
import json

# GitHub raw URL for the banned words JSON file
BANNED_WORDS_URL = "https://raw.githubusercontent.com/username/repository/branch/banned_words.json"

def fetch_banned_words():
    try:
        response = requests.get(BANNED_WORDS_URL)
        if response.status_code == 200:
            data = json.loads(response.text)
            return data.get("banned_words", [])
        else:
            print(f"Failed to fetch banned words: {response.status_code}")
            return []
    except Exception as e:
        print(f"Error fetching banned words: {e}")
        return []

def close_tabs():
    banned_words = fetch_banned_words()
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
