import pygame
import math

BACKGROUND_TILE_PATH = "assets/dirt.png"
BACKGROUND_TILE_SIZE = 128
class Background:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.tile_image = pygame.image.load(BACKGROUND_TILE_PATH)
        self.tile_size = BACKGROUND_TILE_SIZE

    def draw(self, screen):
        for y in range(0, self.screen_height, self.tile_size):
            for x in range(0, self.screen_width, self.tile_size):
                screen.blit(self.tile_image, (x, y))
