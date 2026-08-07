import pygame
from src.grid import SpatialGrid
from src.boid import Boid
from src.stats import Stats
from src.config import WIDTH, HEIGHT, NUM_BOIDS, BLACK, WHITE, LIGHT_BLUE

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
        self.boids_list = []
        for _ in range(NUM_BOIDS):
            self.boids_list.append(Boid())

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

        self.stats.fps_tracker()
        self.stats.boid_information()    

        pygame.display.flip()

    def run(self):
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()     