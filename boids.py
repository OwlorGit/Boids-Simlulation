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
        self.velocityX = random.choice([-3, 3])
        self.velocityY = random.choice([-3, 3])
        self.position = pygame.math.Vector2(
            random.randint(self.radius, WIDTH - self.radius),
            random.randint(self.radius, HEIGHT - self.radius)
        )
    
    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (int(self.position.x), int(self.position.y)), self.radius)

    def movement(self):
        self.position.x += self.velocityX
        self.position.y += self.velocityY
        
        boids_listX.append(self.position.x)
        boids_listY.append(self.position.y)    

    def wall_collision(self):
        if self.position.x < self.radius:
            self.position.x += WIDTH     
        elif self.position.x > WIDTH - self.radius:
            self.position.x -= WIDTH
        if self.position.y < self.radius:
            self.position.y += HEIGHT
        elif self.position.y > HEIGHT - self.radius:
            self.position.y -= HEIGHT       
    
    def separation(self, detection_limit, separation_strength):
        sep_x = 0
        sep_y = 0
        count = 0
        
        current_index = boids_list.index(self)
        
        for boid_id in range(len(boids_listX)):
            if boid_id != current_index: 
                distance_x = boids_listX[boid_id] - self.position.x
                distance_y = boids_listY[boid_id] - self.position.y
                actual_distance = sqrt(distance_x**2 + distance_y**2)
                
                if 0 < actual_distance < detection_limit:
                    sep_x += distance_x / actual_distance
                    sep_y += distance_y / actual_distance
                    count += 1
        
        if count > 0:
            sep_x /= count
            sep_y /= count
            self.velocityX += sep_x * separation_strength * 0.01
            self.velocityY += sep_y * separation_strength * 0.01

                              

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
        boid.separation(300, 10)
        boid.wall_collision()
        boid.draw(screen, WHITE)
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
