import pygame
from sys import exit
from settings import *
from level_editor import *

class State_manager: 
    def __init__(self, state):
        self.state = state
        
    def main_menu(self):
        self.state = "main_menu"
        while self.state == "main_menu":
            # Displays background
            draw_bg()
            # Event loop
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.key.get_pressed(pygame.KEY_LEFT): 
                    scroll_left = True
                if event.type == pygame.KEYDOWN and event.key == pygame.key.get_pressed(pygame.KEY_RIGHT):
                    scroll_right = True 
            
            pygame.draw.line(screen, "red", (0,0), (600, 600))
            return self.state

    def game_start(): 
        pass
    