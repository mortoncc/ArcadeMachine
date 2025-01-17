import pygame
from settings import screen_height, screen_width
import time

class Game_Over:
    def __init__(self, surface):

        #setup screen
        self.surface = surface

        #setup menu variables
        #create fonts
        self.font = pygame.font.Font(None, 32)
        self.big_font = pygame.font.Font(None, 48)

        #create surfaces
        self.game_over_txt_surface = self.big_font.render('GAME OVER', True, 'red')
        self.continue_txt_surface = self.font.render('CONTINUE', True, 'black', 'white')
        self.quit_txt_surface = self.font.render('QUIT', True, 'white')

        #get rectangles
        self.game_over_txt_Rect = self.game_over_txt_surface.get_rect()
        self.continue_txt_Rect = self.continue_txt_surface.get_rect()
        self.quit_txt_Rect = self.quit_txt_surface.get_rect()

        #set rectangle position
        self.game_over_txt_Rect.center = (screen_width / 2, screen_height / 2)
        self.continue_txt_Rect.center = (screen_width / 2, self.game_over_txt_Rect.y + self.game_over_txt_Rect.height * 2)
        self.quit_txt_Rect.center = (screen_width / 2, self.continue_txt_Rect.y + self.continue_txt_Rect.height * 2)

        #variables for menu selection
        self.selected = 'continue'
        self.key_pressed = False

    def create_menu(self):
        self.surface.blit(self.game_over_txt_surface, self.game_over_txt_Rect)
        self.surface.blit(self.continue_txt_surface, self.continue_txt_Rect)
        self.surface.blit(self.quit_txt_surface, self.quit_txt_Rect)
    
    def user_input(self, events):
        for event in events:
            print("hello")
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN] and not self.key_pressed:
            if self.selected == 'continue':
                self.continue_txt_surface = self.font.render('CONTINUE', True, 'white')
                self.quit_txt_surface = self.font.render('QUIT', True, 'black', 'white')
                self.selected = 'quit'
            else:
                self.continue_txt_surface = self.font.render('CONTINUE', True, 'black', 'white')
                self.quit_txt_surface = self.font.render('QUIT', True, 'white')
                self.selected = 'continue'
            self.key_pressed = True


        if keys[pygame.K_UP] and not self.key_pressed:
            if self.selected == 'continue':
                self.continue_txt_surface = self.font.render('CONTINUE', True, 'white')
                self.quit_txt_surface = self.font.render('QUIT', True, 'black', 'white')
                self.selected = 'quit'
            else:
                self.continue_txt_surface = self.font.render('CONTINUE', True, 'black', 'white')
                self.quit_txt_surface = self.font.render('QUIT', True, 'white')
                self.selected = 'continue'
            self.key_pressed = True
    
    def run(self, events):
        self.create_menu()
        self.user_input(events)