import pygame, sys
from settings import *
from level import Level
from overworld import Overworld

class Game:
    def __init__(self):
        self.max_level = 3
        self.overworld = Overworld(0, self.max_level, screen)

    def run(self):
        self.overworld.run()


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)
game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #screen.fill('black')
    screen.blit(level.background, (0, 0))
    game.run()
    level.run()

    pygame.display.update()
    clock.tick(60)