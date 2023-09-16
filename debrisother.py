import random

import pygame

window_width = 800
window_height = 600

size = (window_width, window_height)
screen = pygame.display.set_mode(size)

#Object class

RED = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
WHITE = (255,255,255)
#INSIDE OF THE GAME LOOP

class Debris(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()

        self.image = pygame.Surface([width, height])

        pygame.draw.rect(self.image,
                        color,
                        pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()

    def movex(self, amount):
        self.rect.x += (amount)

    def movey(self, amount):
        self.rect.y += (amount)


pygame.init()

size = (window_width, window_height)
screen = pygame.display.set_mode(size)
background_image = pygame.image.load("images\Space_1.png").convert()
WIDTH = window_width
HEIGHT = window_height

pygame.display.set_caption("Creating Sprite")

all_sprites_list = pygame.sprite.Group()

randomx1 = []
randomy1 = []
number1 = random.randint(3,5)

for x in range(number1):
    randomx1.append(random.randint(-5,5))
    randomy1.append(random.randint(-5,5))
    if randomx1[x] == 0:
        randomx1[x] == 1
    if randomy1[x] == 0:
        randomy1[x] == 1

debris1 = []

for x in range(number1):
    debris1.append(Debris(RED, 20, 30))
    debris1[x].rect.x = (WIDTH-100)*random.random()
    debris1[x].rect.y = (HEIGHT-66)*random.random()
    debris1[x].image= pygame.image.load("images\debris1_1.png")
    all_sprites_list.add(debris1[x])

randomx2 = []
randomy2 = []
number2 = random.randint(3,5)

for x in range(number2):
    randomx2.append(random.randint(-5,5))
    randomy2.append(random.randint(-5,5))
    if randomx2[x] == 0:
        randomx2[x] == 1
    if randomy2[x] == 0:
        randomy2[x] == 1

debris2 = []

for x in range(number2):
    debris2.append(Debris(RED, 20, 30))
    debris2[x].rect.x = (WIDTH-100)*random.random()
    debris2[x].rect.y = (HEIGHT-100)*random.random()
    debris2[x].image= pygame.image.load("images\debris2_1.png")
    all_sprites_list.add(debris2[x])

exit = True
clock = pygame.time.Clock()

while exit:
    screen.fill((0, 0, 0))
    screen.blit(background_image, [0, 0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                exit = False

    keys = pygame.key.get_pressed()
    for x in range(number1):
        if pygame.time.get_ticks() % ((x+1) * 100) == 0:
            randomx1[x] = random.randint(-5,5)
            randomy1[x] = random.randint(-5,5)
            if randomx1[x] == 0:
                randomx1[x] == 1
            if randomy1[x] == 0:
                randomy1[x] == 1
    for x in range(number1):
        debris1[x].movex(randomx1[x])
        debris1[x].movey(randomy1[x])
        if debris1[x].rect.x < 0:
            #debris1[x].rect.x = 0
            print("hi1")
            print(x)
            print(randomx1[x])
            randomx1[x] = -randomx1[x]
            print(randomx1[x])
        if debris1[x].rect.y < 0:
            #debris1[x].rect.y = 0
            print("hi2")
            print(x)
            print(randomy1[x])
            randomy1[x] = -randomy1[x]
            print(randomy1[x])
        if debris1[x].rect.x > WIDTH-100:
            #debris1[x].rect.x = WIDTH-100
            print("hi3")
            print(x)
            print(randomx1[x])
            randomx1[x] = -randomx1[x]
            print(randomx1[x])
        if debris1[x].rect.y > HEIGHT-66:
            #debris1[x].rect.y = HEIGHT-66
            print("hi4")
            print(x)
            print(randomy1[x])
            randomy1[x] = -randomy1[x]
            print(randomy1[x])

    for x in range(number2):
        if pygame.time.get_ticks() % ((x+1) * 100) == 0:
            randomx2[x] = random.randint(-5,5)
            randomy2[x] = random.randint(-5,5)
            if randomx2[x] == 0:
                randomx2[x] == 1
            if randomy2[x] == 0:
                randomy2[x] == 1

    for x in range(number2):
        debris2[x].movex(randomx2[x])
        debris2[x].movey(randomy2[x])
        if debris2[x].rect.x < 0:
            #debris2[x].rect.x = 0
            print("hi5")
            print(x)
            randomx2[x] = -randomx2[x]
        if debris2[x].rect.y < 0:
            #debris2[x].rect.y = 0
            print("hi6")
            print(x)
            randomy2[x] = -randomy2[x]
        if debris2[x].rect.x > WIDTH-100:
            #debris2[x].rect.x = WIDTH-100
            print("hi7")
            print(x)
            randomx2[x] = -randomx2[x]
        if debris2[x].rect.y > HEIGHT-100:
            #debris2[x].rect.y = HEIGHT-100
            print("hi8")
            print(x)
            randomy2[x] = -randomy2[x]



    all_sprites_list.update()
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()