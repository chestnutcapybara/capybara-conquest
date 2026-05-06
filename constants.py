from __future__ import annotations
import pygame

pygame.font.init()

class CapybaraConquestError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

if __name__ == "__main__":
    raise CapybaraConquestError("This file is not meant to be run directly, it contains constants for the game. Please run main.py instead.")

BACKGROUNDCOLOR = (237, 199, 154)
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1200
FONT = pygame.font.Font("assets/fonts/Capybara.ttf", 96)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)