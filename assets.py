from __future__ import annotations

import pygame
from pathlib import Path

class SpriteSheet:
    def __init__(self, image: pygame.Surface):
        self.sheet = image

    def cut(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
    ) -> pygame.Surface:

        sprite = pygame.Surface((width, height), pygame.SRCALPHA)

        sprite.blit(
            self.sheet,
            (0, 0),
            (x, y, width, height),
        )

        return sprite.convert_alpha()

    def cut_strip(
        self,
        start_x: int,
        y: int,
        width: int,
        height: int,
        amount: int,
    ) -> list[pygame.Surface]:
        """
        Cuts sprites lined up horizontally.

        Example:
        [sprite][sprite][sprite][sprite][ sprite][chestnutcapybara]
        """

        sprites = []

        for i in range(amount):
            x = start_x + (i * width)

            sprite = self.cut(
                x,
                y,
                width,
                height,
            )

            sprites.append(sprite)

        return sprites
    

class AssetManager:
    def __init__(self):
        # Stores already-loaded images
        self.assets: dict[str, pygame.Surface] = {}

    def load_image(
        self,
        name: str,
        path: str | Path,
        convert_alpha: bool = True,
    ) -> pygame.Surface:
        # Loads a image and stores it in Asset Manager Cache
        # If image exists in cache already... then just return the cached version instead of loading it again

        # Return cached version if already loaded
        if name in self.assets:
            return self.assets[name]

        image = pygame.image.load(path)

        # performance
        if convert_alpha:
            image = image.convert_alpha()
        else:
            image = image.convert()

        self.assets[name] = image
        return image

    def get_image(self, name: str) -> pygame.Surface:
        # gets an image from the cache

        if name not in self.assets:
            raise KeyError(f'Image "{name}" has not been loaded.')

        return self.assets[name]

    def unload_image(self, name: str) -> None:
        # unloads an image from the cache
        #removes RAM usage by deleting the image from the cache

        if name in self.assets:
            del self.assets[name]

    def clear(self) -> None:
        # DELETES ALL THINGS FROM THE CACHE

        self.assets.clear()