import pygame
from game import Game
from ship import Ship

pygame.init()

screen = pygame.display.set_mode((1080,720))

background = pygame.image.load("bg.jpg")

# charger le jeu
game = Game()

for i in range(11):
    for j in range (5):
        game.spawn_alien(i,j)

running = True

while running:

    # appliquer la fenetre de jeu
    screen.blit(background,(0,-200))

    # declencher les instructions de la partie
    game.update(screen)

    pygame.display.flip()

    for event in pygame.event.get():    # liste des evenements
        if event.type == pygame.QUIT:   # constante de la fermeture de la fenetre
            running = False
            pygame.quit()

    pygame.init()

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT] and game.ship.rect.x >= 0:
        game.ship.move_left()

    if pressed[pygame.K_RIGHT] and game.ship.rect.x + game.ship.rect.width<= screen.get_width():
        game.ship.move_right()

    if pressed[pygame.K_SPACE] and len(game.ship.all_projectiles) < 2:
        game.ship.launch_projectile()



        
            



