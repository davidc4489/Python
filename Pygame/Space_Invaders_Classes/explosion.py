import pygame

# Class for represent the explosion animation
class Explosion(pygame.sprite.Sprite):

    def __init__(self,x,y,size,game):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1,6):
            img = pygame.image.load(f"exp{num}.png")
            if size == 1:
                img = pygame.transform.scale(img,(20,20))
            if size == 2:
                img = pygame.transform.scale(img,(40,40))
            if size == 3:
                img = pygame.transform.scale(img,(160,160))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.counter = 0
        self.game = game

    def update(self):
        explosion_speed = 3
        # update explosion animation
        self.counter += 1

        if self.counter >= explosion_speed and self.index < len(self.images)-1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        # if the animation is complete, delete explosion
        if self.index >= len(self.images) -1 and self.counter >= explosion_speed:
            self.kill()
            if self.game.spaceship.health_remaining <= 0:
                self.game.game_over()