import pygame
from player import Player

pygame.init()

# Classe pour representer le jeu
class Game:

    def __init__(self):
        # charger nore joueur
        self.player = Player()