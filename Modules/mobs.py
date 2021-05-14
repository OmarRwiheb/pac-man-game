import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load("Resources\\Pac.png")
        self.rect = self.image.get_rect()
        self.speed = 3

        self.UPDATE = pygame.USEREVENT + 5
        pygame.time.set_timer(self.UPDATE, 70)

        self.current_direction = ""
        self.animation_index = 0
        self.animation_dict = {"u": ["Resources\\U1.png", "Resources\\Pac.png"], "d": ["Resources\\D1.png", "Resources\\Pac.png"], "l": ["Resources\\L1.png", "Resources\\Pac.png"], "r": ["Resources\\R1.png", "Resources\\Pac.png"]}

        self.rect.move_ip(10, 10)

    def move(self, direction, lvl):

        if direction == "u":

            self.rect.move_ip(0, -self.speed)
            if lvl.check_collision(self):

                while lvl.check_collision(self):
                    self.rect.move_ip(0, 1)

                self.rect.move_ip(0, 2)

            elif self.current_direction != "":
                self.update_animation()

            self.current_direction = "u"

        elif direction == "d":

            self.rect.move_ip(0, self.speed)
            if lvl.check_collision(self):

                while lvl.check_collision(self):
                    self.rect.move_ip(0, -1)

                self.rect.move_ip(0, -2)

            elif self.current_direction != "":
                self.update_animation()

            self.current_direction = "d"

        elif direction == "l":

            self.rect.move_ip(-self.speed, 0)

            if lvl.check_collision(self):

                while lvl.check_collision(self):
                    self.rect.move_ip(1, 0)

                self.rect.move_ip(2, 0)

            elif self.current_direction != "":
                self.update_animation()

            self.current_direction = "l"

        elif direction == "r":

            self.rect.move_ip(self.speed, 0)
            if lvl.check_collision(self):

                while lvl.check_collision(self):
                    self.rect.move_ip(-1, 0)

                self.rect.move_ip(-2, 0)

            elif self.current_direction != "":
                self.update_animation()

            self.current_direction = "r"

    def update_animation(self):

        self.image = pygame.image.load(self.animation_dict[self.current_direction][self.animation_index])

        if self.animation_index < 1:
            self.animation_index += 1

        else:
            self.animation_index = 0
