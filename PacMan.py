import pygame
import numpy as np
from Modules.level import Level, Point
from Modules.mobs import Player

#initializes some standard pygame classes
pygame.init()

# change game icon and name
pygame.display.set_caption("PAC-MAN")
icon = pygame.image.load("Resources\\icon.png")
pygame.display.set_icon(icon)

#makes a level and player instance
level = Level()
player = Player()

#adds all sprites to the variable game_group
game_group = pygame.sprite.Group()
game_group.add(level, player)

#sets the window size to the size specified in the level object(dimensions of the map image)
screen_size = level.size
screen = pygame.display.set_mode(screen_size)

points = []

# boolean 2d array to store points location
# so any location on the map that contain a point we will make it = True in the 2d array
points_location = np.zeros((level.size), dtype=bool)

# store the points location in points list and make it true in the 2d list
for i in range(0, 26):

    # Row 1
    if i not in [0, 12, 13]:
        points.append(Point(21 + i * 16, 23))
        points_location[21 + i * 16, 23] = True
    
    #Row 2
    points.append(Point(21 + i*16, 85))
    points_location[21 + i*16, 85] = True
    
    #Row 3
    if i not in [6, 7, 12, 13, 18, 19]:
        points.append(Point(21 + i*16, 133))
        points_location[21 + i*16, 133] = True
    
    #Row 4
    if i not in [12, 13]:
        points.append(Point(21 + i*16, 325))
        points_location[21 + i*16, 325] = True
    
    #Row 5
    if i not in [3, 4, 21, 22]:
        points.append(Point(21 + i*16, 374))
        points_location[21 + i*16, 374] = True

    #Row 6
    if i not in [6, 7, 12, 13, 18, 19]:
        points.append(Point(21 + i*16, 421))
        points_location[21 + i*16, 421] = True

    #Row 7
    points.append(Point(21 + i*16, 470))
    points_location[21 + i*16, 470] = True

for i in range(0, 28):

    #Column 1 and 10
    if i not in [0, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 22, 23, 24, 25]:
        points.append(Point(21, 21 + i*16))
        points.append(Point(421, 21 + i*16))
        points_location[21, 21 + i*16] = True
        points_location[421, 21 + i*16] = True
    
    #Column 2 and 9
    if i in [23, 24]:
        points.append(Point(53, 21 + i*16))
        points.append(Point(389, 21 + i*16))
        points_location[53, 21 + i*16] = True
        points_location[389, 21 + i*16] = True

    #Column 3 and 8
    if i not in [0, 4, 7, 19, 22, 25, 26, 27]:
        points.append(Point(101, 21 + i*16))
        points.append(Point(341, 21 + i*16))
        points_location[101, 21 + i*16] = True
        points_location[341, 21 + i*16] = True

    #Column 4 and 7
    if i in [5, 6, 23, 24]:
        points.append(Point(149, 21 + i*16))
        points.append(Point(293, 21 + i*16))
        points_location[149, 21 + i*16] = True
        points_location[293, 21 + i*16] = True

    #Column 5 and 6
    if i in [1, 2, 3, 20, 21, 26, 27]:
        points.append(Point(197, 21 + i*16))
        points.append(Point(245, 21 + i*16))
        points_location[197, 21 + i*16] = True
        points_location[245, 21 + i*16] = True


#main loop in which the game runs
running = True
while running:

    #iterate through all events generated from pygame
    for event in pygame.event.get():
        #quits when user presses the X
        if event.type == pygame.QUIT:
            running = False
        #detects keyboard presses
        elif event.type == pygame.KEYDOWN:
            #exits if user presses the escape button
            if event.key == pygame.K_ESCAPE:
                running = False
        #generates a dictionary which contains all the buttons currently pressed
        pressed = pygame.key.get_pressed()

        #the 4 following conditions each correspond to a direction {up,down,left,right}
        if pressed[pygame.K_UP]:
            player.move("u", level)

        elif pressed[pygame.K_DOWN]:
            player.move("d", level)

        elif pressed[pygame.K_LEFT]:
            player.move("l", level)

        elif pressed[pygame.K_RIGHT]:
            player.move("r", level)

    #fills the screen with black to to prepare for the next frame
    screen.fill((0, 0, 0))

    # search if there is any point near to pacman, and if one is found make it false in the 2d list and remove it from points list
    for i in range(-10, 10):
        for j in range(-10, 10):
            if points_location[player.rect.centerx + i, player.rect.centery + j] == True:
                points_location[player.rect.centerx + i, player.rect.centery + j] = False
                # search in the whole poins list for this point
                for k, o in enumerate(points):
                    if o.rect.x == player.rect.centerx + i:
                        del points[k]
                        break
                break


    for p in points:
        screen.blit(p.image, p.rect)

    #iterates through the list of sprites, drawing each image inside its rectangle
    for i in game_group:
        screen.blit(i.image, i.rect)

    #updates the frame
    pygame.display.flip()
