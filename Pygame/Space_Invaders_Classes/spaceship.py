import pygame
from bullets import Bullets
from explosion import Explosion
from pygame import mixer
pygame.mixer.pre_init(44100,-16,2,512)
mixer.init()


class Spaceship(pygame.sprite.Sprite):

    def __init__(self,x,y,health,game):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('spaceship.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.health_start = health
        self.health_remaining = health
        self.last_shot = pygame.time.get_ticks()
        self.game = game

    def health_bar(self):
        # draw health bar
        pygame.draw.rect(self.game.screen,self.game.red,(self.rect.x,(self.rect.bottom+10),self.rect.width,15))
        if self.health_remaining > 0:
            pygame.draw.rect(self.game.screen,self.game.green,(self.rect.x,(self.rect.bottom+10),int(self.rect.width*(self.health_remaining/self.health_start)),15))

    def game_over(self):
        explosion2_fx = pygame.mixer.Sound("explosion2.wav")
        explosion2_fx.play()
        explosion = Explosion(self.rect.centerx,self.rect.centery,3,self.game)
        self.game.explosion_group.add(explosion)
        self.kill()
        self.game.draw_text('GAME OVER',self.game.font40,self.game.white,190,350)

    def launch_projectile(self):
        # record current time
        time_now = pygame.time.get_ticks()
        cooldown = 500
        if time_now - self.last_shot > cooldown:

            laser_fx = pygame.mixer.Sound("laser.wav")
            laser_fx.play()
            bullet = Bullets(self.rect.centerx,self.rect.top,self)
            self.game.bullet_group.add(bullet)
            self.last_shot = time_now

    def move(self):
        speed = 8
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed

        if key[pygame.K_RIGHT] and self.rect.right < 600:
            self.rect.x += speed       

    
    def update(self):

        self.move()
        # get key pressed
        
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.launch_projectile()

        # create a mask
        self.mask = pygame.mask.from_surface(self.image)
        
        if self.health_remaining <= 0:
            self.game_over()

        # draw health bar
        self.health_bar()

