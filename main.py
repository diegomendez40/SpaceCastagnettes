# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
import pygame.font

from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((0,0,0))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    # Spawn the player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    updatable.add(player)
    drawable.add(player)
    # Spawn the asteroid field
    asteroid_field = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0
    font = pygame.font.Font(None, 36)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for upd in updatable:
            upd.update(dt)
        for ast in asteroids:
            if ast.check_collision(player):
                sys.exit("Game over!")
            for bullet in shots:
                if ast.check_collision(bullet):
                    player.increase_score(ASTEROID_SCORE_VALUE)
                    ast.split()
                    bullet.kill()
        for dr in drawable:
            dr.draw(screen)
        # Dibujar la puntuación
        score_text = font.render(f"Score / Puntuación: {player.score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()