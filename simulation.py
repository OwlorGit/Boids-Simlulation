import pygame
from grid import SpatialGrid
from boid import Boid
from config import WIDTH, HEIGHT, NUM_BOIDS, BLACK, WHITE, LIGHT_BLUE

class Simulation:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Boid Simulation")
        self.clock = pygame.time.Clock()
        self.running = False
        self.font = pygame.font.SysFont(None, 25)

        self.grid = SpatialGrid()
        self.boids_list = []
        for _ in range(NUM_BOIDS):
            self.boids_list.append(Boid())

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def fps_tracker(self):
        fps_text = str(int(self.clock.get_fps()))
        fps_surface = self.font.render(f"FPS: {fps_text}", True, LIGHT_BLUE)
        self.screen.blit(fps_surface, (10, 10))

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

        self.fps_tracker()
        pygame.display.flip()

    def run(self):
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()     