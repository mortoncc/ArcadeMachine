import pygame
import os

class Life():
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("lumberjack_platformer\\assets", "heart.png")), (32, 32))