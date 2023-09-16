import pygame
import random
from pygame.locals import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define debris by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Debris1(pygame.sprite.Sprite):
    def __init__(self):
        super(Debris1, self).__init__()
        self.surf = pygame.image.load("images\debris1.png").convert()
        self.surf = pygame.transform.scale(self.surf, (50, 50))
        self.surf.set_colorkey((71, 112, 76), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.hspeed = random.randint(5, 20)
        self.vspeed = random.randint(-5, 5)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.hspeed, self.vspeed)
        if self.rect.right < 0:
            self.kill()
        if self.rect.top < 0:
            self.kill()
        if self.rect.bottom > SCREEN_HEIGHT:
            self.kill()