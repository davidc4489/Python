import pygame
from ship import Ship
from aliens import Alien

pygame.init()

# Classe pour representer le jeu
class Game():

    def __init__(self):
        self.ship = Ship(self)
        self.pressed = {}
        # groupe d'aliens
        self.all_aliens = pygame.sprite.Group()

    def spawn_alien(self,i,j):
        alien = Alien(self)
        alien.rect.x = alien.rect.x + (i*60)
        alien.rect.y = alien.rect.y + (j*40)
        self.all_aliens.add(alien)
        
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, True, pygame.sprite.collide_mask)
    
    def update(self, screen):
        # appliquer l'image du joueur
        screen.blit(self.ship.image,self.ship.rect)

        # recuperer les projectiles d'un joueur
        for projectile in self.ship.all_projectiles:
            projectile.move()

        for alien in self.all_aliens:
            alien.move()

        # appliquer l'image du projectile du joueur
        self.ship.all_projectiles.draw(screen)

        # appliquer l'image de l'ensemble des monstres
        self.all_aliens.draw(screen) 

