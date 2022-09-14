import pygame
from sys import exit
from settings import *
from level_editor import *

class StateManager: 
    def __init__(self):
        self.state = "intro"
        # Background scroll off/on
        self.scroll_left = False
        self.scroll_right = False
        self.scroll = 0
        self.scroll_speed = 1
        
        
    def intro(self):
        # Event loop
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()
            
            # Scrolling background
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT: 
                self.scroll_left = True
                print(self.scroll_left)
            if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                self.scroll_left = False
                print(self.scroll_left)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.scroll_right = True 
                print(self.scroll_right)
            if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                self.scroll_right = False
                print(self.scroll_right)
                
            # Switch game state
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
                
            # Scrolling background
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT: 
                self.scroll_left = True
                print(self.scroll_left)
            if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                self.scroll_left = False
                print(self.scroll_left)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.scroll_right = True 
                print(self.scroll_right)
            if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                self.scroll_right = False
                print(self.scroll_right)
                
        # Move background
        if self.scroll_left == True: 
            self.scroll -= 5
        if self.scroll_right == True: 
            self.scroll += 5

            
        draw_bg()
        pygame.draw.line(screen, "blue", (0,0), (600, 600)) #temp code
        
        pygame.display.update()
        
    def run_state_manager(self): 
        if self.state == "intro":
            self.intro()
        if self.state == "main_game": 
            self.main_game()
    
