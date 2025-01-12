"""
This module implements the CircleShape class.
It inherits from the lib pygame, module sprite, class Sprite.

It has these methods:

- draw which must be overriden by child class

- update which must be overriden by child class

"""

#!/usr/bin/env python

import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    """
    Simple class to handle CircleShape
    """

    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
