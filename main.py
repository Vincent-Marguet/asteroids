#!/usr/bin/env -S python3 -i

# this allows us to use code from
# the open-source pygame library
# throughout this file

import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from shot import Shot


def main():
    """
    Main function of Asteroids game:

    1) Prints info
    2) Initialize pygame lib
    3) Setup the clock
    4) Create 4 groups to handle
    multiple objects on screen
    5) Assign a class member to each class
    the game uses to assign objects to
    groups created in step 4
    6) Create a player and an asteroic field
    7) Create the game loop
    """
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = updatables
    Asteroid.containers = (updatables, drawables, asteroids)
    Player.containers = (updatables, drawables)
    Shot.containers = (updatables, drawables, shots)

    player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroic_field_1 = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for updatable in updatables:
            updatable.update(dt)
        for asteroid in list(asteroids):
            if asteroid.collision_check(player_1) is True:
                print("Game Over!")
                sys.exit()
            for shot in list(shots):
                if shot.collision_check(asteroid) is True:
                    asteroid.split()
                    shot.kill()
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        clock.tick(60.00)
        dt = clock.tick(60.00) / 1000


if __name__ == "__main__":
    main()
