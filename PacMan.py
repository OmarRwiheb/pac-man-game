import pygame
from Modules.level import Level
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
    
    #iterates through the list of sprites, drawing each image inside its rectangle
    for i in game_group:
        screen.blit(i.image, i.rect)
    #updates the frame
    pygame.display.flip()
