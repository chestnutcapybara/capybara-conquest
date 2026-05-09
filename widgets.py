'''
 --- widgets.py ---
This module includes the Button class which is used to create and manage buttons in the game.'''

import pygame
from constants import *

class Button:
    ''' Class for creating and managing buttons in the game. '''
    def __init__(self, x, y, width, height, text,
                 font,
                 bg_color=BACKGROUNDCOLOR,
                 hover_color=pygame.Color(0,0,0),
                 text_color=pygame.Color(255, 255, 255)):

        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font

        self.bg_color = bg_color
        self.hover_color = hover_color
        self.text_color = text_color

        self.is_hovered = False

    def draw(self, surface):
        ''' Draws the button onto the given surface. '''
        # Change color on hover
        color = self.hover_color if self.is_hovered else self.bg_color
        pygame.draw.rect(surface, color, self.rect, border_radius=8)

        # Render text
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def update(self, mouse_pos):
        ''' Checks if the mouse is hovering over the button and updates the is_hovered attribute. '''
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def is_clicked(self, event):
        ''' Checks if the button was clicked. '''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_hovered:
                return True
        return False