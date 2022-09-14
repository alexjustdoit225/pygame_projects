import pygame
from sys import exit
from settings import *
from level_editor import *
from state_management import *

# Set up
pygame.init()
state = State_manager(GAME_STATE)


while(1): 
    state.main_menu()
    if user_clicks_on_space: 
        change the GAME_STATE = state.game_start()
            

    
    pygame.display.update()
    clock.tick(60)
            




