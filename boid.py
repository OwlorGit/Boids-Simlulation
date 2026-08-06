import pygame
import random
from config import WIDTH, HEIGHT, CELL_SIZE, FRICTION, MAX_ACCELERATION, BOIDS_SPEED, SEPERATION_FORCE, ALIGNEMENT_FORCE, COHESION_FORCE, DETECTION_LIMIT
from pygame.math import Vector2 

class Boid:
    def __init__(self):
        self.radius = 3
        self.vel = Vector2(0, 0)
        self.accel = Vector2(0, 0)
        self.pos = Vector2(random.randint(self.radius, WIDTH - self.radius),
                                random.randint(self.radius, HEIGHT - self.radius))

        while self.accel == Vector2(0, 0):
            self.accel = Vector2(random.choice([-1, 0, 1]), random.choice([-1, 0, 1]))
            if self.accel.length() > 0:
                self.accel.normalize_ip()

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (int(self.pos.x), int(self.pos.y)), self.radius)

    def movement(self):
        # To prevent boids from getting infinite speed
        if self.accel.length() > MAX_ACCELERATION:
            self.accel.normalize_ip()
            self.accel *= MAX_ACCELERATION

        self.accel *= BOIDS_SPEED
        self.vel += self.accel
        self.vel *= FRICTION
        self.pos += self.vel

    def wall_collision(self):
        if self.pos.x < self.radius:
            self.pos.x += WIDTH
        elif self.pos.x > WIDTH - self.radius:
            self.pos.x -= WIDTH
        if self.pos.y < self.radius:
            self.pos.y += HEIGHT
        elif self.pos.y > HEIGHT - self.radius:
            self.pos.y -= HEIGHT  

    # Applies all three Craig Reynolds forces
    def physics(self, neighbors):
        count = 0
        sep = Vector2(0, 0)
        align = Vector2(0, 0)
        coh = Vector2(0, 0)
        center_mass = Vector2(0, 0)

        for neighbor in neighbors:
            if neighbor != self:
                distVec = self.pos - neighbor.pos
                distance = distVec.length()

                if 0 < distance < DETECTION_LIMIT:
                    sep += distVec.normalize() / distance
                    align += neighbor.accel
                    center_mass += neighbor.pos
                    count += 1

        if count > 0:
            sep /= count 
            if sep.length() > 0:
                sep.normalize_ip()
                self.accel += sep * SEPERATION_FORCE

            align /= count
            if align.length() > 0:
                align.normalize_ip()
                self.accel += align * ALIGNEMENT_FORCE

            center_mass /= count
            coh = center_mass - self.pos
            if coh.length() > 0:
                coh.normalize_ip()
                self.accel += coh * COHESION_FORCE

    def locate_in_grid(self, grid):
        cell_x = int(self.pos.x // CELL_SIZE) % grid.num_rows
        cell_y = int(self.pos.y // CELL_SIZE) % grid.num_cols
        grid.cells[(cell_x, cell_y)].append(self)
        return cell_x, cell_y  