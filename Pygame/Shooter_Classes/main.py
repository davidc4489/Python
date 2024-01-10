import pygame
from game import Game

pygame.init()

pygame.display.set_caption("Comete Fall Game")
screen = pygame.display.set_mode((1080,600))

background = pygame.image.load('bg.jpg')

banner = pygame.transform.scale(pygame.image.load('banner.png'),(500,500))
play_button = pygame.image.load('button.png')
play_button = pygame.transform.scale(play_button,(500,200))
play_button_rect = play_button.get_rect()
play_button_rect.x = int(screen.get_width()/3.5)
play_button_rect.y = int(screen.get_height()/1.7)

game = Game()

running = True

while running:

    game.clock.tick(60)

    screen.blit(background,(0,-300))

    # verify if the game is beginning
    if game.is_playing == True:
        game.update(screen)
    else:
        screen.blit(banner, (300,-50))
        screen.blit(play_button,(int(screen.get_width()/3.5),int(screen.get_height()/1.7)))

    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()


