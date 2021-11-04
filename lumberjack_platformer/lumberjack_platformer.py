import pygame
import os
pygame.init()

WIDTH, HEIGHT = 750, 750
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lumberjack Platformer!")

MAIN_BG = pygame.transform.scale(pygame.image.load(os.path.join("lumberjack_platformer\\assets", "CloudsBack.png")), (WIDTH, HEIGHT))
BOTTOM_CLOUDS = pygame.transform.scale(pygame.image.load(os.path.join("lumberjack_platformer\\assets", "CloudsFront.png")), (WIDTH, HEIGHT))
MOUNTAINS = pygame.transform.scale(pygame.image.load(os.path.join("lumberjack_platformer\\assets", "BGBack.png")), (WIDTH, HEIGHT))
MIDDLE_GRASS_TILE_IMG = pygame.transform.scale(pygame.image.load(os.path.join("lumberjack_platformer\\assets", "middle_grass_tile.png")), (64, 64))
MIDDLE_GRASS_TILE = pygame.mask.from_surface(MIDDLE_GRASS_TILE_IMG)
PLAYER_IMG =  pygame.transform.scale(pygame.image.load(os.path.join("lumberjack_platformer\\assets", "LumberjackMale.png")), (64, 64))
PLAYER_MOTION = [0, 0]
class tile:
    # Constructor
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
    
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

class player:
    # Constructor
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
    
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    # If there is any overlap between the object's masks, return true, else, return false
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

player = player(WIDTH/2,HEIGHT/2,PLAYER_IMG)
tile = tile(WIDTH/2-32, HEIGHT-64, MIDDLE_GRASS_TILE_IMG)

while True:
    SCREEN.blit(MAIN_BG, (0, 0))
    SCREEN.blit(BOTTOM_CLOUDS, (0, 0))
    SCREEN.blit(MOUNTAINS, (0, 0))
    tile.draw(SCREEN)
    player.draw(SCREEN)

    # Gravity :)
    if collide(player, tile):
        PLAYER_MOTION[1] = 0
    else:
        PLAYER_MOTION[1] = +10

    player.x += PLAYER_MOTION[0]
    player.y += PLAYER_MOTION[1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
    
pygame.quit()
