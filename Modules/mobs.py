import pygame

#defines the player (pacman) class
class Player(pygame.sprite.Sprite):
    #initializes pacman on game start
    def __init__(self):
        super(Player, self).__init__()
        #loads the pacman image into the image variable
        self.image = pygame.image.load("Resources\\Pac.png")
        
        #gets the rectangle (border) of the pac man image
        self.rect = self.image.get_rect()
        
        #how many pixels pacman moves per frame
        self.speed = 4

        #a custom pygame event (id=5) to update pacman
        self.UPDATE = pygame.USEREVENT + 5
        #fires the custom event to update pacman every 70 ms
        pygame.time.set_timer(self.UPDATE, 70)

        #starts with no direction
        self.current_direction = ""
        
        #pacman has two frames, closed mouth and open mouth, this variable is used to control which frame is being shown
        self.animation_index = 0
        
        #dictionary which contains all pacman frames in every movement direction
        self.animation_dict = {"u": ["Resources\\U1.png", "Resources\\Pac.png"], "d": ["Resources\\D1.png", "Resources\\Pac.png"], "l": ["Resources\\L1.png", "Resources\\Pac.png"], "r": ["Resources\\R1.png", "Resources\\Pac.png"]}

        #(0,0) is the upper left corner, on game start pacman is moved 10 units right and down so he doesn't get stuck in the wall
        self.rect.move_ip(10, 10)
        

    #defines the move function used to control pacman
    def move(self, direction, lvl):

        #4 blocks of code
        #each one corresponds to a direction
        
        #up direction
        if direction == "u":
            #moves pacman from his current position one step in the negative Y-axis 
            self.rect.move_ip(0, -self.speed)
            
            #checks if the new position collides with a wall
            if lvl.check_collision(self):
                #moves in the opposite direction until there is no longer collision 
                while lvl.check_collision(self):
                    self.rect.move_ip(0, 1)

                #moves pac 2 units away from the wall to prevent buggy behavior
                self.rect.move_ip(0, 2)

            elif self.current_direction != "":
                self.update_animation()

            self.current_direction = "u"

        #down direction
        elif direction == "d":

            self.rect.move_ip(0, self.speed)
            if lvl.check_collision(self):

                while lvl.check_collision(self):
                    self.rect.move_ip(0, -1)

                self.rect.move_ip(0, -2)

            elif self.current_direction != "":
                self.update_animation()

            self.current_direction = "d"

        #left direction
        elif direction == "l":

            self.rect.move_ip(-self.speed, 0)

            if lvl.check_collision(self):

                while lvl.check_collision(self):
                    self.rect.move_ip(1, 0)

                self.rect.move_ip(2, 0)

            elif self.current_direction != "":
                self.update_animation()

            self.current_direction = "l"

        #right direction
        elif direction == "r":

            self.rect.move_ip(self.speed, 0)
            if lvl.check_collision(self):

                while lvl.check_collision(self):
                    self.rect.move_ip(-1, 0)

                self.rect.move_ip(-2, 0)

            elif self.current_direction != "":
                self.update_animation()

            self.current_direction = "r"

    #function to update pac's animation 
    def update_animation(self):

        #from the dictionary containing all images, select the current direction and decide which frame to use based on the animation index
        self.image = pygame.image.load(self.animation_dict[self.current_direction][self.animation_index])

        #if pacman is on his zero frame, move into the first frame
        if self.animation_index ==0:
            self.animation_index = 1

        #if pacman is on his first frame, move back into the zero frame
        else:
            self.animation_index = 0
