import pygame 
import random
import math
from pygame.math import Vector2

pygame.init()
WIDTH, HEIGHT = 1600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

# CONSTANTS
NUM_BOIDS = 200
BOIDS_SPEED = 1
MAX_ACCELERATION = 2
FRICTION = 0.85

DETECTION_LIMIT = 100
SEPERATION_FORCE = 1
ALIGNEMENT_FORCE = 1
COHESION_FORCE = 1

boids_list = []

#COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Boid:
    def __init__(self):
        self.radius = 5
        self.acceleration = Vector2(0, 0)
        self.velocity = Vector2(0, 0)
        self.position = Vector2(random.randint(self.radius, WIDTH - self.radius), 
                                random.randint(self.radius, HEIGHT - self.radius))
        self.direction = Vector2(0, 0)
        while self.direction == Vector2(0, 0):
          self.direction = Vector2(random.choice([-1, 0, 1]), random.choice([-1, 0, 1]))

          if self.direction.length() > 0:
              self.direction.normalize_ip()
        
    
    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (int(self.position.x), int(self.position.y)), self.radius)

    def movement(self):
        if self.direction.length() > MAX_ACCELERATION:
            self.direction.normalize_ip()
            self.direction *= MAX_ACCELERATION

        self.acceleration = self.direction * BOIDS_SPEED
        self.velocity += self.acceleration
        self.velocity *= FRICTION
        self.position += self.velocity

    def wall_collision(self):
        if self.position.x < self.radius:
            self.position.x += WIDTH     
        elif self.position.x > WIDTH - self.radius:
            self.position.x -= WIDTH
        if self.position.y < self.radius:
            self.position.y += HEIGHT
        elif self.position.y > HEIGHT - self.radius:
            self.position.y -= HEIGHT

    def physics(self, seperation_strength, alignement_strength, cohesion_strength, detection_limit):
        count = 0
        sep = Vector2(0, 0)
        align = Vector2(0, 0)
        coh = Vector2(0, 0)
        center_mass = Vector2(0, 0)

        for neighbor in boids_list:
            if neighbor is not self:
                diff = self.position - neighbor.position
                distance = diff.length()

                if 0 < distance < detection_limit:
                    dispersion_force = diff.normalize() / distance
                    sep += dispersion_force
                    align += neighbor.direction
                    center_mass += neighbor.position
                    count += 1

        if count > 0:

            sep /= count
            if sep.length() > 0:
                sep.normalize_ip()
                self.direction += sep * seperation_strength

            align /= count
            if align.length() > 0:
                align.normalize_ip()
                self.direction += align * alignement_strength

            center_mass /= count 
            coh = center_mass - self.position
            if coh.length() > 0:
                coh.normalize_ip()
                self.direction += coh * cohesion_strength            
        

for _ in range(NUM_BOIDS):
    boids_list.append(Boid())

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLACK) 
    
    for boid in boids_list:
        boid.movement()    
        boid.wall_collision()
        boid.physics(SEPERATION_FORCE, ALIGNEMENT_FORCE, COHESION_FORCE, DETECTION_LIMIT)
        boid.draw(screen, WHITE)
   
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
