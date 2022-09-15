import pygame
from settings import *

# Create buttons
class Buttons: 
    def __init__(self, x, y, img):
        self.img = img
        self.rect = self.img.get_rect(topleft= (x, y))
        self.clicked = False

    # draw button on screen, returns True or False if btn is clicked
    def draw(self, surface): 
        action = False
        # Get mouse position
        pos = pygame.mouse.get_pos()
        
        # Check if mouse is over button and clicked conditions
        if self.rect.collidepoint((pos)): 
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: 
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0: 
                self.clicked = False
                action = False
                
        # Draw btn on screen
        surface.blit(self.img, (self.rect.x, self.rect.y))
        return action
    