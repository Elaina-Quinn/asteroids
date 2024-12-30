import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # fps variables
    clock = pygame.time.Clock()
    dt = 0

    # player initilization
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    # infinite while loop to run asteroids continuously
    while True:
        # exits the program when window is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()

        # fps limit
        dt = (clock.tick(60)) / 1000



if __name__ == "__main__":
    main()
