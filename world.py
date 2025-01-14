import pygame

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

#define game variables
tile_size = 20


#load images
sun_img = pygame.image.load('img/sun.png')

#Scaling image to screen size
bg_img = pygame.image.load('img/sky.png')
bg_img = pygame.transform.scale(bg_img, (screen_height,screen_width))


class World():
    def __init__(self, data):
        self.tile_list = []
        #load images
        dirt_img = pygame.image.load('img/dirt.png')
        grass_img = pygame.image.load('img/grass.png')
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1
                    
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
