import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def check_collision(self, threat: 'CircleShape'):
        # distance = math.sqrt( (self.position.x - threat.position.x)^2 + (self.position.y - threat.position.y)^2)
        distance = self.position.distance_to(threat.position)
        return (distance <= (self.radius + threat.radius))

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass