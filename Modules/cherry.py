import pygame
#define the cherry class
#each cherry will spawn at the given (x,y)
class Cherry():
    def __init__(self, x, y):
        self.image=pygame.image.load("Resources\\cherry.png")
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y