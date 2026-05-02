from __future__ import annotations
import pygame

class CapybaraConquestError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

if __name__ == "__main__":
    raise CapybaraConquestError("This file is not meant to be run directly, it contains constants for the game. Please run main.py instead.")


BACKGROUND_COLOR = (237, 199, 154)
