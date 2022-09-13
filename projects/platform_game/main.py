from turtle import width
import pygame
from sys import exit
from settings import WIDTH, HEIGHT, clock

# Set up
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer") #temp name, change this

# Background images
bg_surf1 = pygame.image.load("projects\\platform_game\\graphics\\bg\\sky_solid_color.png").convert_alpha()
bg_surf1 = pygame.transform.scale(bg_surf1, (WIDTH, HEIGHT))
bg_surf2 = pygame.image.load("projects\\platform_game\\graphics\\bg\\clouds.png").convert_alpha()
bg_surf2 = pygame.transform.scale(bg_surf2, (WIDTH, (HEIGHT//3)))
bg_surf3 = pygame.image.load("projects\\platform_game\\graphics\\bg\\mountain_depth_z_1.png").convert_alpha()
bg_surf3 = pygame.transform.scale(bg_surf3, (WIDTH, HEIGHT//2))
bg_surf4 = pygame.image.load("projects\\platform_game\graphics\\bg\\mountain_depth_z_2.png").convert_alpha()
bg_surf4 = pygame.transform.scale(bg_surf4, (WIDTH, HEIGHT//3))


while(1): 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()


    # Background display
    screen.blit(bg_surf1, (0,0))
    screen.blit(bg_surf2, (0,0))
    screen.blit(bg_surf3, (0,HEIGHT - (HEIGHT//2)))
    screen.blit(bg_surf4, (0,HEIGHT - (HEIGHT//3)))
    
    
    pygame.display.update()
    clock.tick(60)
            




