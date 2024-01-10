import pygame

# Classe pour representer le joueur
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.image = pygame.image.load("/home/mefathim/m07.davidcy/Pygame/Shooter/PygameAssets-main/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 300