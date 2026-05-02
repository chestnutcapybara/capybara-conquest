from __future__ import annotations
import pygame, json, sys
from pathlib import Path
from typing import Any
from constants import *
if __name__ == "__main__":
    raise CapybaraConquestError("This file is not meant to be run directly, it contains utility functions for the game. Please run main.py instead.")

def resolve_path(relative_path: str) -> Path:
    if hasattr(sys, "_MEIPASS"):
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = Path(getattr(sys, "_MEIPASS"))
    else:
        # In development, use the current working directory
        base_path = Path(".").resolve()

    return base_path / Path(relative_path)

def load_font(path: str, font_size: int) -> pygame.font.Font:
    try:
        return pygame.font.Font(resolve_path(path), font_size)
    except FileNotFoundError:
        print(f"{resolve_path(path)} not found, defaulting to system font.")
        return pygame.font.SysFont(None, font_size)
    except Exception as exc:
        raise RuntimeError(f"Failed loading font from {path}, {exc}") from exc

def load_image(path: str, alpha: bool) -> pygame.Surface:
    try:
        if alpha is True:
            return pygame.image.load(resolve_path(path)).convert_alpha()
        return pygame.image.load(resolve_path(path)).convert()
    except FileNotFoundError:
        raise FileNotFoundError(f"{resolve_path(path)} not found!") from FileNotFoundError
    except Exception as exc:
        raise RuntimeError(f"Failed loading image from {path}, {exc}") from exc
    
def load_sound(path: str) -> pygame.mixer.Sound:
    try:
        return pygame.mixer.Sound(resolve_path(path))
    except FileNotFoundError:
        raise FileNotFoundError(f"{resolve_path(path)} not found!") from FileNotFoundError
    except Exception as exc:
        raise RuntimeError(f"Failed loading Sound from: {path}, {exc}") from exc

def open_json(path: str) -> Any:
    try:
        with open(resolve_path(path), "r") as f:
            return json.load(f)
    except OSError as exc:
        raise OSError(f"Failed to open {path}, {exc}") from exc
