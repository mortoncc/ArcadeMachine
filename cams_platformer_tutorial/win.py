import pygame
import os

class Win(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("lumberjack_platformer\\assets", "flag.png")), (64, 64))
        self.rect = self.image.get_rect(topleft = pos)