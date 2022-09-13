from turtle import width
import pygame
from sys import exit
from settings import WIDTH, HEIGHT, clock

pygame.init()
pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer") #temp name, change this

while(1): 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()





pygame.display.update()
clock.tick(60)
            




