import pygame
import os, sys


from pygame.constants import K_UP, KEYDOWN
from tiles import Tile

pygame.init()

WIDTH, HEIGHT = 750, 750
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lumberjack Platformer!")
clock = pygame.time.Clock()

MAIN_BG = pygame.transform.scale(pygame.image.load(os.path.join("lumberjack_platformer\\assets", "CloudsBack.png")), (WIDTH, HEIGHT))
BOTTOM_CLOUDS = pygame.transform.scale(pygame.image.load(os.path.join("lumberjack_platformer\\assets", "CloudsFront.png")), (WIDTH, HEIGHT))
MOUNTAINS = pygame.transform.scale(pygame.image.load(os.path.join("lumberjack_platformer\\assets", "BGBack.png")), (WIDTH, HEIGHT))
MIDDLE_GRASS_TILE_IMG = pygame.transform.scale(pygame.image.load(os.path.join("lumberjack_platformer\\assets", "middle_grass_tile.png")), (64, 64))
MIDDLE_GRASS_TILE = pygame.mask.from_surface(MIDDLE_GRASS_TILE_IMG)
PLAYER_IMG =  pygame.transform.scale(pygame.image.load(os.path.join("lumberjack_platformer\\assets", "LumberjackMale.png")), (64, 64))
PINECONE = pygame.transform.scale(pygame.image.load(os.path.join("lumberjack_platformer\\assets", "Pinecone.png")), (30, 30))
TREE = pygame.transform.scale(pygame.image.load(os.path.join("lumberjack_platformer\\assets", "Tree.png")), (350, 350))
BEARKAT = pygame.transform.scale(pygame.image.load(os.path.join("lumberjack_platformer\\assets", "Bearkat.png")), (64, 64))
PLAYER_MOTION = [0, 0]



class cone:
    # Constructor
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
    
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

class tree:
    # Constructor
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
    
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

class villan:
    # Constructor
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
    
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

class Player:
    # Constructor
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
        self.isJump = False
        self.jumpCount = 10
    
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
        

def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    # If there is any overlap between the object's masks, return true, else, return false
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

player = Player(WIDTH/2,HEIGHT/2,PLAYER_IMG)
Tile = Tile(WIDTH/2-32, HEIGHT-64, MIDDLE_GRASS_TILE_IMG)
cone = cone(WIDTH/2+100, HEIGHT-30, PINECONE)
tree = tree(WIDTH/2+100, HEIGHT-350, TREE)
villan = villan(WIDTH/2+125, HEIGHT-56, BEARKAT)

isJump = False
jumpCount = 10

while True:
    SCREEN.blit(MAIN_BG, (0, 0))
    SCREEN.blit(BOTTOM_CLOUDS, (0, 0))
    SCREEN.blit(MOUNTAINS, (0, 0))
    Tile.draw(SCREEN)
    player.draw(SCREEN)
    cone.draw(SCREEN)
    tree.draw(SCREEN)
    villan.draw(SCREEN)

    #Gravity :)
    if collide(player, Tile):
        PLAYER_MOTION[1] = 0
    if (player.y + player.img.get_height()) >= HEIGHT:
        PLAYER_MOTION[1] = 0
        player.y = HEIGHT - 64
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and player.x - 10 < 0:
        player.x = 0
    elif keys[pygame.K_LEFT] and collide(player, Tile):
        player.x = (Tile.x + Tile.img.get_width())
    elif keys[pygame.K_LEFT]:
        player.x -= 10
    if keys[pygame.K_RIGHT] and (player.x + player.img.get_width()) + 10 > WIDTH:
        player.x = WIDTH - 54
    elif keys[pygame.K_RIGHT]:
        player.x += 10
    #elif keys[pygame.K_RIGHT] and collide(player, tile):
    #    player.x = 
    if not(isJump):
        PLAYER_MOTION[1] = 10
        player.x += PLAYER_MOTION[0]
        if player.y + 64 < HEIGHT:
            player.y += PLAYER_MOTION[1]
        if keys[pygame.K_UP]:
            isJump = True
    else:
        if jumpCount >= -10:
            print(player.y)
            player.y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(60)
    