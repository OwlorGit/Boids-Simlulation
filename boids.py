import pygame 
import random
import math
from pygame.math import Vector2

pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

# CONSTANTS
NUM_BOIDS = 25
BOIDS_SPEED = 1
FRICTION = 0.85
DETECTION_LIMIT = 50
SEPERATION_FORCE = 0.01

boids_list = []

#COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Boid:
    def __init__(self):
        self.radius = 10
        self.acceleration = Vector2(0, 0)
        self.velocity = Vector2(0, 0)
        self.position = Vector2(random.randint(self.radius, WIDTH - self.radius), 
                                random.randint(self.radius, HEIGHT - self.radius))
        self.direction = Vector2(0, 0)
        while self.direction == Vector2(0, 0):
          self.direction = Vector2(random.choice([-1, 0, 1]), random.choice([-1, 0, 1]))
        
    
    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (int(self.position.x), int(self.position.y)), self.radius)

    def movement(self):
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

    def seperation(self, seperation_strength, detection_limit):
        count = 0
        sep = Vector2(0, 0)

        for neighbor in boids_list:
            if neighbor is not self: 
                distance = (self.position - neighbor.position).length()
                if 0 < distance < detection_limit:
                    count += 1
                    sep += (self.position - neighbor.position) 

        if count > 0: 
            sep /= count
            self.direction = sep * seperation_strength
                        

    def cohesion(self):
        pass

    def alignement(self):
        pass
        


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
        boid.seperation(SEPERATION_FORCE, DETECTION_LIMIT)
        boid.draw(screen, WHITE)
   
    pygame.display.flip()
    clock.tick(60)
pygame.quit()