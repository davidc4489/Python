import pygame
from projectile import Projectile

pygame.init()

# Classe pour representer le joueur
class Ship(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 3
        self.max_health = 3
        self.velocity = 2
        self.image = pygame.image.load("ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500
        self.all_projectiles = pygame.sprite.Group()

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def launch_projectile(self):
        # Creer une nouvelle instance de la classe projectile
            self.all_projectiles.add(Projectile(self))