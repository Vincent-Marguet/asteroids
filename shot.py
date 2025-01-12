# access to numbers on jklm uio!/usr/bin/env -S python3 -i
"""
This is the module for Shot class
Shot class inherits from CircleShape class.

It has these methods:

- draw which overrides parent's method as intended

- update which overrides parent's method as intended

"""

import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    """
    Shot class inherit from CircleShape
    """

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = SHOT_RADIUS

    def draw(self, screen):
        """
        Override the CircleShape draw method.
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
