import pygame
from sys import exit
from settings import *
from level_editor import *

class StateManager: 
    def __init__(self):
        self.state = "intro"
        
        
    def intro(self):
        # Event loop
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.key.get_pressed(pygame.KEY_LEFT): 
                scroll_left = True
            if event.type == pygame.KEYDOWN and event.key == pygame.key.get_pressed(pygame.KEY_RIGHT):
                scroll_right = True 
            if event.type == pygame.MOUSEBUTTONDOWN: 
                self.state = "main_game"
            
        # Displays background
        draw_bg()
        pygame.draw.line(screen, "red", (0,0), (600, 600)) #temp code
        
        pygame.display.update()

    def main_game(self):
        # Event loop
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.key.get_pressed(pygame.KEY_LEFT): 
                scroll_left = True
            if event.type == pygame.KEYDOWN and event.key == pygame.key.get_pressed(pygame.KEY_RIGHT):
                scroll_right = True 
            
        draw_bg()
        pygame.draw.line(screen, "blue", (0,0), (600, 600)) #temp code
        
        pygame.display.update()
        
    def run_state_manager(self): 
        if self.state == "intro":
            self.intro()
        if self.state == "main_game": 
            self.main_game()
    
