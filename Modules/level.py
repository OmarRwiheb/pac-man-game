import pygame


#defines the level class which inherits from pygame
class Level(pygame.sprite.Sprite):
    #constructor for the level class
    def __init__(self):
        super(Level, self).__init__()
        #size variable, contains the dimensions of the game window based on the dimensions of the map image
        self.size = [450, 500]
        
        #loads map image into the image variable
        self.image = pygame.image.load("Resources\\Level.png")
        
        #gets the rectangle (border) of the map
        self.rect = self.image.get_rect()

    def check_collision(self, obj):
        #compares the position of the player to the walls, returns true if they collide
        return pygame.sprite.collide_mask(self, obj)


