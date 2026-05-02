# WARNING - This game uses pygame-ce, which is NOT normal pygame but uses the same name (pygame)
# Pygame-CE (Pygame Community Edition) is a fork of the original Pygame library that is actively maintained and has additional features and improvements.
# You can install it with pip install pygame-ce but make sure you uninstall normal Pygame first (if you have it)

import pygame

pygame.init()
pygame.display.init()

icon = pygame.image.load("icon.ico")
win = pygame.window.Window(title="My Game", size=(800, 600), resizable=True)

win.maximize()

screen = win.get_surface()
pygame.display.set_icon(icon)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(pygame.Color((255, 255, 255)))
    

    win.flip()

pygame.quit()