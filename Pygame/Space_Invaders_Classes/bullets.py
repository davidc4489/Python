import pygame
from aliens import Aliens
from explosion import Explosion

# Class for represent bullet
class Bullets(pygame.sprite.Sprite):

    def __init__(self,x,y,player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bullet.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.player = player

    def update(self):
        self.rect.y -= 5

        if self.rect.bottom < 0: # remove the bullet if it came out of the screen
            self.kill()


            