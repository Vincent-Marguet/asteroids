#!/usr/bin/env -S python3 -i

# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    """
    Main function of Asteroids game
    """
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player_1.update(dt)
        player_1.draw(screen)
        pygame.display.flip()
        clock.tick(60.00)
        dt = clock.tick(60.00) / 1000


if __name__ == "__main__":
    main()
