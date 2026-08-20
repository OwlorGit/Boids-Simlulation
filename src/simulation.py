import pygame
from src.grid import SpatialGrid
from src.boid import Boid
from src.obstacle import Obstacle
from src.stats import Stats
from config import (
    WIDTH, 
    HEIGHT, 
    NUM_BOIDS, 
    NUM_OBSTACLES, 
    BLACK, 
    WHITE,
    LIGHT_GREY
)

class Simulation:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Boid Simulation")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 25)
        self.running = False

        self.grid = SpatialGrid()
        self.stats = Stats(self.screen, self.clock)

        self.boids_list = [Boid() for _ in range(NUM_BOIDS)]
        self.obstacle_list = [Obstacle() for _ in range(NUM_OBSTACLES)]

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.grid.reset()
        boid_cell_indices = []
        for boid in self.boids_list:
            boid.movement()
            boid.wall_collision()
            cell_idx = boid.locate_in_grid(self.grid)
            boid_cell_indices.append(cell_idx)

        for boid, (cell_x, cell_y) in zip(self.boids_list, boid_cell_indices):
            neighbors = self.grid.surronding_boids(cell_x, cell_y)
            boid.physics(neighbors)

    def draw(self):
        self.screen.fill(BLACK)
        self.grid.draw(self.screen)

        for boid in self.boids_list:
            boid.draw(self.screen, WHITE)

        for obstacle in self.obstacle_list:
            obstacle.draw(self.screen, LIGHT_GREY)

        self.stats.display_info()
        pygame.display.flip()

    def run(self):
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()     