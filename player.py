import pygame
import math

SPRITE_IMAGE_PATH = "assets/player.png"

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y,):
        super().__init__()
        self.image = pygame.image.load(SPRITE_IMAGE_PATH)
        self.original_image = self.image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.angle = 0
    
    def update(self):
        SPEED = 4
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0

        # Detect if the W key is pressed
        if keys[pygame.K_w]:
            dy -= SPEED
        # Detect if the A key is pressed
        if keys[pygame.K_a]:
            dx -= SPEED
        # Detect if the S key is pressed
        if keys[pygame.K_s]:
            dy += SPEED
        # Detect if the D key is pressed
        if keys[pygame.K_d]:
            dx += SPEED
        
        # Normalize the diagonal speed
        if dx != 0 and dy != 0:
            dx *= 0.7071
            dy *= 0.7071
        
        # Update the position
        self.rect.x += dx
        self.rect.y += dy

        # Update the angle
        if dx != 0 or dy != 0:
            self.angle = math.degrees(math.atan2(dy, dx)) + 90
            self.image = pygame.transform.rotate(self.original_image, -self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)
        
