# Import the pygame module
import pygame

# Import random for random numbers
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import *

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

PLAYER_H = 0
PLAYER_V = 0


# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("images\scottyRocket.png").convert()
        # self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (50, 50))
        # self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

        self.rightsideup = True

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

        PLAYER_H = (self.rect.left + self.rect.right) / 2
        PLAYER_V = (self.rect.top + self.rect.bottom) / 2


# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Trash(pygame.sprite.Sprite):
    def __init__(self):
        super(Trash, self).__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((100, 100, 100))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.hspeed = random.randint(1, 5)
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


class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        super(Projectile, self).__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect(
            center=(
                PLAYER_H, PLAYER_V
            )
        )

    def update(self):
        self.rect.move_ip(0, 8)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.kill()


# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a custom event for adding a new enemy
ADDTRASH = pygame.USEREVENT + 1
pygame.time.set_timer(ADDTRASH, 500)

# Instantiate player. Right now, this is just a rectangle.
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
trash = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Variable to keep the main loop running
running = True

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Main loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_SPACE:
                PLAYER_H = (player.rect.left + player.rect.right) / 2
                PLAYER_V = (player.rect.top + player.rect.bottom) / 2
                new_projectile = Projectile()
                projectiles.add(new_projectile)
                all_sprites.add(new_projectile)

        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False

        # Add a new enemy?
        elif event.type == ADDTRASH:
            # Create the new enemy and add it to sprite groups
            new_trash = Trash()
            trash.add(new_trash)
            all_sprites.add(new_trash)

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    # Update enemy position
    trash.update()

    projectiles.update()

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, trash):
        # If so, then remove the player and stop the loop
        player.kill()
        running = False

    pygame.sprite.groupcollide(trash, projectiles, True, True)

    # Update the display
    pygame.display.flip()

    # Ensure program maintains a rate of 60 frames per second
    clock.tick(60)