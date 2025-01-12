#!/usr/bin/env -S python3 -i
"""
This module handles the Player class.
Player class inherits from CircleShape class.

It has these methods:

- triangle method to move and calculate new
position.

- draw which overrides parent's method as intended

"""


import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED


class Player(CircleShape):
    """
    Implements Player class as a Circle
    """

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        """
        Represents the player as a Triangle instead of a Circle
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        """
        Overrides the CircleShape draw method.
        Draw the Player triangle.
        """
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        """
        Rotate Player by adding value to rotation member
        """
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
