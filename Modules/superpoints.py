import pygame


#define the superpoint class
#each superpoint will spawn at the given (x,y)
class SuperPoint(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(SuperPoint, self).__init__()
        self.image = pygame.image.load("Resources\\super_point.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
