import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS

class Shot(CircleShape):
    containers = ()
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        for group in self.containers:
            group.add(self)
        

    def draw(self, screen):
        center = (self.position.x, self.position.y)
        pygame.draw.circle(screen, "white", center, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
