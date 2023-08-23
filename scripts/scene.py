import pygame
import random as rng
from globals import *

class Scene():
    def __init__(self, display: pygame.Surface) -> None:
        self.player = ()
        self.screen = display
        self.room = Room()
        pygame.font.init()
        self.small_font = pygame.font.SysFont("Lucida Consola", 32)

    def update(self):
        self._draw()

    def _draw(self):
        pass

    

        

class Room():
    def __init__(self) -> None:
        self.rows = 0
        self.columms = 0

    def generate(self):
        self.rows = rng.randint(5, 16)
        self.columms = rng.randint(5, 16)

        for row in range(self.rows):
            for columms in range(self.columms):
                pass