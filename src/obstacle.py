import pygame 
from random import randint
from pygame.math import Vector2
from config import (
    WIDTH,
    HEIGHT,
    MIN_RADIUS,
    MAX_RADIUS,
)

class Obstacle:
    def __init__(self):
        self.radius = randint(MIN_RADIUS, MAX_RADIUS)
        self.position = Vector2(randint(self.radius, WIDTH - self.radius)
                                ,randint(self.radius, HEIGHT - self.radius))

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (self.position.x, self.position.y), self.radius)
        