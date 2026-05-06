import pygame
from constants import *
from functions import *
from widgets import *

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
WORLD_PLATFROMS = []
running = True

WORLD_PLATFROMS.append(("flat-platform-chunk", 0, 0)) #This can be used in world gen

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SCREEN_HEIGHT = screen.get_height()
    SCREEN_WIDTH = screen.get_width()
    PLAYBUTTON = Button(SCREEN_WIDTH/2 - 150, 400, 400, 120, "Play", FONT, BACKGROUND_COLOR, WHITE, BLACK) #Keep this there so it updates to the new screen width
    PLAYBUTTON.update(pygame.mouse.get_pos())

    screen.fill(BACKGROUND_COLOR)
    screen.blit(icon, (SCREEN_WIDTH/2 - icon.get_width()/2, -40))
    screen.blit(title, (SCREEN_WIDTH/2 - title.get_width()/2, 150))
    PLAYBUTTON.draw(screen)
    for name, offset_x, offset_y in WORLD_PLATFROMS:
        draw_tmx(screen, name, offset_x, offset_y)

    win.flip()

pygame.quit()