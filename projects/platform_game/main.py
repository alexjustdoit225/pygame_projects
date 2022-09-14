import pygame
from sys import exit
from settings import *
from level_editor import *
from state_management import *
from level_editor import *

# Set up
pygame.init()
game_state = StateManager()
editor = LevelEditor()




while(1): 
    
    
    # editor.draw_grid(MAX_COLS, MAX_ROWS)
    game_state.run_state_manager()
    
    clock.tick(60)
            




