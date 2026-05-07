from constants import *

import pygame
import functions
import widgets
from functions import *

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

# Load TMX maps
WORLD_PLATFORMS = []
WORLD_PLATFORMS.append(("flat-platform-chunk", 0, 0))
WORLD_PLATFORMS.append(("ladder-platform-chunk", 300, 300))


running = True

scene_state = "menu"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if scene_state == "menu":
        SCREEN_HEIGHT = screen.get_height()
        SCREEN_WIDTH = screen.get_width()
        PLAYBUTTON = widgets.Button(SCREEN_WIDTH/2 - 150, 400, 400, 120, "Play", FONT, BACKGROUNDCOLOR) #Keep this there so it updates to the new screen width
        QUITBUTTON = widgets.Button(SCREEN_WIDTH/2 - 150, 550, 400, 120, "Quit", FONT, BACKGROUNDCOLOR)
        PLAYBUTTON.update(pygame.mouse.get_pos())
        QUITBUTTON.update(pygame.mouse.get_pos())
        if PLAYBUTTON.is_clicked(event):
            scene_state = "game"
        if QUITBUTTON.is_clicked(event):
            running = False
        
        


        screen.fill(BACKGROUNDCOLOR)
        screen.blit(icon, (SCREEN_WIDTH/2 - icon.get_width()/2, -40))
        screen.blit(title, (SCREEN_WIDTH/2 - title.get_width()/2, 150))
        PLAYBUTTON.draw(screen)
        QUITBUTTON.draw(screen)

    elif scene_state == "game":
        screen.fill(BACKGROUNDCOLOR)
        # game things here now...?
        for tmx_data, offset_x, offset_y in WORLD_PLATFORMS:
            functions.draw_tmx(screen, tmx_data, offset_x, offset_y)
    
    win.flip()

pygame.quit()