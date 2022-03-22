import pygame
from settings import screen_height, screen_width

class Game_Over:
    def __init__(self, surface):

        #setup
        self.surface = surface

    def create_menu(self):
        text = 'GAME OVER'
        font = pygame.font.Font(None, 32)
        txt_surface = font.render(text, True, 'white')
        textRect = txt_surface.get_rect()
        textRect.center = (screen_width / 2, screen_height)
        self.surface.blit(text, textRect)
    
    def run(self):
        self.create_menu()