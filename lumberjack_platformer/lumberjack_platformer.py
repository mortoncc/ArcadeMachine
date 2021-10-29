import pygame
import os
pygame.init()

WIDTH, HEIGHT = 750, 750
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lumberjack Platformer!")

MAIN_BG = pygame.transform.scale(pygame.image.load(os.path.join("lumberjack_platformer\\assets", "CloudsBack.png")), (WIDTH, HEIGHT))
BOTTOM_CLOUDS = pygame.transform.scale(pygame.image.load(os.path.join("lumberjack_platformer\\assets", "CloudsFront.png")), (WIDTH, HEIGHT))
MOUNTAINS = pygame.transform.scale(pygame.image.load(os.path.join("lumberjack_platformer\\assets", "BGBack.png")), (WIDTH, HEIGHT))
GRASS_TILES = pygame.transform.scale(pygame.image.load(os.path.join("lumberjack_platformer\\assets", "middle_grass_tile.png")), (64, 64))
PLAYER =  pygame.transform.scale(pygame.image.load(os.path.join("lumberjack_platformer\\assets", "LumberjackMale.png")), (64, 64))
while True:
    SCREEN.blit(MAIN_BG, (0, 0))
    SCREEN.blit(BOTTOM_CLOUDS, (0, 0))
    SCREEN.blit(MOUNTAINS, (0, 0))
    SCREEN.blit(GRASS_TILES, (WIDTH/2-32,HEIGHT-64))
    SCREEN.blit(PLAYER, (WIDTH/2, HEIGHT/2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
    
pygame.quit()
