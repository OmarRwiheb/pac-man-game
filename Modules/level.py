import pygame


class Level(pygame.sprite.Sprite):

    def __init__(self):
        super(Level, self).__init__()
        self.size = [450, 500]
        self.image = pygame.image.load("Resources\\Level.png")
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def check_collision(self, obj):

        return pygame.sprite.collide_mask(obj, self)