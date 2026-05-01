import pygame

pygame.init()
pygame.display.init()

win = pygame.window.Window(title="My Game", size=(800, 600), resizable=True)

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