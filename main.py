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


pygame.init()


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

exit = True
clock = pygame.time.Clock()

background_image = pygame.image.load("images\earth.png").convert()

while exit:
    screen.fill((0,0,0))
    screen.blit(background_image, [0, 0])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                exit = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        scotty.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        scotty.moveRight(5)
    if keys[pygame.K_DOWN]:
        scotty.moveForward(5)
    if keys[pygame.K_UP]:
        scotty.moveBack(5)

    if pygame.sprite.spritecollideany(scotty, informations):
        font = pygame.font.SysFont('Arial', 25)
        pygame.display.set_caption('Box Test')
        screen.fill(GRAY)
        screen.blit(font.render('PLEASE save us from the space trash! Go!', True, (255, 0, 0)), (200, 100))

        # Add dialogue text and buttons here
    all_sprites_list.update()
    all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()