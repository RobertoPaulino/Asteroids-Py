import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from encodings import rot_13

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20,50)

        rot_1 = self.velocity.rotate(angle)
        rot_2 = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = rot_1 * 1.2

        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = rot_2 * 1.2
