from circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame

class Shot(CircleShape):

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = 0

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, 'white', self.position, self.radius, width=2)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt