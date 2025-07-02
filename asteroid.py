import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        astroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        astroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        astroid1.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle) * 1.2
        astroid2.velocity = pygame.math.Vector2.rotate(self.velocity, -random_angle) * 1.2


