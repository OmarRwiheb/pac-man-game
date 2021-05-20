import pygame


# define the points class
import pygame.sprite


class Point(pygame.sprite.Sprite):
    #each point is drawn at it's given (x,y)
    def __init__(self, x, y):
        super(Point, self).__init__()
        self.image = pygame.image.load("Resources\\Point.png")
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

#function to return a list of points locations
def draw_points():

    # a sprite group that will be filled with all the point() objects
    points_group = pygame.sprite.Group()
    # points_left variable is used to count the points number
    points_left = 0

    # populates the rows of the map with points
    for i in range(0, 26):

        # Row 1
        if i not in [0, 12, 13]:
            points_group.add(Point(21 + i * 16, 23))
            points_left += 1

        # Row 2
        points_group.add(Point(21 + i * 16, 85))
        points_left += 1

        # Row 3
        if i not in [6, 7, 12, 13, 18, 19]:
            points_group.add(Point(21 + i * 16, 133))
            points_left += 1

        # Row 4
        if i not in [0, 12, 13, 25]:
            points_group.add(Point(21 + i * 16, 325))
            points_left += 1

        # Row 5
        if i not in [3, 4, 21, 22]:
            points_group.add(Point(21 + i * 16, 374))
            points_left += 1

        # Row 6
        if i not in [6, 7, 12, 13, 18, 19]:
            points_group.add(Point(21 + i * 16, 421))
            points_left += 1

        # Row 7
        points_group.add(Point(21 + i * 16, 470))
        points_left += 1

    # populates the columns of the map with points
    for i in range(0, 28):

        # Column 1 and 10
        if i not in [0, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 22, 23, 24, 25]:
            points_group.add(Point(21, 21 + i * 16))
            points_group.add(Point(421, 21 + i * 16))
            points_left += 2

        # Column 2 and 9
        if i in [23, 24]:
            points_group.add(Point(53, 21 + i * 16))
            points_group.add(Point(389, 21 + i * 16))
            points_left += 2

        # Column 3 and 8
        if i not in [0, 4, 7, 19, 22, 25, 26, 27]:
            points_group.add(Point(101, 21 + i * 16))
            points_group.add(Point(341, 21 + i * 16))
            points_left += 2

        # Column 4 and 7
        if i in [5, 6, 23, 24]:
            points_group.add(Point(149, 21 + i * 16))
            points_group.add(Point(293, 21 + i * 16))
            points_left += 2

        # Column 5 and 6
        if i in [1, 2, 3, 20, 21, 26, 27]:
            points_group.add(Point(197, 21 + i * 16))
            points_group.add(Point(245, 21 + i * 16))
            points_left += 2

    return [points_group, points_left]
