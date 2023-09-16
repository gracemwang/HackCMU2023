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

health = 100
score = 0

prev_hit = False

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("scottyRocket.png").convert()
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
        
        PLAYER_H = (self.rect.left + self.rect.right) / 2
        PLAYER_V = (self.rect.top + self.rect.bottom) / 2

# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Debris1(pygame.sprite.Sprite):
    def __init__(self):
        super(Debris1, self).__init__()
        self.surf = pygame.image.load("debris1.png").convert()
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

class Debris2(pygame.sprite.Sprite):
    def __init__(self):
        super(Debris2, self).__init__()
        self.surf = pygame.image.load("debris2.png").convert()
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

class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        super(Projectile, self).__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((200, 200, 200))
        self.rect = self.surf.get_rect(
            center=(
                PLAYER_H, PLAYER_V
            )
        )
    
    def update(self):
        self.rect.move_ip(0, 10 )
        if self.rect.bottom > SCREEN_HEIGHT:
            self.kill()

# def spritecollideany(sprite1, sprite2):
#     if sprite1.rect.right > sprite2.rect.left or sprite1.rect.left > sprite2.rect.right:
#         return False
#     if sprite1.rect.top > sprite2.rect.bottom or sprite1.rect.bottom < sprite2.rect.top:
#         return False
#     return True

# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bg = pygame.transform.scale((pygame.image.load('bgSpace.png')).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a custom event for adding a new enemy
ADDDEBRIS = pygame.USEREVENT + 1
pygame.time.set_timer(ADDDEBRIS, 500)
HIT = pygame.USEREVENT + 2
pygame.time.set_timer(HIT, 1000)

# Instantiate player. Right now, this is just a rectangle.
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
debris1 = pygame.sprite.Group()
debris2 = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

font_health = pygame.font.Font('freesansbold.ttf', 20)
text_health = font_health.render('Health: ' + str(health), True, (255, 255, 255))
textRect_health = text_health.get_rect()
textRect_health.center = (SCREEN_WIDTH - 100, SCREEN_HEIGHT - 80)

font_score = pygame.font.Font('freesansbold.ttf', 20)
text_score = font_health.render('Score: ' + str(score), True, (255, 255, 255))
textRect_score = text_score.get_rect()
textRect_score.center = (SCREEN_WIDTH - 100, SCREEN_HEIGHT - 50)

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
                PLAYER_V = (player.rect.top + player .rect.bottom) / 2     
                new_projectile = Projectile()
                projectiles.add(new_projectile)
                all_sprites.add(new_projectile)
                
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False

        # Add a new enemy?
        elif event.type == ADDDEBRIS:
            # Create the new enemy and add it to sprite groups
            new_debris1 = Debris1()
            debris1.add(new_debris1)
            all_sprites.add(new_debris1)
            new_debris2 = Debris2()
            debris2.add(new_debris2)
            all_sprites.add(new_debris2)
        
        elif event.type == HIT:
            hit1 = pygame.sprite.spritecollide(player, debris1, False)
            hit2 = pygame.sprite.spritecollide(player, debris2, False)
            for hit in hit1:
                health -= 10
                hit.vspeed *= -1
                hit.hspeed *= -1
            for hit in hit2:
                health -= 5
                hit.vspeed *= -1
                hit.hspeed *= -1


    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    # Update enemy position
    debris1.update()
    debris2.update()

    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    projectiles.update()

    # Fill the screen with black
    screen.fill((0, 0, 0))

    screen.blit(bg, (0, 0))

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    
    text_health = font_health.render('Health: ' + str(health), True, (255, 255, 255))
    screen.blit(text_health, textRect_health)
    text_score = font_score.render('Score: ' + str(score), True, (255, 255, 255))
    screen.blit(text_score, textRect_score)

    collide1 = pygame.sprite.groupcollide(projectiles, debris1, True, True)
    collide2 = pygame.sprite.groupcollide(projectiles, debris2, True, True)
    for collide in collide1:
        score += 1
    for collide in collide2:
        score += 1
    
    
    if health <= 0:
        running = False

    # Update the display
    pygame.display.flip()

    # Ensure program maintains a rate of 60 frames per second
    clock.tick(60)