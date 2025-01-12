#!/usr/bin/env -S python3 -i
"""
This is the module for Asteroid class
"""

import pygame

from circleshape import CircleShape


class Asteroid(CircleShape):
    """
    Asteroid class
    """

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        """
        Overrides the CircleShape draw method.
        """
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=2,
        )

    def update(self, dt):
        """
        Override CircleShape update method.
        """
        self.position += self.velocity * dt
