import pygame
import random
from pygame.locals import *

import Player as p
import Debris1 as d1
import Debris2 as d2

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

RED = (255, 0, 0)
GRAY = (50, 50, 50)

PLAYER_H = 0
PLAYER_V = 0

health = 100
score = 0

prev_hit = False
game=False

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
        self.rect.move_ip(0, 10)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.kill()

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()

        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image,
                        color,
                        pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveForward(self, speed):
        self.rect.y += speed * speed/10

    def moveBack(self, speed):
        self.rect.y -= speed * speed/10

def button(screen, position, text):
    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, (255, 0, 0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w , h))
    #print("screen.blit...", screen.blit(text_render, (x, y)))
    return screen.blit(text_render, (x, y)) # this is a rect pygame.Rect


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

if(game):
    bg = pygame.transform.scale((pygame.image.load('images\Space_1.png')).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
else:
    bg= pygame.image.load("images\earth.png").convert()


# Create a custom event for adding a new enemy
ADDDEBRIS = pygame.USEREVENT + 1
pygame.time.set_timer(ADDDEBRIS, 500)
HIT = pygame.USEREVENT + 2
pygame.time.set_timer(HIT, 1000)

# Instantiate player. Right now, this is just a rectangle.
player = p.Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
debris1 = pygame.sprite.Group()
debris2 = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()


font_health = pygame.font.Font('freesansbold.ttf', 20)
text_health = font_health.render('Health: ' + str(health), True, (255, 255, 255))
textRect_health = text_health.get_rect()
textRect_health.center = (SCREEN_WIDTH - 100, SCREEN_HEIGHT - 80)

font_score = pygame.font.Font('freesansbold.ttf', 20)
text_score = font_score.render('Score: ' + str(score), True, (255, 255, 255))
textRect_score = text_score.get_rect()
textRect_score.center = (SCREEN_WIDTH - 100, SCREEN_HEIGHT - 50)

font_score_final = pygame.font.Font('freesansbold.ttf', 20)
text_score_final = font_score_final.render('Health: ' + str(health), True, (255, 255, 255))
textRect_score_final = text_score_final.get_rect()
textRect_score_final.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

font_over = pygame.font.Font('freesansbold.ttf', 20)
text_over = font_over.render('Health: ' + str(health), True, (255, 255, 255))
textRect_over = text_over.get_rect()
textRect_over.center = (SCREEN_WIDTH/2 -250, SCREEN_HEIGHT/2-100)


# Variable to keep the main loop running
running = True
game = False
window_width = 800
window_height = 600
size = (window_width, window_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Creating Sprite")

all_sprites_list = pygame.sprite.Group()

informations = pygame.sprite.Group()

info = Sprite(RED, 20, 30)
info.rect.x = 100
info.rect.y = 100
info.image = pygame.image.load("images\info.png")
all_sprites_list.add(info)
informations.add(info)

scotty = Sprite(RED, 20, 30)
scotty.rect.x = 400
scotty.rect.y = 300
scotty.image= pygame.image.load("images\scottyEarth.png")
all_sprites_list.add(scotty)

dialogue_box_width = 400
dialogue_box_height = 200
dialogue_box_x = (window_width - dialogue_box_width) // 2
dialogue_box_y = (window_height - dialogue_box_height) // 2

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if b1.collidepoint(pygame.mouse.get_pos()):  # checks a collision with a pygame.Rect and the mouse pos
                print("SLAYING")  # placeholder for new frame function
                all_sprites_list.remove(info)
                all_sprites_list.remove(scotty)
                all_sprites.add(player)
                game = True

        if(game):
            # Add a new enemy?
            if event.type == ADDDEBRIS:
                # Create the new enemy and add it to sprite groups
                new_debris1 = d1.Debris1()
                debris1.add(new_debris1)
                all_sprites.add(new_debris1)
                new_debris2 = d2.Debris2()
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

    # Fill the screen with black
    screen.fill((0, 0, 0))

    if (game):
        bg = pygame.transform.scale((pygame.image.load('images\Space_1.png')).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
    else:
        bg = pygame.image.load("images\earth.png").convert()

    screen.blit(bg, (0, 0))

    if(not game):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            scotty.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            scotty.moveRight(5)
        if keys[pygame.K_DOWN]:
            scotty.moveForward(8)
        if keys[pygame.K_UP]:
            scotty.moveBack(8)

        if pygame.sprite.spritecollideany(scotty, informations):
            font = pygame.font.SysFont('Arial', 25)
            pygame.display.set_caption('Box Test')
            screen.fill(GRAY)
            screen.blit(font.render('PLEASE save us from the space trash! Go!', True, (255, 0, 0)), (200, 100))
            b1 = button(screen, (400, 300), "Walk to the SKY!")
    else:
        # Update enemy position
        debris1.update()
        debris2.update()

        # Update the player sprite based on user keypresses
        player.update(pressed_keys)

        projectiles.update()



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
            screen.fill((0, 0, 0))
            text_end = font_over.render('You Died! This will be our future if we do not solve this issue!', True, (255, 255, 255))
            screen.blit(text_end, textRect_over)
            text_score_final = font_score_final.render('Score: ' + str(score), True, (255, 255, 255))
            screen.blit(text_score_final, textRect_score_final)
            #running = False

    all_sprites_list.update()
    all_sprites_list.draw(screen)

    # Update the display
    pygame.display.flip()

    # Ensure program maintains a rate of 60 frames per second
    clock.tick(60)