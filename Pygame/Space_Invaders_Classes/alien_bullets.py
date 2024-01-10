import pygame
from explosion import Explosion

# Class for represent alien bullets
class Alien_Bullets(pygame.sprite.Sprite):

    def __init__(self,x,y,game):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('alien_bullet.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.game = game

    def move(self):
        self.rect.y += 2

        if self.rect.top > 600: # remove the bullet if it came out of the screen
            self.kill()

    def checkCollision(self):
        # check collision between alien bullet and a spaceship and delete a bullet
        if pygame.sprite.spritecollide(self,self.game.spaceship_group,False,pygame.sprite.collide_mask):
            self.kill()
            self.game.spaceship.health_remaining -= 1 # update the spaceship health
            explosion_fx = pygame.mixer.Sound("explosion.wav")
            explosion_fx.play()
            explosion = Explosion(self.rect.centerx,self.rect.centery,2,self.game)
            self.game.explosion_group.add(explosion)


    def update(self): # shoot down
        self.move()
        self.checkCollision()


