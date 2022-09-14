import pygame, settings, tiles
from settings import *

class LevelEditor: 
    def __init__(self, screen_width, screen_height):
        self.width = screen_width
        self.height = screen_height
        self.margin_right = 300
        self.margin_bottom = 100
        # add edited levels to a dict or list
        self.levels = ""
    
    # Draws editing grid
    def draw_grid(self, max_cols, max_rows, tile_sz, color):
        # Draw vertical lines
        for c in range(1, max_cols + 1):
            pygame.draw.line(settings.screen, color, ((c * tile_sz) - settings.scroll, 0), ((c * tile_sz) - settings.scroll, self.height - self.margin_bottom))
        # Draw horizontal lines
        for r in range(1, max_rows + 1):
            pygame.draw.line(settings.screen, color, (0, r * tile_sz), (self.width - self.margin_right, r * tile_sz))
                
    