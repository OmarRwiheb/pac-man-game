from Modules.PacMan import Player
import pygame
import random

# defines the ghost class, which inherits from the player class


class ghost(Player):
    # each ghost will spawn at the (x,y) passed to it
    def __init__(self, x, y):
        # load image
        self.Color="red"
        self.image = pygame.image.load("Resources\\red_ghost.png")
        # get image borders
        self.rect = self.image.get_rect()
        # controls the ghost's speed
        self.speed = 4
        # the next 2 lines tell pygame where to begin drawing the ghosts
        self.rect.x = x
        self.rect.y = y
        # list of directions each ghost may take
        self.ghost_directions = ["u", "d", "l", "r"]
        # direction is given an initial value to prevent bugs, doesn't have to be 'up'
        self.direction = "u"
        # a custom event with the number 30
        # ----this number may not be changed----
        self.CHANGE_GHOST_DIRECTION = pygame.event.Event(30)
        # each ghost separately changes directions every 1 second, can be changed
        pygame.time.set_timer(self.CHANGE_GHOST_DIRECTION,
                              random.randint(15, 30)*100)

    #function to change ghost colors when pac eats a cherry or runs out of strength
    def UpdateColor(self,x):
        if not x>0:
            self.image = pygame.image.load("Resources\\red_ghost.png")
        else:
            self.image = pygame.image.load("Resources\\weak_ghost.png")
    
    # function to change directions, chooses randomly between the 0-3 index
    def changeDirection(self):
        self.direction = self.ghost_directions[random.randint(0, 3)]

    # move function, inherited from pacman class and overridden
    def move(self,  lvl):
        # 4 blocks of code
        # each one corresponds to a direction

        # up direction
        if self.direction == "u":
            self.rect.move_ip(0, -self.speed)

        # down direction
        elif self.direction == "d":
            self.rect.move_ip(0, self.speed)

        # left direction
        elif self.direction == "l":
            self.rect.move_ip(-self.speed, 0)

        # right direction
        elif self.direction == "r":
            self.rect.move_ip(self.speed, 0)

        # every time a ghost moves, check if it's at a portal, update it's movement direction, and reposition away from walls
        # these functions are inherited from the pacman class
        self.check_portal()
        self.current_direction = self.direction
        self.reposition(lvl)
