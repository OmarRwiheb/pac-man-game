import pygame, math
import numpy as np
from Modules.map import Map
from Modules.PacMan import Player
from Modules.point import Point
from Modules.ghosts import ghost

# initializes some standard pygame classes
pygame.init()

# change game icon and name
pygame.display.set_caption("PAC-MAN")
icon = pygame.image.load("Resources\\icon.png")
pygame.display.set_icon(icon)

# makes a level and player instance
map = Map()
player = Player()

# a list containing all instances of the ghosts, maximum is 4 without lag
ghost_list = [ghost(410, 460), ghost(10, 460), ghost(
    410, 10)]

# adds all sprites to the variable game_group
game_group = pygame.sprite.Group()
game_group.add(map, player)

# sets the window size to the size specified in the level object(dimensions of the map image)
screen_size = map.size
screen = pygame.display.set_mode(screen_size)

# a empty list that will be filled with all the point() objects
points = []

# boolean 2d array to store points location
# so any location on the map that contain a point we will make it = True in the 2d array
points_location = np.zeros((map.size), dtype=bool)

# points_left variable is used to count the points number
points_left = 0

# populates the rows of map with points
for i in range(0, 26):

    # Row 1
    if i not in [0, 12, 13]:
        points.append(Point(21 + i * 16, 23))
        points_location[21 + i * 16, 23] = True
        points_left += 1

    # Row 2
    points.append(Point(21 + i * 16, 85))
    points_location[21 + i * 16, 85] = True
    points_left += 1
    # Row 3
    if i not in [6, 7, 12, 13, 18, 19]:
        points.append(Point(21 + i * 16, 133))
        points_location[21 + i * 16, 133] = True
        points_left += 1
    # Row 4
    if i not in [0, 12, 13, 25]:
        points.append(Point(21 + i * 16, 325))
        points_location[21 + i * 16, 325] = True
        points_left += 1
    # Row 5
    if i not in [3, 4, 21, 22]:
        points.append(Point(21 + i * 16, 374))
        points_location[21 + i * 16, 374] = True
        points_left += 1
    # Row 6
    if i not in [6, 7, 12, 13, 18, 19]:
        points.append(Point(21 + i * 16, 421))
        points_location[21 + i * 16, 421] = True
        points_left += 1
    # Row 7
    points.append(Point(21 + i * 16, 470))
    points_location[21 + i * 16, 470] = True
    points_left += 1

# populates the columns with points
for i in range(0, 28):

    # Column 1 and 10
    if i not in [0, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 22, 23, 24, 25]:
        points.append(Point(21, 21 + i * 16))
        points.append(Point(421, 21 + i * 16))
        points_location[21, 21 + i * 16] = True
        points_location[421, 21 + i * 16] = True
        points_left += 2
    # Column 2 and 9
    if i in [23, 24]:
        points.append(Point(53, 21 + i * 16))
        points.append(Point(389, 21 + i * 16))
        points_location[53, 21 + i * 16] = True
        points_location[389, 21 + i * 16] = True
        points_left += 2
    # Column 3 and 8
    if i not in [0, 4, 7, 19, 22, 25, 26, 27]:
        points.append(Point(101, 21 + i * 16))
        points.append(Point(341, 21 + i * 16))
        points_location[101, 21 + i * 16] = True
        points_location[341, 21 + i * 16] = True
        points_left += 2
    # Column 4 and 7
    if i in [5, 6, 23, 24]:
        points.append(Point(149, 21 + i * 16))
        points.append(Point(293, 21 + i * 16))
        points_location[149, 21 + i * 16] = True
        points_location[293, 21 + i * 16] = True
        points_left += 2
    # Column 5 and 6
    if i in [1, 2, 3, 20, 21, 26, 27]:
        points.append(Point(197, 21 + i * 16))
        points.append(Point(245, 21 + i * 16))
        points_location[197, 21 + i * 16] = True
        points_location[245, 21 + i * 16] = True
        points_left += 2

# Score
score_value = 0
font = pygame.font.Font('Resources\\emulogic.ttf', 32)
# postion of the score on the screen
text_X = 10
text_Y = 500


# show_score function to print the score on the screen
def show_score(x, y):
    score = font.render("Score:" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

# functino to calculate x power 2
def power2(x):
    return x * x

# function to check if pacman near to any pont by calculating the distance between pacman and each point
def point_collsion(player):
    for k, o in enumerate(points):
        if math.sqrt(power2(o.rect.centerx - player.rect.centerx) + power2(o.rect.centery - player.rect.centery)) <= 9:
            del points[k]
            # decrease the cnt valye by one when a point is deleted
            global cnt, score_value
            score_value += 100
            break


# main loop in which the game runs
running = True
while running:

    # iterate through all events generated from pygame
    for event in pygame.event.get():

        ghost_list[0].move(map)
        ghost_list[1].move(map)
        ghost_list[2].move(map)

        # quits when pacman eat all the points
        if points_left == 0:
            running = False
        # quits when user presses the X
        if event.type == pygame.QUIT:
            running = False

        # this event is generated by the ghost class to tell them to change direction
        # note: don't iterate through the list of ghosts to change direction, this implementation is faster
        if event.type == 30:
            ghost_list[0].changeDirection()
            ghost_list[1].changeDirection()
            ghost_list[2].changeDirection()


        # detects keyboard presses
        elif event.type == pygame.KEYDOWN:
            # exits if user presses the escape button
            if event.key == pygame.K_ESCAPE:
                running = False
        # generates a dictionary which contains all the buttons currently pressed
        pressed = pygame.key.get_pressed()

        # the 4 following conditions each correspond to a direction {up,down,left,right}
        if pressed[pygame.K_UP]:
            player.move("u", map)

        elif pressed[pygame.K_DOWN]:
            player.move("d", map)

        elif pressed[pygame.K_LEFT]:
            player.move("l", map)

        elif pressed[pygame.K_RIGHT]:
            player.move("r", map)

    # fills the screen with black to to prepare for the next frame
    screen.fill((0, 0, 0))

    # search if there is any point near to pacman, and if one is found remove it from points list
    point_collsion(player)

    # iterate through the list of points drawing them
    for p in points:
        screen.blit(p.image, p.rect)
    # draw ghosts
    for g in ghost_list:
        screen.blit(g.image, g.rect)
    # iterates through the list of sprites, drawing each image inside its rectangle
    for i in game_group:
        screen.blit(i.image, i.rect)

    # print the score
    show_score(text_X, text_Y)

    # updates the frame
    pygame.display.flip()
