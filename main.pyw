from time import sleep
import pygetwindow as gw
import pyautogui
import requests
import json
import threading

# GitHub raw URL for the banned words JSON file
BANNED_WORDS_URL = "https://raw.githubusercontent.com/zgndia/Project-C/refs/heads/main/banned_words.json"

# Global variable to store banned words
banned_words = []

def fetch_banned_words():
    global banned_words
    try:
        response = requests.get(BANNED_WORDS_URL)
        if response.status_code == 200:
            data = json.loads(response.text)
            banned_words = data.get("banned_words", [])
            print("Banned words updated")
        else:
            print(f"Failed to fetch banned words: {response.status_code}")
    except Exception as e:
        print(f"Error fetching banned words: {e}")

def update_banned_words():
    # Update banned words every minute
    while True:
        fetch_banned_words()
        sleep(60)

def close_tabs():
    while True:
        if banned_words:
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
        else:
            print("Waiting for banned words to be fetched...")
            sleep(5)

if __name__ == "__main__":
    # Start a thread to fetch banned words every 60 seconds
    threading.Thread(target=update_banned_words, daemon=True).start()

    # Start the main loop to check for and close windows
    close_tabs()
