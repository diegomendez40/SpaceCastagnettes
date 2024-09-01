from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random
import math
from typing import List, Tuple

class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

    def bezier_curve(self, p0: Tuple[float, float], p1: Tuple[float, float], p2: Tuple[float, float], p3: Tuple[float, float], num_points: int) -> List[Tuple[int, int]]:
        points = []
        for i in range(num_points):
            t = i / (num_points - 1)
            x = (1-t)**3*p0[0] + 3*(1-t)**2*t*p1[0] + 3*(1-t)*t**2*p2[0] + t**3*p3[0]
            y = (1-t)**3*p0[1] + 3*(1-t)**2*t*p1[1] + 3*(1-t)*t**2*p2[1] + t**3*p3[1]
            points.append((int(x), int(y)))
        return points

    def draw(self, screen: pygame.Surface) -> None:
        # Puntos de control para las curvas Bézier
        p0 = (self.position.x, self.position.y - self.radius)
        p1 = (self.position.x + self.radius, self.position.y - self.radius * 0.5)
        p2 = (self.position.x + self.radius * 0.5, self.position.y + self.radius * 0.5)
        p3 = (self.position.x, self.position.y + self.radius)
        p4 = (self.position.x - self.radius * 0.5, self.position.y + self.radius * 0.5)
        p5 = (self.position.x - self.radius, self.position.y - self.radius * 0.5)

        # Dibujar las curvas Bézier
        points1 = self.bezier_curve(p0, p1, p2, p3, 30)
        points2 = self.bezier_curve(p3, p4, p5, p0, 30)

        # Dibujar la castañuela
        pygame.draw.polygon(screen, 'white', points1 + points2[::-1], 2)

        # Añade la "lengüeta" de la castañuela
        angle = self.velocity.angle_to(pygame.Vector2(1, 0))
        end_pos = self.position + pygame.Vector2(self.radius * 0.7, 0).rotate(angle)
        pygame.draw.line(screen, 'white', self.position, end_pos, width=2)
        
        # Añade algunos detalles decorativos
        small_radius = self.radius * 0.15
        pygame.draw.circle(screen, 'white', self.position, small_radius, width=1)
        
        # Dibuja algunos puntos decorativos alrededor del borde
        for i in range(6):
            point_angle = i * 60
            point_pos = self.position + pygame.Vector2(self.radius * 0.8, 0).rotate(point_angle)
            pygame.draw.circle(screen, 'white', point_pos, 2)


    def draw_castanet_shape(self, screen: pygame.Surface) -> None:
        num_points = 20
        points = []
        for i in range(num_points):
            angle = 2 * math.pi * i / num_points
            r = self.radius * (1 - 0.2 * math.sin(angle * 2)**2)  # Modifica el radio para crear la forma de aleta
            x = self.position.x + r * math.cos(angle)
            y = self.position.y + r * math.sin(angle)
            points.append((x, y))
        pygame.draw.polygon(screen, 'white', points, width=2)


    def split(self) -> Tuple['Asteroid', 'Asteroid'] | None:
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

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt