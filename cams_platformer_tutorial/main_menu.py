import pygame

class Main_menu:
    def __init__(self, screen):
        self.screen = screen

    def create_menu(self):
        font = pygame.font.Font(None, 32)
        
        game_over_txt_surface = font.render('GAME OVER', True, 'white')
        continue_txt_surface = font.render('CONTINUE', True, 'white')
        quit_txt_surface = font.render('QUIT', True, 'white')
        game_over_txt_Rect = game_over_txt_surface.get_rect()
        continue_txt_Rect = continue_txt_surface.get_rect()
        quit_txt_Rect = quit_txt_surface.get_rect()
        game_over_txt_Rect.center = (screen_width / 2, screen_height / 2)
        continue_txt_Rect.center = (screen_width / 2, game_over_txt_Rect.y + game_over_txt_Rect.height * 2)
        quit_txt_Rect.center = (screen_width / 2, continue_txt_Rect.y + continue_txt_Rect.height * 2)
        self.surface.blit(game_over_txt_surface, game_over_txt_Rect)
        self.surface.blit(continue_txt_surface, continue_txt_Rect)
        self.surface.blit(quit_txt_surface, quit_txt_Rect)
    
    def run(self):
        self.create_menu()