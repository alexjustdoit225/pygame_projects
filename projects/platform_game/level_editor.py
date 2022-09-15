import pygame, settings, tiles
from settings import *
from btn import Buttons

class LevelEditor: 
    def __init__(self, screen_width, screen_height):
        self.width = screen_width
        self.height = screen_height
        self.margin_right = 300
        self.margin_bottom = 100
        self.tile_types = 2
        self.tile_list = []
        # add edited levels to a dict or list
        self.levels = ""
        
        
    # Loops through and loads images, scales image and appends image to list, returns a list of images
    def load_images(self): 
        for x in range(self.tile_types): 
            tile_img = pygame.image.load(f'projects\\platform_game\\graphics\\tiles\\{x}.png')  
            tile_img = pygame.transform.scale(tile_img, (settings.TILE_SIZE, settings.TILE_SIZE))
            self.tile_list.append(tile_img)
        return (self.tile_list)
    
    # Draws editing grid
    def draw_grid(self, max_cols, max_rows, tile_sz, color):
        # Draw vertical lines
        for c in range(1, max_cols + 1):
            pygame.draw.line(settings.screen, color, ((c * tile_sz) - settings.scroll, 0), ((c * tile_sz) - settings.scroll, self.height - self.margin_bottom))
        # Draw horizontal lines
        for r in range(1, max_rows + 1):
            pygame.draw.line(settings.screen, color, (0, r * tile_sz), (self.width - self.margin_right, r * tile_sz))
                
    