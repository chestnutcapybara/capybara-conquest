'''
 --- animation.py ---
This module includes the class Animation which is a fully functional animation system.

'''

# Imports
from __future__ import annotations
import pygame  # type: ignore
from constants import *

class Animation:
    ''' The Animation class which is used to manage and create animations. '''
    def __init__(
        self,
        frames: list[pygame.Surface],
        frame_duration: float,
        loop: bool = True,
    ):
        self.frames = frames
        self.frame_duration = frame_duration
        self.loop = loop

        self.current_frame = 0
        self.timer = 0

    def update(self, dt: float):
        ''' Updates the animation based on Delta-Time (dt) '''
        self.timer += dt

        if self.timer >= self.frame_duration:
            self.timer = 0
            self.current_frame += 1

            if self.current_frame >= len(self.frames):
                if self.loop:
                    self.current_frame = 0
                else:
                    self.current_frame = len(self.frames) - 1

    def get_frame(self) -> pygame.Surface:
        ''' Returns the current frame of the animation '''
        return self.frames[self.current_frame]

    def reset(self):
        ''' Resets the animation to first frame '''
        self.current_frame = 0
        self.timer = 0