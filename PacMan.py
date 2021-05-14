import pygame
from Modules.level import Level
from Modules.mobs import Player

pygame.init()

level = Level()
player = Player()
game_group = pygame.sprite.Group()
game_group.add(level, player)

screen_size = level.size
screen = pygame.display.set_mode(screen_size)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                pygame.quit()

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            player.move("u", level)

        elif pressed[pygame.K_DOWN]:
            player.move("d", level)

        elif pressed[pygame.K_LEFT]:
            player.move("l", level)

        elif pressed[pygame.K_RIGHT]:
            player.move("r", level)

    screen.fill((0, 0, 0))

    for i in game_group:
        screen.blit(i.image, i.rect)

    pygame.display.flip()
