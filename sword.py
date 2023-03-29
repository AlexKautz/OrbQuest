import pygame
import math


SPRITE_IMAGE_PATH = "assets/sword.png"
SWORD_OFFSET = -70
SWORD_SWING_SPEED = -20
SWORD_SWING_ANGLE = -180
SWORD_SWING_STARTING_ANGLE = 90

class Sword(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.original_image = pygame.image.load(SPRITE_IMAGE_PATH)
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.angle = 0
        self.swing_start_angle = self.angle + SWORD_SWING_STARTING_ANGLE
        self.swinging = False
        self.key_pressable = True

    def update(self):
        self.rect.center = self.player.rect.center



        # Update the sword's angle based on the player's angle
        keys = pygame.key.get_pressed()
        if not self.swinging:
            self.angle = self.player.angle + SWORD_SWING_STARTING_ANGLE
            if not keys[pygame.K_SPACE]:
                self.key_pressable = True


        # Check if the spacebar is pressed and the sword is not already swinging
        if keys[pygame.K_SPACE] and self.key_pressable and not self.swinging:
            self.swinging = True
            self.key_pressable = False
            self.swing_start_angle = self.angle

        # Handle sword swinging
        if self.swinging:
            self.angle += SWORD_SWING_SPEED
            if self.angle <= self.swing_start_angle + SWORD_SWING_ANGLE:
                self.swinging = False

        self.image = pygame.transform.rotate(self.original_image, -self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        # Calculate the offset of the sword from the player's center
        offset_x = SWORD_OFFSET * math.cos(math.radians(self.angle + 90))
        offset_y = SWORD_OFFSET * math.sin(math.radians(self.angle + 90))

        # Update the sword's position based on the calculated offset
        self.rect.centerx += offset_x
        self.rect.centery += offset_y