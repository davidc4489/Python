import pygame
from pygame.sprite import Group
import random
import animation

class Monster(animation.AnimateSprite):

    def __init__(self,game,name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100 
        self.max_health = 100
        self.attack = 5
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0,300)
        self.rect.y = 438 - offset
        self.start_animation()
        self.loot_amount = 10

    def set_speed(self,speed):
        self.default_speed = speed
        self.velocity = random.randint(1,self.default_speed)
    
    def set_loot_amount(self, amount):
        self.loot_amount = amount
    
    def add_score(self, points):
        self.game.score += points
    
    def damage(self,amount):
        self.health -= amount

        if self.health <= 0:
            self.rect.x = 1000 + random.randint(0,300)
            self.velocity = random.randint(1,3)
            self.health = self.max_health
            self.add_score(self.loot_amount)

            if self.game.comet_event.is_full_loaded():
                self.game.all_monsters.remove(self)

                self.game.comet_event.attempt_fall()
    
    def update_animation(self):
        self.animate(loop=True)
    
    def update_health_bar(self,surface):
        bar_color = (111,210,46)
        back_bar_color = (60,63,60)
        bar_position = [self.rect.x + 10,self.rect.y - 20,self.health,5]
        back_bar_position = [self.rect.x + 10,self.rect.y - 20,self.max_health,5]
        pygame.draw.rect(surface,back_bar_color,back_bar_position)
        pygame.draw.rect(surface,bar_color,bar_position)
    
    def forward(self):
        if not self.game.check_collision(self,self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)

class Mummy(Monster):

    def __init__(self,game):
        super().__init__(game,'mummy',(130,130))
        self.set_speed(3)

class Alien(Monster):

    def __init__(self, game):
        super().__init__(game,'alien',(300,300),150)
        self.health = 200
        self.max_health = 200
        self.set_speed(1)
        self.loot_amount = 20