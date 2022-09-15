import pygame
from sys import exit
from settings import *
from level_editor import *
from btn import Buttons

class StateManager: 
    def __init__(self):
        self.state = "intro"
        
        
    def intro(self):
        # Event loop
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN: 
                # Switch to level editor
                if event.key == pygame.K_e: 
                    self.state = "edit_level"
                    settings.scroll = 0
                
             # Switch to main game
            if event.type == pygame.MOUSEBUTTONDOWN: 
                self.state = "main_game"
                settings.scroll = 0
                
    
        # Move background
        settings.scroll += 5
        
    
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
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT: 
                    settings.scroll_left = False
                if event.key == pygame.K_RIGHT: 
                    settings.scroll_right = False
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT: 
                    settings.scroll_speed = 1
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    settings.scroll_left = True
                if event.key == pygame.K_RIGHT:
                    settings.scroll_right = True 
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT: 
                    settings.scroll_speed = 5
                
                # Switch to intro
                if event.key == pygame.K_ESCAPE: 
                    self.state = "intro"
                    settings.scroll = 0
                
        # Move background
        if settings.scroll_left == True and settings.scroll > 0: 
            settings.scroll -= 5 * settings.scroll_speed
        if settings.scroll_right == True: 
            settings.scroll += 5 * settings.scroll_speed

        screen.fill("Grey")
        draw_bg(settings.scroll)
        pygame.draw.line(screen, "blue", (0,0), (600, 600)) #temp code
        
        pygame.display.update()
        
    def edit_level(self): 
        # Event loop
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()
        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT: 
                    settings.scroll_left = False
                if event.key == pygame.K_RIGHT: 
                    settings.scroll_right = False
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT: 
                    settings.scroll_speed = 1
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    settings.scroll_left = True
                if event.key == pygame.K_RIGHT:
                    settings.scroll_right = True 
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT: 
                    settings.scroll_speed = 5
                
                # Switch to intro
                if event.key == pygame.K_i: 
                    self.state = "intro"
                    settings.scroll = 0
                
        # Move background
        if settings.scroll_left == True and settings.scroll > 0: 
            settings.scroll -= 5 * settings.scroll_speed
        if settings.scroll_right == True and settings.scroll < (MAX_COLS * TILE_SIZE) - WIDTH: 
            settings.scroll += 5 * settings.scroll_speed
        
        # add Btn conditions, if clicked then what    
                
                
                
        # Displays background
        screen.fill("Grey")
        draw_bg(settings.scroll)
        pygame.draw.line(screen, "green", (0,0), (600, 600)) #temp code
        editor.draw_grid(MAX_COLS, MAX_ROWS, TILE_SIZE, "white")
        pygame.display.update()
        
    def run_state_manager(self): 
        if self.state == "intro":
            self.intro()
        if self.state == "main_game": 
            self.main_game()
        if self.state == "edit_level": 
            self.edit_level()
    
