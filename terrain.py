from __future__ import annotations
from pytmx.util_pygame import load_pygame

import pygame
import pytmx

from constants import *

def draw_tmx(screen,name: str,offset_x: int, offset_y: int):
    tmx_data = load_pygame(f"assets/tiles/{name}.tmx")
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer.tiles():
                tile_image = tmx_data.get_tile_image_by_gid(gid)
                if tile_image:
                    tile_image = pygame.transform.scale(tile_image, (TILE_SIZE, TILE_SIZE))
                    screen.blit(tile_image, (x * tmx_data.tilewidth * (TILE_SIZE / tmx_data.tilewidth) + offset_x, 
                                             y * tmx_data.tileheight * (TILE_SIZE / tmx_data.tileheight) + offset_y))