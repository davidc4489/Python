import pygame
from pygame.locals import *
from pygame.sprite import Group

# define frames per second
clock = pygame.time.Clock()
fps = 60

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Space Invaders')

# define game variables
rows = 5
cols = 5
alien_cooldown = 1000 # in milliseconds
last_alien_shot = pygame.time.get_ticks()

red = (255,0,0)
green = (0,255,0)

bg = pygame.image.load('bg.png')

def draw_bg():
    screen.blit(bg,(0,0))

class Spaceship(pygame.sprite.Sprite):

    def __init__(self,x,y,health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('spaceship.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.health_start = health
        self.health_remaining = health
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        speed = 8

        cooldown = 500 # milliseconds

        # get key pressed
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed

        if key[pygame.K_RIGHT] and self.rect.right < 600:
            self.rect.x += speed

        # record current time
        time_now = pygame.time.get_ticks()

        if key[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
            bullet = Bullets(self.rect.centerx,self.rect.top)
            bullet_group.add(bullet)
            self.last_shot = time_now

        # create a mask
        self.mask = pygame.mask.from_surface(self.image)

        # draw health bar
        pygame.draw.rect(screen,red,(self.rect.x,(self.rect.bottom+10),self.rect.width,15))
        if self.health_remaining > 0:
            pygame.draw.rect(screen,green,(self.rect.x,(self.rect.bottom+10),int(self.rect.width*(self.health_remaining/self.health_start)),15))

import random

class Bullets(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bullet.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    def update(self):
        self.rect.y -= 5

        if self.rect.bottom < 0:
            self.kill()

        if pygame.sprite.spritecollide(self,alien_group,True):
            self.kill()

class Aliens(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('alien' + str(random.randint(1,5)) + '.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.move_counter = 0
        self.move_direction = 1

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 75:
            self.move_direction *= -1
            self.move_counter *= self.move_direction

import random

class Alien_Bullets(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('alien_bullet.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    def update(self):
        self.rect.y += 2

        if self.rect.top > 600:
            self.kill()

        if pygame.sprite.spritecollide(self,spaceship_group,False,pygame.sprite.collide_mask):
            self.kill()
            spaceship.health_remaining -= 1

# create sprite group
spaceship_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()
alien_bullet_group = pygame.sprite.Group()

# create player
spaceship = Spaceship(300,540,3)
spaceship_group.add(spaceship)

#create aliens
def create_alien():
    for row in range(rows):
        for item in range(cols):
            alien = Aliens(100 + item * 100, 100 + row * 50)
            alien_group.add(alien)

create_alien()

run = True

while run:

    clock.tick(fps)
    
    # draw background
    draw_bg()

    # create random alien_bullet
    # record current time
    time_now = pygame.time.get_ticks()
    # shoot
    if time_now - last_alien_shot > alien_cooldown and len(alien_bullet_group) < 5 and len(alien_group) > 0:
        attacking_alien = random.choice(alien_group.sprites())
        alien_bullet = Alien_Bullets(attacking_alien.rect.centerx, attacking_alien.rect.bottom)
        alien_bullet_group.add(alien_bullet)
        last_alien_shot = time_now 
    
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update spaceship
    spaceship.update()
    bullet_group.update()
    alien_group.update()
    alien_bullet_group.update()
    
    # update sprite group
    spaceship_group.draw(screen)
    bullet_group.draw(screen)
    alien_group.draw(screen)
    alien_bullet_group.draw(screen)
    
    pygame.display.update()

pygame.quit()