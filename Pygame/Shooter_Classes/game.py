import pygame

from player import Player
from monster import Alien, Monster, Mummy
from comet_event import CometFallEvent

class Game:

    def __init__(self):

        # define if the game is beginning
        self.is_playing = False

        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.comet_event = CometFallEvent(self)
        self.pressed = {}
        self.clock = pygame.time.Clock()
        self.score = 0

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)
    
    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.comet_event.percent = 0
        self.player.health = self.player.max_health
        self.is_playing = False
    
    def update(self, screen):

        font = pygame.font.SysFont("Constantia", 30)
        score_text = font.render(f"Score: {self.score}", 1, (0,0,0))
        screen.blit(score_text, (20,20))

        screen.blit(self.player.image,self.player.rect)

        self.player.update_health_bar(screen)

        self.comet_event.update_bar(screen)

        self.player.update_animation()

        for projectile in self.player.all_projectiles:
            projectile.move()

        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        for comet in self.comet_event.all_comets:
            comet.fall()

        self.player.all_projectiles.draw(screen)

        self.all_monsters.draw(screen)

        self.comet_event.all_comets.draw(screen)

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        if self.pressed.get(pygame.K_LEFT) and self.player.rect.x > -40:
            self.player.move_left()
    
    def check_collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)
    
    def spawn_monster(self,monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))