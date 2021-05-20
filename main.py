import pygame
import time
import random

from Modules.map import Map
from Modules.player import Player
from Modules.points import draw_points
from Modules.ghosts import Ghost
from Modules.superpoints import SuperPoint


# initializes some standard pygame classes
pygame.init()
#play start game sound
game_music = pygame.mixer.music.load("sound\\start the game.wav")
pygame.mixer.music.play()
# change game icon and name
pygame.display.set_caption("PAC-MAN")
icon = pygame.image.load("Resources\\icon.png")
pygame.display.set_icon(icon)

# makes a level instance
level = Map()
# makes a player instance
player = Player()

# variable to track whether the player has died or not
player_state = 2
# number of ghosts alive
ghosts_alive = 4

# a list containing all locations of the ghosts
ghost_list = [(410, 460), (10, 460), (410, 10), (280, 250)]
# list of superpoint locations
super_points_list = [(138, 170), (295, 170), (138, 278), (295, 278)]

# adds the player and the map sprites to a sprite group
game_group = pygame.sprite.Group()
game_group.add(level, player)

# creates ghosts and add them to a sprite group
ghosts_group = pygame.sprite.Group()

for x, y in ghost_list:
    ghosts_group.add(Ghost(x, y, player))

# creates super points and add them to a sprite group
super_points_group = pygame.sprite.Group()

for x, y in super_points_list:
    super_points_group.add(SuperPoint(x, y))

# Storing the point objects group and the points left value from draw_points function
points_group, points_left = draw_points()

# sets the window size to the size specified in the level object(dimensions of the map image)
screen_size = level.size
screen = pygame.display.set_mode(screen_size)

# Score
score_value = 0
font1 = pygame.font.Font('Resources\\emulogic.ttf', 32)
font2 = pygame.font.Font('Resources\\emulogic.ttf', 19)

#position of the score on the screen
text_X = 10
text_Y = 500
tip = random.choice(["Kill all ghosts to win!", "Eat all points to win!"])


# show_score function to print the score on the screen
def show_score(x, y, player_state):
    score = font1.render("Score:" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
    #when the players loses
    if player_state == 0:
        score = font1.render("You Died!", True, (255, 255, 255))
        screen.blit(score, (x, y+50))
    #when the player wins
    elif player_state == 1:
        score = font1.render("You Won!", True, (255, 255, 255))
        screen.blit(score, (x, y+50))
    #while the game is running
    else:
        score = font2.render(tip, True, (255, 255, 255))
        screen.blit(score, (x, y+50))

#event to update player attributes, fires every 60 ms
UPDATE_PLAYER = pygame.USEREVENT + 1
pygame.time.set_timer(UPDATE_PLAYER, 60)

#event to update ghost attributes, fires every 60 ms
UPDATE_GHOSTS = pygame.USEREVENT + 2
pygame.time.set_timer(UPDATE_GHOSTS, 60)

# main loop in which the game runs
running = True
while running:

    # iterate through all events generated from pygame
    for event in pygame.event.get():

        # quits when user presses the X
        if event.type == pygame.QUIT:
            running = False

        # detects keyboard presses
        if event.type == pygame.KEYDOWN:

            # exits if user presses the escape button
            if event.key == pygame.K_ESCAPE:
                running = False
        
        if event.type == UPDATE_PLAYER:
            #if pac has strength, he should lose it by time
            if player.strength > 0:
                player.strength -= 1.2
            #reset pac's strength and speed
            else:
                player.strength = 0
                player.speed = 4

            # generates a dictionary which contains all the buttons currently pressed
            pressed = pygame.key.get_pressed()

            # the 4 following conditions each correspond to a direction {up,down,left,right}
            if pressed[pygame.K_UP]:
                player.move("u", level)

            elif pressed[pygame.K_DOWN]:
                player.move("d", level)

            elif pressed[pygame.K_LEFT]:
                player.move("l", level)

            elif pressed[pygame.K_RIGHT]:
                player.move("r", level)

        # this event updates ghost attributes and changes their directions
        if event.type == UPDATE_GHOSTS:
            #iterate through the list of ghosts
            for g in ghosts_group:
                g.move(level)

                #make them strong if pac isn't strong
                if player.strength == 0:
                    g.weakened = False
                
                #if they are weak check if pac is close to them so they can run away
                if g.weakened:
                    if g.check_player(50)[0] == g.current_direction == "l":
                        g.change_direction()

                    elif g.check_player(50)[0] == g.current_direction == "r":
                        g.change_direction()

                    if g.check_player(50)[1] == g.current_direction == "u":
                        g.change_direction()

                    elif g.check_player(50)[1] == g.current_direction == "d":
                        g.change_direction()

    #if pac collided with a superpoint put it into super_points_eaten
    super_points_eaten = pygame.sprite.spritecollide(
        player, super_points_group, False)
    #if super_points_eaten is not empty
    if super_points_eaten:

        #if pac has strength, don't eat another point
        if player.strength > 0:
            pass
        #if pac is weak, remove the super point, give him 100 strength, increase his speed
        else:
            #plays cherry eating sound
            eat = pygame.mixer.music.load("sound\\pac_eat cherries.wav")
            pygame.mixer.music.play()
            
            super_points_eaten[0].kill()
            player.strength = 100
            player.speed = 6

            #set ghosts to weak
            for g in ghosts_group:
                g.weakened = True
                g.change_direction()

    #if pac collides with a ghost, put it into collided_ghosts
    collided_ghosts = pygame.sprite.spritecollide(player, ghosts_group, False)
    #if collided_ghosts is not empty
    if collided_ghosts:
        #if pac is strong, remove the ghost
        if player.strength > 0:
            #play ghost eating sound
            strong = pygame.mixer.music.load("sound\\pac_strong.mp3")
            pygame.mixer.music.play()
            
            collided_ghosts[0].kill()
            score_value += 5000
            ghosts_alive -= 1

        #if pac is weak, change the state into dead state
        else:
            #play dying sound
            fail = pygame.mixer.music.load("sound\\pac_fail.wav")
            pygame.mixer.music.play()
            player_state = 0
            running = False

    # search if there is any point near to pacman, and if one is found remove it from points list
    points_eaten = pygame.sprite.spritecollide(player, points_group, True)
    if points_eaten:
        points_left -= 1
        score_value += 100

    # quits when pacman eat all the points or ghosts
    if points_left == 0 or ghosts_alive == 0:
        #play winning sound
        win = pygame.mixer.music.load("sound\\pac_win.mp3")
        pygame.mixer.music.play()
        player_state = 1
        running = False

    # fills the screen with black to to prepare for the next frame
    screen.fill((0, 0, 0))

    # iterate through the list of points drawing them
    for p in points_group:
        screen.blit(p.image, p.rect)

    # iterates through the list of sprites, drawing each image inside its rectangle
    for i in game_group:
        screen.blit(i.image, i.rect)

    for i in ghosts_group:
        screen.blit(i.image, i.rect)

    for i in super_points_group:
        screen.blit(i.image, i.rect)

    # print the score
    show_score(text_X, text_Y, player_state)
    if player_state != 2:
        time.sleep(3)
    # updates the frame
    pygame.display.flip()
