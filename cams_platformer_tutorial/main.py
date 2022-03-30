import pygame, sys
from settings import *
from level import Level
from overworld import Overworld
from game_over import Game_Over
from main_menu import Main_menu


class Game:
    def __init__(self):
        self.is_game_over = True
        self.max_level = 0
        self.overworld = Overworld(0, self.max_level, screen, self.create_level, self.is_game_over)
        self.status = 'overworld'
        self.game_over = Game_Over(screen)
        self.main_menu = Main_menu(screen)

    def create_level(self, current_level, is_game_over):
        self.level = Level(current_level, screen, self.create_overworld, self.max_level, is_game_over, self.display_game_over)
        self.status = 'level'

    def create_overworld(self, current_level, new_max_level, is_game_over):
        if new_max_level > self.max_level:
            self.max_level = new_max_level
        if new_max_level < self.max_level:
            self.max_level = new_max_level
        self.overworld = Overworld(current_level, self.max_level, screen, self.create_level, is_game_over)
        self.status = 'overworld'
    
    def display_game_over(self):
        self.status = 'game over'

    def create_main_menu(self):
        self.status = 'main menu'

    def run(self):
        if self.status == 'overworld':
            self.overworld.run()
        elif self.status == 'game over':
            self.game_over.run()
        elif self.status == 'main menu':
            self.main_menu.run()
        else:
            self.level.run()


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
#level = Level(level_map, screen)
game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    game.run()

    pygame.display.update()
    clock.tick(60)