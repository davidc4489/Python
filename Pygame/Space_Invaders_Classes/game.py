import pygame
from spaceship import Spaceship
from aliens import Aliens

# Class for represent the game
class Game():

    def __init__(self):

        # define if the game is beginning:
        self.is_playing = False

        # define frames per second
        self.clock = pygame.time.Clock()
        self.fps = 60

        self.score = 0
        self.counter_end = 0

        self.screen = pygame.display.set_mode((600,600))
        pygame.display.set_caption('Space Invaders')

        self.font30 = pygame.font.SysFont('Constantia',30)
        self.font40 = pygame.font.SysFont('Constantia',40)
        self.font_score = pygame.font.Font('Yatra.ttf',30)

        # define game variables
        self.rows = 5
        self.cols = 5
        self.alien_cooldown = 1000 # in milliseconds
        self.last_alien_shot = pygame.time.get_ticks()
        self.countdown = 3
        self.last_count = pygame.time.get_ticks()

        self.red = (255,0,0)
        self.green = (0,255,0)
        self.white = (255,255,255)

        self.bg = pygame.image.load('bg.png')

        self.spaceship_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.alien_group = pygame.sprite.Group()
        self.alien_bullet_group = pygame.sprite.Group()
        self.spaceship = Spaceship(300,540,3,self)
        self.spaceship_group.add(self.spaceship)
        self.explosion_group = pygame.sprite.Group()

        self.velocity_alien = 1
        self.level = 1
        self.dead = False

    
    def start(self):
         self.is_playing = True
         self.level = 0
         if len(self.alien_group) == 0:
            self.create_alien()
         for alien in self.alien_group:
          alien.velocity = 1
         if len(self.spaceship_group) == 0:
            self.spaceship = Spaceship(300,540,3,self)
            self.spaceship_group.add(self.spaceship)
    
    def game_over(self):
         
         for alien in self.alien_group:
              alien.kill()
         for bullet in self.alien_bullet_group:
              bullet.kill()
         self.is_playing = False
         self.alien_group = pygame.sprite.Group()
         self.spaceship.kill()
         
         self.score = 0
    
    def draw_bg(self):
        self.screen.blit(self.bg,(0,0))

    def draw_text(self,text,font,text_col, x,y):
        img = font.render(text,True,text_col)
        self.screen.blit(img,(x,y))

    def create_alien(self): 
        #create aliens
        for row in range(self.rows):
            for item in range(self.cols):
                alien = Aliens(100 + item * 100, 100 + row * 50,self.spaceship,self.velocity_alien)
                self.alien_group.add(alien)

    def update(self):
        if self.countdown > 0: # before starting game
            self.draw_text('GET READY!!!',self.font40,self.white,190,350)
            self.draw_text(str(self.countdown),self.font40,self.white,290,400)
            count_timer = pygame.time.get_ticks()
            if count_timer - self.last_count > 1000:
                self.countdown -= 1
                self.last_count = count_timer
        
        if len(self.alien_group) == 0 and self.counter_end < 200: # if the player wins
                self.counter_end += 1
                self.draw_text('CONGRATULATIONS!!!',self.font40,self.white,130,250)
        if len(self.alien_group) == 0 and self.spaceship.health_remaining != 0 and self.counter_end >= 200 and self.counter_end < 400:
                    self.counter_end += 1
                    if self.counter_end < 250 or self.counter_end > 300 or self.counter_end > 350:
                        self.draw_text(f'LEVEL {self.level+1}',self.font40,self.red,250,250)
                    else:
                        self.draw_text(f'LEVEL {self.level+1}',self.font40,self.white,250,250)
        if len(self.alien_group) == 0 and self.spaceship.health_remaining != 0 and self.counter_end >= 400:
                    self.velocity_alien += 1
                    self.create_alien()
                    self.counter_end = 0
                    self.level += 1

        #if self.spaceship.health_remaining == 0: # if the player loses
            #self.draw_text('GAME OVER', self.font40, self.white, 190, 350)

        self.explosion_group.update()
        
        # update sprite groups
        self.spaceship_group.draw(self.screen)
        self.bullet_group.draw(self.screen)
        self.alien_group.draw(self.screen)
        self.alien_bullet_group.draw(self.screen)
        self.explosion_group.draw(self.screen)

