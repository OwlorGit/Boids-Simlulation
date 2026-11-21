import pygame
from src.config import (
    WIDTH, 
    HEIGHT, 
    CELL_SIZE, 
    CELL_BORDER, 
    NEIGHBOR_CELLS, 
    DEEP_SLATE_GREY
)

class SpatialGrid():
    def __init__(self):
        self.num_rows = int(WIDTH / CELL_SIZE)
        self.num_cols = int(HEIGHT / CELL_SIZE)
        self.cells = {}

    def reset(self):
        self.cells.clear()

    def draw(self, screen):
        for x in range(self.num_rows):
            for y in range(self.num_cols):
                rect = (
                    x * CELL_SIZE,
                    y * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE
                )
                pygame.draw.rect(screen, DEEP_SLATE_GREY, rect, CELL_BORDER)

    def surrounding_boids(self, cell_x, cell_y):
        surrounding_boids = []
        for neighbor_row in NEIGHBOR_CELLS:
            for x_offset, y_offset in neighbor_row:
                surrounding_cell_x = (cell_x + x_offset) % self.num_rows
                surrounding_cell_y = (cell_y + y_offset) % self.num_cols

                if (surrounding_cell_x, surrounding_cell_y) in self.cells:
                    surrounding_boids.extend(self.cells[(surrounding_cell_x, surrounding_cell_y)])

        return surrounding_boids