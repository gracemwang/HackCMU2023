import pygame

COLOR =(255,100,98)
SURFACE_COLOR=(167, 255,100)

WIDTH = 1000
HEIGHT = 700

#Object class

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)

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


pygame.init()

RED = (255, 0, 0)

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Creating Sprite")

all_sprites_list = pygame.sprite.Group()

scotty = Sprite(RED, 20, 30)
scotty.rect.x = 100
scotty.rect.y = 100
scotty.image= pygame.image.load("images\scotty.png")
all_sprites_list.add(scotty)

exit = True
clock = pygame.time.Clock()

while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                exit = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        scotty.moveLeft(10)
    if keys[pygame.K_RIGHT]:
        scotty.moveRight(10)
    if keys[pygame.K_DOWN]:
        scotty.moveForward(10)
    if keys[pygame.K_UP]:
        scotty.moveBack(10)

    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()