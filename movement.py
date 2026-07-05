import pygame 
import random

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
        self.speed = 3
        self.angle = random.uniform(0, 360)
        self.position = pygame.math.Vector2(
            random.randint(self.radius, WIDTH - self.radius),
            random.randint(self.radius, HEIGHT - self.radius)
        )
        self.velocity = pygame.math.Vector2()
        self.velocity.from_polar((self.speed, self.angle))
    
    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (int(self.position.x), int(self.position.y)), self.radius)

    def movement(self):
        self.position += self.velocity
        
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
        boid.wall_collision()
        boid.draw(screen, WHITE)

    for i in range(min(len(boids_listX), len(boids_listY))):
        print(f"Boid {i + 1}: {boids_listX[i]}, {boids_listY[i]}")  
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()