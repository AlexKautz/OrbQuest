import sys
import pygame
import time
import numpy as np
import random
from player import Player
from sword import Sword
from background import Background
# Initialize pygame
pygame.init()
pygame.mixer.init()
import threading

# Play random music function
def play_random_music():
    sample_rate = 44100 # Sample rate in Hz
    duration = 0.5 # Note duration in seconds
    volume = 0.1 # Volume between 0.0 and 1.0

    # Define the scale of notes (in Hz)
    scale = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]

    while True:
        frequency = random.choice(scale)
        samples = np.arange(sample_rate * duration)
        note = np.sin(2 * np.pi * frequency * samples / sample_rate)
        stereo_note = np.ascontiguousarray(np.array([note, note]).T)
        sound = pygame.sndarray.make_sound((volume * 32767 * stereo_note).astype(np.int16))
        sound.play()
        pygame.time.wait(int(duration * 1000))

# Set up display
WIDTH, HEIGHT = 1080, 720

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
game_surface = pygame.Surface((WIDTH, HEIGHT))
pygame.display.set_caption("Orb Quest!")

# Objects
player = Player(WIDTH//2, HEIGHT//2)
sword = Sword(player)
background = Background(WIDTH, HEIGHT)
all_sprites = pygame.sprite.Group(player, sword)

# Game loop
clock = pygame.time.Clock()
FPS = 60
BACKGROUND_COLOR = (0, 0, 0) # black
music_thread = threading.Thread(target=play_random_music, daemon=True)
music_thread.start()
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Update game state
    all_sprites.update()

    # Render game
    game_surface.fill(BACKGROUND_COLOR) # Fills the screen with the background color
    background.draw(game_surface)
    all_sprites.draw(game_surface) # Draws all sprites in the all_sprites sprite group to the screen
    scaled_game_surface = pygame.transform.scale(game_surface, screen.get_size())
    screen.blit(scaled_game_surface, (0, 0)) # Draws the game surface to the screen
    pygame.display.flip() # Updates the display
    clock.tick(FPS) # Waits until 1/FPS seconds have passed since the last time this was called





