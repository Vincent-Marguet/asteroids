#!/usr/bin/env -S python3 -i
"""
This is the module for Asteroid class
"""

import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    """
    Asteroid class
    """

    container = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

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

    def split(self):
        """
        Split asteroids in two smaller if possible
        """
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        random_angle = random.uniform(20, 50)

        velocity_1 = self.velocity.rotate(random_angle) * 1.2
        velocity_2 = self.velocity.rotate(-random_angle) * 1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        pos = pygame.Vector2(self.position.x, self.position.y)

        split_1 = Asteroid(pos.x, pos.y, new_radius)
        split_2 = Asteroid(pos.x, pos.y, new_radius)

        split_1.velocity = velocity_1
        split_2.velocity = velocity_2

        self.kill()
