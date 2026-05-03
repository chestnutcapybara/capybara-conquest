import pygame
from constants import *
from functions import *

# Constants
FONT = pygame.font.Font("assets/fonts/Capybara.ttf", 96)

# Variables
title = FONT.render("Capybara Conquest", True, (0, 0, 0))

pygame.init()
pygame.display.init()

# Load icon first
icon = pygame.image.load("icon.ico")

win = pygame.window.Window(
    title="Capybara Conquest",
    size=(SCREEN_WIDTH, SCREEN_HEIGHT),
    resizable=True
)

# Set the window icon
win.set_icon(icon)
win.maximize()
screen = win.get_surface()
SCREEN_HEIGHT = screen.get_height()
SCREEN_WIDTH = screen.get_width()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SCREEN_HEIGHT = screen.get_height()
    SCREEN_WIDTH = screen.get_width()

    screen.fill(BACKGROUND_COLOR)
    screen.blit(icon, (SCREEN_WIDTH/2 - icon.get_width()/2, -40))
    screen.blit(title, (SCREEN_WIDTH/2 - title.get_width()/2, 150))
    
    win.flip()

pygame.quit()