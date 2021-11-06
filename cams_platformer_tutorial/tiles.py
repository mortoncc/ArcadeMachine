import pygame
import os

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("lumberjack_platformer\\assets", "middle_grass_tile.png")), (size, size))
        self.rect = self.image.get_rect(topleft = pos)
    
    def update(self, x_shift):
        self.rect.x += x_shift