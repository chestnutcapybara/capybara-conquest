import pygame
from constants import *
from functions import *

pygame.init()
pygame.display.init()

# Load icon first
icon = pygame.image.load("icon.ico")

win = pygame.window.Window(
    title="Capybara Conquest",
    size=(800, 600),
    resizable=True
)

# Set the window icon
win.set_icon(icon)

win.maximize()

screen = win.get_surface()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(pygame.Color((255, 255, 255)))
    win.flip()

pygame.quit()