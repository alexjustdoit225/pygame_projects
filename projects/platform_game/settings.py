import pygame

level_map = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],

]

# Sizes
TILE_SIZE = 64
WIDTH = 1200
HEIGHT = 700

# Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer") #temp name, change this
clock = pygame.time.Clock()

# Background scroll
scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1


def tile_setup(map): 
    """ Loops through map and returns a new map with tiles.
        :param map: list - level map
        :return new_map: list of objects - tiles 
    """
    new_map = []
    for row_index, rows in enumerate(map): 
        for col_index, cell in enumerate(rows): 
            print(f"(coordinate: {col_index}, {row_index})") #temp code delete later
            print(f"Row: {rows}\nCell: {cell}") 
    
            if cell == 1: # Grass tile
                # tile = Tile(), new_map.append(tile), tile.draw(img_surf), 
                pass
            if cell == 2: # Dirt tile
                pass
    return new_map
            
# Draw background
def draw_bg(): 
    # Load images
    bg_surf1 = pygame.image.load("projects\\platform_game\\graphics\\bg\\sky_solid_color.png").convert_alpha()
    bg_surf1 = pygame.transform.scale(bg_surf1, (WIDTH, HEIGHT))
    bg_surf2 = pygame.image.load("projects\\platform_game\\graphics\\bg\\clouds.png").convert_alpha()
    bg_surf2 = pygame.transform.scale(bg_surf2, (WIDTH, (HEIGHT//3)))
    bg_surf3 = pygame.image.load("projects\\platform_game\\graphics\\bg\\mountain_depth_z_1.png").convert_alpha()
    bg_surf3 = pygame.transform.scale(bg_surf3, (WIDTH, HEIGHT//2))
    bg_surf4 = pygame.image.load("projects\\platform_game\graphics\\bg\\mountain_depth_z_2.png").convert_alpha()
    bg_surf4 = pygame.transform.scale(bg_surf4, (WIDTH, HEIGHT//3))
    
    screen.blit(bg_surf1, (0,0))
    screen.blit(bg_surf2, (0,0))
    screen.blit(bg_surf3, (0,HEIGHT - (HEIGHT//2)))
    screen.blit(bg_surf4, (0,HEIGHT - (HEIGHT//3)))
            
