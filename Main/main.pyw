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
lock = threading.Lock()

def fetch_banned_words():
    global banned_words
    try:
        with lock:  # Use lock to prevent race conditions when updating banned_words
            response = requests.get(BANNED_WORDS_URL)
            response.raise_for_status()  # Will raise an HTTPError for bad responses
            data = json.loads(response.text)
            banned_words = data.get("banned_words", [])
            print(f"Banned words updated, {len(banned_words)} words.")
    except requests.RequestException as e:
        print(f"Failed to fetch banned words: {e}")
    except json.JSONDecodeError:
        print("Failed to decode JSON response from the server")
    except Exception as e:
        print(f"An unexpected error occurred while fetching banned words: {e}")

def update_banned_words():
    while True:
        fetch_banned_words()
        sleep(60)

def close_window(window_title):
    """Attempt to close a window by its title."""
    try:
        window = gw.getWindowsWithTitle(window_title)[0]
        window.activate()
        pyautogui.hotkey('ctrl', 'w')
        sleep(1)  # Wait a bit to give time for the action to process
    except Exception as e:
        print(f"Error closing window '{window_title}': {e}")

def close_tabs():
    while True:
        if banned_words:
            open_windows = gw.getAllTitles()
            matching_windows = []

            for window in open_windows:
                window_lower = window.lower()
                if any(f' {banned_word.lower()} ' in f' {window_lower} ' for banned_word in banned_words):
                    matching_windows.append(window)

            for window_title in matching_windows:
                close_window(window_title)
        else:
            print("Waiting for banned words to be fetched...")
            sleep(5)

if __name__ == "__main__":
    # Start a thread to fetch banned words every 60 seconds
    threading.Thread(target=update_banned_words, daemon=True).start()

    # Start the main loop to check for and close windows
    close_tabs()