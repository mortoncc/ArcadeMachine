import pygame 
import os
import time

from pygame import surface
from tiles import Tile
from game_data import levels, lives, add_lives
from settings import tile_size, num_of_lives
from player import Player
from settings import screen_width, screen_height
from win import Win

class Level:
    def __init__(self, current_level, surface, create_overworld, max_level, is_game_over):
        self.display_surface = surface
        self.current_level = current_level
        level_data = levels[current_level]
        level_content = level_data['content']
        self.new_max_level = level_data['unlock']
        self.create_overworld = create_overworld
        self.max_level = max_level
        self.is_game_over = is_game_over

        # level display
        self.font = pygame.font.Font(None, 40)
        #self.text_surf = self.font.render(level_content, True, 'White')
        #self.text_rect = self.text_surf.get_rect(center = (screen_width / 2, screen_height / 2))

        self.setup_level(level_content)
        self.world_shift = 0
        self.background = pygame.transform.scale(pygame.image.load(os.path.join("lumberjack_platformer\\assets", "CloudsBack.png")), (screen_width, screen_height))
    
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.win = pygame.sprite.GroupSingle()
        if self.is_game_over:
            add_lives()
            self.is_game_over = False

        # level placement
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'X':
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == 'W':
                    win_sprite = Win((x,y))
                    self.win.add(win_sprite)
                if cell == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                
    
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8
    
    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
    
    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.canJump = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.create_overworld(self.current_level, self.new_max_level)
        if keys[pygame.K_ESCAPE]:
            self.create_overworld(self.current_level, 0)

    def beat_or_lose_level(self):
        if self.player.sprite.rect.colliderect(self.win.sprite.rect):
            self.create_overworld(self.current_level, self.new_max_level, self.is_game_over)
        if self.player.sprite.rect.top > screen_height + 200:
            self.create_overworld(self.current_level, self.max_level, self.is_game_over)
            if len(lives) > 0:
                lives.pop()
        if len(lives) == 0:
            self.game_over()
    
    def game_over(self):
        self.is_game_over = True
        self.create_overworld(0, 0, self.is_game_over)

    
    def draw_lives(self):
        life_x = 64
        life_y = 64
        for life in lives:
            self.display_surface.blit(life.image, (life_x, life_y))
            life_x = life_x + 32

    def run(self):
        # draw images
        self.display_surface.blit(self.background, (0,0))
        self.draw_lives()
        self.input()

        # level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        self.beat_or_lose_level()

        # player
        self.player.update(self.tiles)
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)

        # win flag
        self.win.update(self.world_shift)
        self.win.draw(self.display_surface)