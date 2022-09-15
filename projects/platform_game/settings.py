import pygame
from level_editor import *
from btn import Buttons

level_map = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],

]

# Sizes
WIDTH = 1200
HEIGHT = 700
MAX_ROWS = 16
MAX_COLS = 150
TILE_SIZE = HEIGHT // MAX_ROWS

# Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer") #temp name, change this
clock = pygame.time.Clock()
editor = LevelEditor(WIDTH, HEIGHT)

# Background scroll off/on
scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1

# Btn's
btn_imgs = editor.load_images()  
all_btns = []
btn_row = 0
btn_col = 0

    
     
dirt = Buttons(400, 400, btn_imgs[0])


# Draw background
def draw_bg(scroll_var): 
    # Load images
    bg_surf1 = pygame.image.load("projects\\platform_game\\graphics\\bg\\sky_solid_color.png").convert_alpha()
    bg_surf1 = pygame.transform.scale(bg_surf1, (WIDTH, HEIGHT))
    bg_surf2 = pygame.image.load("projects\\platform_game\\graphics\\bg\\clouds.png").convert_alpha()
    bg_surf2 = pygame.transform.scale(bg_surf2, (WIDTH, (HEIGHT//3)))
    bg_surf3 = pygame.image.load("projects\\platform_game\\graphics\\bg\\mountain_depth_z_1.png").convert_alpha()
    bg_surf3 = pygame.transform.scale(bg_surf3, (WIDTH, HEIGHT//2))
    bg_surf4 = pygame.image.load("projects\\platform_game\graphics\\bg\\mountain_depth_z_2.png").convert_alpha()
    bg_surf4 = pygame.transform.scale(bg_surf4, (WIDTH, HEIGHT//3))
    
    width = bg_surf1.get_width()
    
    # Creates frames of image surfaces and positions them, parallax effect
    for x in range(6): 
        screen.blit(bg_surf1, ((width * x) - scroll_var * 0.3,0))
        screen.blit(bg_surf2, ((width * x) - scroll_var * 0.4,0))
        screen.blit(bg_surf3, ((width * x) - scroll_var * 0.5,HEIGHT - (HEIGHT//2)))
        screen.blit(bg_surf4, ((width * x) -scroll_var * 0.6,HEIGHT - (HEIGHT//3)))
        continue
        

            

    
