import pygame
from projectile import Projectile
import animation

class Player(animation.AnimateSprite):

    def __init__(self,game):
        super().__init__('player')
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 400

    def update_animation(self):
        self.animate()
    
    def damage(self,amount):
        self.health -= amount

        if self.health <= 0:
            self.game.game_over()
    
    def update_health_bar(self,surface):
        pygame.draw.rect(surface,(60,63,60),[self.rect.x + 50,self.rect.y + 20,self.max_health,7])
        pygame.draw.rect(surface,(111,210,46),[self.rect.x + 50,self.rect.y + 20,self.health,7])
    
    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))
        self.start_animation()
    
    def move_right(self):
        if not self.game.check_collision(self,self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity    