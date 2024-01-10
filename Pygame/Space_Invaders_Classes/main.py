import pygame
from pygame.locals import *
from pygame.sprite import Group
from alien_bullets import Alien_Bullets
import random
from game import Game
from pygame import mixer
from spaceship import Spaceship

pygame.init()

game = Game()

banner = pygame.transform.scale(pygame.image.load('Space_Invaders_Logo.png'),(500,500))
banner = pygame.transform.scale(banner,(400,200))
play_button = pygame.image.load('button.png')
play_button = pygame.transform.scale(play_button,(200,100))
play_button_rect = play_button.get_rect()
play_button_rect.x = int(game.screen.get_width()/3.5)
play_button_rect.y = int(game.screen.get_height()/1.7)

# game.create_alien()
    
run = True

starting_music = pygame.mixer.Sound("x-files.wav")
    
while run:

        game.clock.tick(game.fps)
        
        # draw background
        game.draw_bg()
        if game.is_playing == False:
            game.screen.blit(pygame.image.load('alien1.png'),(50,450))
            game.screen.blit(pygame.image.load('alien2.png'),(50,510))
            game.screen.blit(pygame.image.load('alien3.png'),(50,560))
            game.screen.blit(pygame.image.load('alien4.png'),(350,450))
            game.screen.blit(pygame.image.load('alien5.png'),(350,510))
            game.draw_text(': 10',game.font40,game.white,120,450)
            game.draw_text(': 20',game.font40,game.white,120,510)
            game.draw_text(': 30',game.font40,game.white,120,560)
            game.draw_text(': 40',game.font40,game.white,420,450)
            game.draw_text(': 50',game.font40,game.white,420,510)

        if game.is_playing == False:
            starting_music.play()
        else:
            starting_music.stop()

        if game.is_playing == True:
            game.update()
        else:
            game.screen.blit(banner, (100,100))
            game.screen.blit(play_button,(int(game.screen.get_width()/3),int(game.screen.get_height()/1.7)))

        if game.countdown == 0: # start the game


            # font = pygame.font.SysFont("microsofthimalaya", 30)
            score_text = game.font_score.render(f"Score: {game.score}", 1, (255,255,255))
            game.screen.blit(score_text, (20,20))

            # create random alien_bullet
            # record current time
            time_now = pygame.time.get_ticks()
            # shoot from a random alien every second
            if time_now - game.last_alien_shot > game.alien_cooldown and len(game.alien_bullet_group) < 5 and len(game.alien_group) > 0:
                attacking_alien = random.choice(game.alien_group.sprites())
                alien_bullet = Alien_Bullets(attacking_alien.rect.centerx, attacking_alien.rect.bottom,game)
                game.alien_bullet_group.add(alien_bullet)
                last_alien_shot = time_now 
        
            # update spaceship
            game.spaceship_group.update()
            game.bullet_group.update()
            game.alien_group.update()
            game.alien_bullet_group.update()

        if game.dead == True:
            if game.spaceship.health_remaining <= 0:
                game.counter_end += 1
                game.draw_text('GAME OVER', game.font40, game.white, 190, 350)
                game.is_playing = False
                game.game_over()

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                 # game.is_playing = True
                 game.start()

        
        pygame.display.update()

pygame.quit()