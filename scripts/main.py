"""v1.0.0"""

import pygame
import sys
from globals import *
from scene import Scene

class Game():
    def __init__(self):
        
        self.screen: pygame.Surface = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.scene = Scene(self.screen)

        self.running = True

    def run(self):
        while self.running:
            self.update()
        self.finish()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
        
        self.screen.fill(BLACK)
        self.scene.update()

        pygame.display.update()
        self.clock.tick(FPS)
    
    def finish(self):
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.run()