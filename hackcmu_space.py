import pygame
pygame.init()

screen_width = 500
screen_height = 500

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("First Game")

class player(object):
    def __init__(self,x,y,width, height,vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel

    def draw(self,win):
        pygame.draw.rect(win, self.color, (self.x,self.y, self.width, self.height))

class trash(object):
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 8

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y),self.radius)

run = True
collectible_trashes = []
harmful_trashes = []
projectiles = []
player1 = player(50, 50, 40, 60, 5)
space_pressed = False

while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #reset screen
    win.fill((0,0,0))

    #collectible_trash movement
    for c_trash in collectible_trashes:
        if c_trash.y < screen_height and c_trash.y > 0:
            c_trash.y += c_trash.vel     
            trash.draw(c_trash, win)
        else:
            collectible_trashes.pop(collectible_trashes.index(c_trash))

    #projectile movement
    for p in projectiles:
        if p.y < screen_height and p.y > 0:
            p.y += p.vel
            trash.draw(p, win)
        else:
            projectiles.pop(projectiles.index(p))

    #player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player1.x > player1.vel:
        player1.x -= player1.vel
    if keys[pygame.K_RIGHT] and player1.x < screen_width - player1.vel - player1.width:
        player1.x += player1.vel
    if keys[pygame.K_UP] and y > vel:
        player1.y -= player1.vel
    if keys[pygame.K_DOWN] and player1.y < screen_height - player1.vel - player1.height:
        player1.y += player1.vel

    #player spawns projectile
    if keys[pygame.K_SPACE] and space_pressed == False:
        proj_new = trash(player1.x+player1.width/2, player1.y+player1.height/2, 10, (0,255,0))
        projectiles.append(proj_new)
        space_pressed = True
    elif not keys[pygame.K_SPACE]:
        space_pressed = False

    #draw player
    pygame.draw.rect(win, (255,0,0), (player1.x, player1.y, player1.width, player1.height))
    pygame.display.update()

pygame.quit()