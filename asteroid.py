import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

class Asteroid(CircleShape):
    containers = ()
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        for group in self.containers:
            group.add(self)

    def draw(self, screen):
        center = (self.position.x, self.position.y)
        pygame.draw.circle(screen, "white", center, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt


