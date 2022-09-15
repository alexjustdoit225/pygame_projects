import pygame
from sys import exit
from settings import *
from level_editor import *
from state_management import *
from level_editor import *

# Set up
pygame.init()
game_state = StateManager()





while(1): 
    
    
    game_state.run_state_manager()
    editor.draw_grid(MAX_COLS, MAX_ROWS, TILE_SIZE, "white")
    clock.tick(60)
            




