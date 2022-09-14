import pygame
from sys import exit
from settings import *

# Set up
pygame.init()




while(1): 
    # Displays background
    draw_bg()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()


    get_map_info(level_map)
    
    
    pygame.display.update()
    clock.tick(60)
            




