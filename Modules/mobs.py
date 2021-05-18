import pygame


# defines the player (pacman) class
class Player(pygame.sprite.Sprite):

    # initializes pacman on game start
    def __init__(self):
        super(Player, self).__init__()
        # loads the pacman image into the image variable
        self.image = pygame.image.load("Resources\\Pac.png")

        # gets the rectangle (border) of the pac man image
        self.rect = self.image.get_rect()

        # how many pixels pacman moves per frame
        self.speed = 6

        # a custom pygame event (id=5) to update pacman
        self.UPDATE = pygame.USEREVENT + 5
        # fires the custom event to update pacman every 70 ms
        pygame.time.set_timer(self.UPDATE, 70)

        # starts with no direction
        self.current_direction = ""

        # pacman has two frames, closed mouth and open mouth, this variable is used to control which frame is being shown
        self.animation_index = 0

        # dictionary which contains all pacman frames in every movement direction
        self.animation_dict = {"u": ["Resources\\U1.png", "Resources\\Pac.png"],
                               "d": ["Resources\\D1.png", "Resources\\Pac.png"],
                               "l": ["Resources\\L1.png", "Resources\\Pac.png"],
                               "r": ["Resources\\R1.png", "Resources\\Pac.png"]}

        # (0,0) is the upper left corner, on game start pacman is moved 10 units right and down so he doesn't get stuck in the wall
        self.rect.move_ip(9, 9)

    # defines the move function used to control pacman
    def move(self, direction, lvl):

        # checks if pacman entered any of the two portals
        self.check_portal()

        # 4 blocks of code
        # each one corresponds to a direction
        # up direction
        if direction == "u":
            self.rect.move_ip(0, -self.speed)
            self.current_direction = direction

        # down direction
        elif direction == "d":
            self.rect.move_ip(0, self.speed)
            self.current_direction = direction

        # left direction
        elif direction == "l":
            self.rect.move_ip(-self.speed, 0)
            self.current_direction = direction

        # right direction
        elif direction == "r":

            self.rect.move_ip(self.speed, 0)
            self.current_direction = direction

        self.update_animation(lvl)
        self.reposition(lvl)

    # function to update pac's animation
    def update_animation(self, lvl):

        if not lvl.check_collision(self):
            # from the dictionary containing all images, select the current direction and decide which frame to use based on the animation index
            self.image = pygame.image.load(self.animation_dict[self.current_direction][self.animation_index])

            # if pacman is on his zero frame, move into the first frame
            if self.animation_index == 0:
                self.animation_index = 1

            # if pacman is on his first frame, move back into the zero frame
            else:
                self.animation_index = 0

    def check_portal(self):

        # checks if pacman moved in the left portal
        if self.rect.x < -30:
            self.rect.x = 440
            self.rect.y = 219

        # checks if pacman moved in the right portal
        elif self.rect.x > 460:
            self.rect.x = -20
            self.rect.y = 219

    def reposition(self, lvl):

        # mackes sure to set a constant distance between pacman and any other wall
        d = 2

        if self.current_direction == "u":
            self.rect.move_ip(0, -d)
            if not lvl.check_collision(self):
                self.rect.move_ip(0, d)

            else:

                while lvl.check_collision(self):
                    self.rect.move_ip(0, 1)

                self.rect.move_ip(0, d)

        elif self.current_direction == "d":
            self.rect.move_ip(0, d)
            if not lvl.check_collision(self):
                self.rect.move_ip(0, -d)

            else:

                while lvl.check_collision(self):
                    self.rect.move_ip(0, -1)

                self.rect.move_ip(0, -d)

        elif self.current_direction == "l":
            self.rect.move_ip(-d, 0)
            if not lvl.check_collision(self):
                self.rect.move_ip(d, 0)

            else:

                while lvl.check_collision(self):
                    self.rect.move_ip(1, 0)

                self.rect.move_ip(d, 0)

        elif self.current_direction == "r":
            self.rect.move_ip(d, 0)
            if not lvl.check_collision(self):
                self.rect.move_ip(-d, 0)

            else:

                while lvl.check_collision(self):
                    self.rect.move_ip(-1, 0)

                self.rect.move_ip(-d, 0)
