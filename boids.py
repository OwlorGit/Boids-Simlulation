import pygame 
import random
import math
from pprint import pprint
from pygame.math import Vector2


# Physics/Boid forces
NUM_BOIDS = 150
BOIDS_SPEED = 1
MAX_ACCELERATION = 2
FRICTION = 0.85
DETECTION_LIMIT = 100
SEPERATION_FORCE = 1
ALIGNEMENT_FORCE = 1
COHESION_FORCE = 1

# Dimensions
WIDTH, HEIGHT = 1600, 800
CELL_SIZE = DETECTION_LIMIT
CELL_BORDER = 1
dict_cell = {}

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DEEP_SLATE_GREY = (48, 50, 52)


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

class Grid(Boid):
    def __init__(self):
        self.num_row = int(WIDTH / CELL_SIZE)
        self.num_col = int(HEIGHT / CELL_SIZE)
        self.cell_size = CELL_SIZE
        self.cell_border = CELL_BORDER
        super().__init__()

    def grid_logic(self, process_type):
        for i in range(self.num_row):
            for j in range(self.num_col):
                if process_type == "init":
                    dict_cell[(i, j)] = {
                        "position_x": self.cell_size * i,
                        "position_y": self.cell_size * j
                    }
                elif process_type == "update":
                    pygame.draw.rect(screen, DEEP_SLATE_GREY, (self.cell_size * i, self.cell_size * j, self.cell_size, self.cell_size), self.cell_border)

    def calculation(self):
        pass
                    

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

boids_list = []
for _ in range(NUM_BOIDS):
    boids_list.append(Boid())

grid = Grid()
grid.grid_logic(process_type="init")
pprint(dict_cell)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLACK) 
    grid.grid_logic(process_type="update")
    
    for boid in boids_list:
        boid.movement()    
        boid.wall_collision()
        boid.physics(SEPERATION_FORCE, ALIGNEMENT_FORCE, COHESION_FORCE, DETECTION_LIMIT)
        boid.draw(screen, WHITE)
   
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
