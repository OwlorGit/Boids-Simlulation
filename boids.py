import pygame 
import random
from math import sqrt
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
BOID_SIGHT = 50

boids_list = []
boids_listX = []
boids_listY = []

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
        self.starting_direction = Vector2(0, 0)
        while self.starting_direction == Vector2(0, 0):
          self.starting_direction = Vector2(random.choice([-1, 0, 1]), random.choice([-1, 0, 1]))
        
    
    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (int(self.position.x), int(self.position.y)), self.radius)

    def movement(self):
        self.acceleration = self.starting_direction * BOIDS_SPEED
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
                              

for _ in range(NUM_BOIDS):
    boids_list.append(Boid())

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLACK)
    boids_listX.clear()
    boids_listY.clear()

    for boid in boids_list:
        boid.movement()
        boids_listX.append(boid.position.x)
        boids_listY.append(boid.position.y) 
    
    for boid in boids_list:    
        boid.wall_collision()
        boid.draw(screen, WHITE)
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()