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

#b1 = button(screen, (400, 300), "Go To Space") # this is a pygame.Rect?

while exit:

    screen.fill((0,0,0))
    screen.blit(background_image, [0, 0])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                exit = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if b1.collidepoint(pygame.mouse.get_pos()):  # checks a collision with a pygame.Rect and the mouse pos
                print("SLAYING") #placeholder for new frame function
                screen.fill(RED)

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
        b1 = button(screen, (400, 300), "Walk to the SKY!")  # this is a pygame.Rect?


        # Add dialogue text and buttons here
    all_sprites_list.update()
    all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()