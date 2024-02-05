import pyautogui
import time
import os

def open_chrome():
    for _ in range(50):
        os.system("start chrome")

def open_word():
    for _ in range(50):
        os.system("start winword")

def open_file_explorer():
    for _ in range(50):
        os.system("start explorer")

def open_steam():
    for _ in range(50):
        os.system("start steam")

def open_teams():
    for _ in range(50):
        os.system("start msteams")

def open_task_manager():
    for _ in range(30):
        os.system("start taskmgr")

if __name__ == "__main__":
    open_chrome()
    time.sleep(0.00001)
    open_word()
    open_file_explorer()
    open_steam()
    open_teams()
    open_task_manager()
