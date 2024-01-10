import pygame
pygame.init()

# Classe pour representer les aliens
class Alien(pygame.sprite.Sprite): 
    
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 2
        self.image = pygame.image.load("alien.bmp")
        self.image = pygame.transform.scale(self.image,(40,50))
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10
        self.velocity = 1

    def move(self):
        if self.rect.x + self.rect.width <= 1080:
         self.rect.x += self.velocity

    
        



        

