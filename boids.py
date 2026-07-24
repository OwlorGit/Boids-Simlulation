import pygame 
import random
from math import sqrt

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

NUM_BOIDS = 25
boids_list = []
boids_listX = []
boids_listY = []

# Separation
# Cohesion
# Alignment  

#COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Boid:
    def __init__(self):
        self.radius = 10
        self.max_speed = 3
        self.velocityX = random.uniform(-3, 3)
        self.velocityY = random.uniform(-3, 3)
        self.position = pygame.math.Vector2(
            random.randint(self.radius, WIDTH - self.radius),
            random.randint(self.radius, HEIGHT - self.radius)
        )
    
    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (int(self.position.x), int(self.position.y)), self.radius)

    def movement(self):
        self.position.x += self.velocityX
        self.position.y += self.velocityY
        distanceX = self.position.x - (self.position.x - self.velocityX)
        distanceY = self.position.y - (self.position.y - self.velocityY)
        acutal_distance = sqrt(distanceX**2 + distanceY**2)
        if acutal_distance > self.max_speed:
            acutal_distance = self.max_speed

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