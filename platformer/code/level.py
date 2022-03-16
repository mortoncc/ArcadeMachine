import pygame
from support import import_csv_layout, import_cut_graphics
from settings import tile_size
from tiles import Tile, StaticTile

class Level:
    def __init__(self,level_data,surface):
        #general setup
        self.display_surface = surface
        self.world_shift = -5

        #terrain setup
        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout,'terrain')

        #tree setup
        fordrop_layout = import_csv_layout(level_data['fordrop'])
        self.fordrop_sprites = self.create_tile_group(fordrop_layout,'fordrop')

        #coins setup
        coins_layout = import_csv_layout(level_data['coins'])
        self.coins_sprites = self.create_tile_group(coins_layout,'coins')

    def create_tile_group(self,layout,type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type == 'terrain':
                        terrain_tile_list = import_cut_graphics('../graphics/terrain/grass_tile.png')
                        tile_surface = terrain_tile_list[int(val)]
                        sprite = StaticTile(tile_size,x,y,tile_surface)
                    
                    if type == 'fordrop':
                        fordrop_tile_list = import_cut_graphics('../graphics/decorations/Tree.png')
                        tile_surface = fordrop_tile_list[int(val)]
                        sprite = StaticTile(tile_size,x,y,tile_surface)
                        
                    if type == 'coins':
                        coin_tile_list = import_cut_graphics('../graphics/coins/Pinecone.png')
                        tile_surface = coin_tile_list[int(val)]
                        sprite = StaticTile(tile_size,x,y,tile_surface)

                    sprite_group.add(sprite)

        return sprite_group

    def run(self):
        # run the entire game / level

        # terrain
        self.terrain_sprites.update(self.world_shift)        
        self.terrain_sprites.draw(self.display_surface)

        # fordrop
        self.fordrop_sprites.update(self.world_shift)
        self.fordrop_sprites.draw(self.display_surface)

        # coins
        self.coins_sprites.update(self.world_shift)
        self.coins_sprites.draw(self.display_surface)