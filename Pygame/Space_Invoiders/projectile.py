import pygame

# Classe pour representer le projectile du joueur
class Projectile(pygame.sprite.Sprite):

    def __init__(self,ship):
        super().__init__()
        self.velocity = 2
        self.ship = ship
        self.image = pygame.image.load("projectile.png")
        self.image = pygame.transform.scale(self.image,(20,20))
        self.rect = self.image.get_rect()
        self.rect.x = ship.rect.x + 20
        self.rect.y = ship.rect.y - 20
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
    
    def move(self):
        self.rect.y -= self.velocity
        self.rotate()

        if pygame.sprite.spritecollide(self,self.ship.game.all_aliens,True):
            self.kill()

        # verifier si le projectile est sorti de l'ecran
        if self.rect.y < 0:
            # supprimer le projectile
            self.remove()