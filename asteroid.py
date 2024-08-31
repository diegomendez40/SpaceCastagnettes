from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = 0


    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, width=2)


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            # rotate
            v1 = self.velocity.rotate(angle)
            v2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            ast1 = Asteroid(*self.position, new_radius)
            ast2 = Asteroid(*self.position, new_radius)
            ast1.velocity = v1 * 1.2
            ast2.velocity = v2 * 1.2
        return (ast1, ast2)

    def update(self, dt):
        self.position += self.velocity * dt