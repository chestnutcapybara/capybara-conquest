import pygame
from constants import *
from functions import *

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

screen = win.get_surface()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)
    screen.blit(CAPYBARACONQUESTTITLE, (SCREEN_WIDTH/2 - CAPYBARACONQUESTTITLE.get_width()/2, 150))
    screen.blit(icon, (SCREEN_WIDTH/2 - icon.get_width()/2, SCREEN_HEIGHT/2 - icon.get_height()/2))

    win.flip()

pygame.quit()