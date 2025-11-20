import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

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

    def split(self):
        self.kill()
        if ASTEROID_MIN_RADIUS >= self.radius:
            return
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)
        first = Asteroid(self.position.x, self.position.y, new_radius)
        first.velocity = a * 1.2
        second = Asteroid(self.position.x, self.position.y, new_radius)
        second.velocity = b * 1.2
            


