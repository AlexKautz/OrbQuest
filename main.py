import sys
import pygame
import time
from player import Player

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 1080, 720
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Orb Quest!")

# Objects
player = Player(WIDTH//2, HEIGHT//2)
all_sprites = pygame.sprite.Group(player)

# Game loop
clock = pygame.time.Clock()
FPS = 60
BACKGROUND_COLOR = (0, 0, 0) # black
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Update game state
    all_sprites.update()

    # Render game
    window.fill(BACKGROUND_COLOR) # Fills the screen with the background color
    all_sprites.draw(window) # Draws all sprites in the all_sprites sprite group to the screen
    pygame.display.flip() # Updates the display
    clock.tick(FPS) # Waits until 1/FPS seconds have passed since the last time this was called





