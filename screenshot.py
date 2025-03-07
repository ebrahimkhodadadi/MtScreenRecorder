import os
import time
import pyautogui

VIDEO_FOLDER = os.getcwd()  # Change this to your video folder path

def capture_screenshot():
    """Capture a screenshot of the MetaTrader chart."""
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(VIDEO_FOLDER, f"screenshot_{timestamp}.png")
    screenshot = pyautogui.screenshot()
    screenshot.save(file_path)
    print(f"Screenshot saved: {file_path}")