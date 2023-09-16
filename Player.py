import pygame
import random
from pygame.locals import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define a player object by extending pygame.sprite.Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("images\scottyRocket.png").convert()
        # self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (100, 100))
        # self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

        self.hspeed = 5
        self.vspeed = 5

        self.rect = self.surf.get_rect(
            center=(
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2,
            )
        )

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1 * self.vspeed)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, self.vspeed)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1 * self.hspeed, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.hspeed, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT