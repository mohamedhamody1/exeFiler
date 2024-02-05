import pyautogui
import time
import os
import random

def open_desktop():
    pyautogui.hotkey('winleft', 'd')

def double_click_randomly():
    desktop_width, desktop_height = pyautogui.size()

    for _ in range(300):
        x = random.randint(0, desktop_width - 1)
        y = random.randint(0, desktop_height - 1)
        
        pyautogui.moveTo(x, y)
        pyautogui.doubleClick()
        
        time.sleep(0.1)

if __name__ == "__main__":
    open_desktop()
    time.sleep(0.2)
    double_click_randomly()
