from circleshape import CircleShape
from shot import Shot
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN
)
import pygame
from typing import List

class Player(CircleShape):

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        self.score = 0  # Añadimos el atributo de puntuación

    def triangle(self) -> List[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]


    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, 'white', self.triangle(), 2)


    def move(self, dt: float) -> None:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt


    def shoot(self) -> None:
        shot = Shot(self.position.x, self.position.y)
        velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = PLAYER_SHOOT_SPEED * velocity


    def update(self, dt: float) -> None:
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.shoot_timer <= 0:
                self.shoot()
                self.shoot_timer = PLAYER_SHOOT_COOLDOWN

    def increase_score(self, points: int) -> None:
        self.score += points