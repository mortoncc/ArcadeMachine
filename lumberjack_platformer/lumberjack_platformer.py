import pygame
from pygame.locals import *
import os
pygame.init()

WIDTH, HEIGHT = 750, 750
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lumberjack Platformer!")

MAIN_BG = pygame.transform.scale(pygame.image.load(os.path.join("lumberjack_platformer\\assets", "CloudsBack.png")), (WIDTH, HEIGHT))
BOTTOM_CLOUDS = pygame.transform.scale(pygame.image.load(os.path.join("lumberjack_platformer\\assets", "CloudsFront.png")), (WIDTH, HEIGHT))
MOUNTAINS = pygame.transform.scale(pygame.image.load(os.path.join("lumberjack_platformer\\assets", "BGBack.png")), (WIDTH, HEIGHT))

while True:
    SCREEN.blit(MAIN_BG, (0, 0))
    SCREEN.blit(BOTTOM_CLOUDS, (0, 0))
    SCREEN.blit(MOUNTAINS, (0, 0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

