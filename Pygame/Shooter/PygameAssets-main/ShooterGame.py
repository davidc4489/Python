import pygame
from game import Game

pygame.init()

pygame.display.set_caption("Comet Fall Game")
screen = pygame.display.set_mode((1080,720))

background = pygame.image.load("/home/mefathim/m07.davidcy/Pygame/Shooter/PygameAssets-main/bg.jpg")

# charger le jeu
game = Game()

running = True

while running:

    # appliquer la fenetre de jeu
    screen.blit(background,(0,-200))

    # appliquer l'image du joueur
    screen.blit(game.player.image,game.player.rect)

    pygame.display.flip()

    for event in pygame.event.get():    # liste des evenements
        if event.type == pygame.QUIT:   # constante de la fermeture de la fenetre
            running = False
            pygame.quit()

pygame.quit()   # Desinitialisation des elements de pygame