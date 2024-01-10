import pygame
import random
from explosion import Explosion

# Class for represent an alien
class Aliens(pygame.sprite.Sprite):

    def __init__(self,x,y,player,velocity):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.transform.scale(pygame.image.load('reb.jpeg'),(50,50))
        self.type = random.randint(1,5)
        self.image = pygame.image.load('alien' + str(self.type) + '.png')
        # self.image = pygame.image.load('alien' + str(random.randint(1,5)) + '.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.move_counter = 0       # counter for the movements of the alien
        self.move_direction = 1     # positive direction : to the right
        self.player = player
        self.loot_amount = self.type * 10
        self.velocity = velocity
    
    def move(self):
        #for alien in self.player.game.alien_group:
        self.rect.x += self.move_direction * self.velocity
        if self.rect.x < 0:
            for alien in self.player.game.alien_group:
                alien.move_direction *= -1  # negative direction : to the left
                alien.rect.y += 10
        if self.rect.x > 580: # take down all the aliens
            for alien in self.player.game.alien_group:
                alien.move_direction *= -1  # negative direction : to the left
                alien.rect.y += 10

    def checkCollision(self):
        # check collision between an alien and a spaceship and delete both
        if pygame.sprite.spritecollide(self,self.player.game.spaceship_group,True):
            self.kill()
            explosion = Explosion(self.rect.centerx,self.rect.centery,3,self.player.game)
            self.player.game.explosion_group.add(explosion)
            explosion_fx = pygame.mixer.Sound("explosion.wav")
            explosion_fx.play()

        if pygame.sprite.spritecollide(self,self.player.game.bullet_group,True):
            self.kill()
            explosion = Explosion(self.rect.centerx,self.rect.centery,2,self.player.game)
            self.player.game.explosion_group.add(explosion)
            explosion_fx = pygame.mixer.Sound("explosion.wav")
            explosion_fx.play()
            self.player.game.score += self.loot_amount
    
    def update(self):
        self.move()
        self.checkCollision()




