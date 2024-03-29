import pygame
from pygame.sprite import Group
import random

from monster import Alien, Mummy

class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load('comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1,3)
        self.rect.x = random.randint(20,800)
        self.rect.y = - random.randint(0,800)
        self.comet_event = comet_event
    
    def remove(self):
        self.comet_event.all_comets.remove(self)

        if len(self.comet_event.all_comets) == 0:
            self.comet_event.percent = 0
            self.comet_event.game.spawn_monster(Mummy)
            self.comet_event.game.spawn_monster(Mummy)
            self.comet_event.game.spawn_monster(Alien)
    
    def fall(self):
        self.rect.y += random.randint(1,5)

        if self.rect.y >= 410:
            self.remove()

            if len(self.comet_event.all_comets) == 0:
                self.comet_event.percent = 0
                self.comet_event.fall_mode = False

        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            self.remove()
            self.comet_event.game.player.damage(20)
        