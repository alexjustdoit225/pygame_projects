import pygame
from sys import exit
from settings import *
from level_editor import *
from state_management import *

# Set up
pygame.init()
game_state = StateManager()




while(1): 
    
    
    
    game_state.run_state_manager()
    clock.tick(60)
            




