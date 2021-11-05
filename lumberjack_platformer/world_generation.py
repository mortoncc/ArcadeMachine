import os, sys, pygame
from pygame.locals import *
pygame.init()

# Declares the width and height for the game window
WIDTH, HEIGHT = 750, 750
# Creates the game window of width and height specified above
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
# Sets the caption of the window to "Lumberjack Platformer!"
pygame.display.set_caption("Lumberjack Platformer!")
# Creates the game's FPS counter
clock = pygame.time.Clock()

# constant size (in pixels) for all world tiles generated
# ex: TILE_SIZE = 25 means all world tiles will be 25px x 25px
TILE_SIZE = 50

# loads background images
MAIN_BG = pygame.transform.scale(pygame.image.load(os.path.join("lumberjack_platformer\\assets", "CloudsBack.png")), (WIDTH, HEIGHT))
BOTTOM_CLOUDS = pygame.transform.scale(pygame.image.load(os.path.join("lumberjack_platformer\\assets", "CloudsFront.png")), (WIDTH, HEIGHT))
MOUNTAINS = pygame.transform.scale(pygame.image.load(os.path.join("lumberjack_platformer\\assets", "BGBack.png")), (WIDTH, HEIGHT))

class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.motion = [0, 0]
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("lumberjack_platformer\\assets", "LumberjackMale.png")), (60, 95))
        self.mask = pygame.mask.from_surface(self.image)
    
    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.x -= 10
        if key[pygame.K_RIGHT]:
            self.x += 10
        if key[pygame.K_UP]:
            self.y -= 10
        if key[pygame.K_DOWN]:
            self.y += 10

        SCREEN.blit(self.image, (self.x, self.y))

class World():
    def __init__(self, level):
        # tile_list will hold a list of tuples which each contain (tile image, tile position)
        self.tile_list = []

        # load tile images
        middle_grass = pygame.image.load(os.path.join("lumberjack_platformer\\assets", "middle_grass_tile.png"))

        # traverses through level list passed and appends a tuple with the tile image and position
        row_number = 0
        for row in level:
            col_number = 0
            for tile_key in row:
                # if tile_key = 1, that means we want a grass block in that position
                if tile_key == 1:
                    # scales the tile image to scale
                    img = pygame.transform.scale(middle_grass, (TILE_SIZE, TILE_SIZE))
                    # creates a rectangle that's the same size as the image and updates it's position
                    # this is because images can't have positions but rectangles can
                    img_rect = img.get_rect()
                    img_rect.x = col_number * TILE_SIZE
                    img_rect.y = row_number * TILE_SIZE
                    # creates a tuple called "tile" that has the tile image and the tile rect which holds the position
                    tile = (img, img_rect)
                    # add the tuple above to the tile_list
                    self.tile_list.append(tile)
                col_number += 1
            row_number += 1
    
    def draw(self):
        # draw all tiles in the tile list
        for tile in self.tile_list:
            # tile[0] holds the image and tile[1] holds the position where we want to draw it
            SCREEN.blit(tile[0], tile[1])

def draw_grid():
    for line in range(0, 19):
        pygame.draw.line(SCREEN, (255, 255, 255), (0, line * TILE_SIZE), (WIDTH, line * TILE_SIZE))
        pygame.draw.line(SCREEN, (255, 255, 255), (line * TILE_SIZE, 0), (line * TILE_SIZE, HEIGHT))

# level_1 holds the terrain data for the first level.
# if you change any 0 to a 1, a grass tile will be placed there.
level_1 = [ 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]]

# generates the terrain data using level_1
level = World(level_1)

# creates a player
player = Player(0, HEIGHT - (TILE_SIZE + 80))

# main game loop
while True:
    # draw the background images
    SCREEN.blit(MAIN_BG, (0, 0))
    SCREEN.blit(BOTTOM_CLOUDS, (0, 0))
    SCREEN.blit(MOUNTAINS, (0, 0))

    # creates a grid to help us see the tiles easily
    draw_grid()

    # draws the tiles where they belong
    level.draw()

    player.move()

    # checks all events in the game
    for event in pygame.event.get():
        # if a "quit" event is detected, close the window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            

    # push all changes made to the window
    pygame.display.update()
    # game will run at 60 FPS
    clock.tick(60)