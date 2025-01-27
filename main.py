import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot

def main():

    print ("Starting asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # fps variables
    clock = pygame.time.Clock()
    dt = 0

    # creating groups and containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # object initilization
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2), shots)
    AsteroidField()

    # infinite while loop to run asteroids continuously
    while True:
        # exits the program when window is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        for i in updatable:
            i.update(dt)
        for j in drawable:
            j.draw(screen)
        pygame.display.flip()
        for h in asteroids:
            if player.collision(h):
                print ("Game over!")
                sys.exit()
            for s in shots:
                if h.collision(s):
                    h.split()
                    s.kill()


        # fps limit
        dt = (clock.tick(60)) / 1000



if __name__ == "__main__":
    main()
