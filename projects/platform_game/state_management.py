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
            
                
             # Switch game state
            if event.type == pygame.MOUSEBUTTONDOWN: 
                self.state = "main_game"
                settings.scroll = 0
                
                
    
        # Move background
        # settings.scroll -= 5
        # settings.scroll += 5
        
    
        # Displays background
        screen.fill("Grey")
        draw_bg(settings.scroll)
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
                settings.scroll_left = True
                print(settings.scroll_left) # temp code
            if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                settings.scroll_left = False
                print(settings.scroll_left) # temp code
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                settings.scroll_right = True 
                print(settings.scroll_right) # temp code
            if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                settings.scroll_right = False
                print(settings.scroll_right) # temp code
                
        # Move background
        if settings.scroll_left == True and settings.scroll > 0: 
            settings.scroll -= 5
        if settings.scroll_right == True: 
            settings.scroll += 5

        screen.fill("Grey")
        draw_bg(settings.scroll)
        pygame.draw.line(screen, "blue", (0,0), (600, 600)) #temp code
        
        pygame.display.update()
        
    def run_state_manager(self): 
        if self.state == "intro":
            self.intro()
        if self.state == "main_game": 
            self.main_game()
    
