import pygame

pygame.init()

pygame.display.set_mode((400,400))

running = True

while running:
    for event in pygame.event.get():    # liste des evenements
        if event.type == pygame.QUIT:   # constante de la fermeture de la fenetre
            running = False

pygame.quit()   # Desinitialisation des elements de pygame