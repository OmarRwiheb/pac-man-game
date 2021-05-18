from Modules.PacMan import Player
import pygame

class ghost(Player):
    def __init__(self, x, y):
        self.image = pygame.image.load("Resources\\red_ghost.png")
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
