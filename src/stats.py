import pygame
from src.config import (NUM_BOIDS, SEPERATION_FORCE, ALIGNEMENT_FORCE, COHESION_FORCE, DETECTION_LIMIT, LIGHT_BLUE, FONT_SYTLE, FONT_SIZE)

class Stats:
    def __init__(self, screen, clock):
        self.clock = clock
        self.screen = screen
        self.font = pygame.font.SysFont(FONT_SYTLE, FONT_SIZE)

    def fps_tracker(self):
        fps_text = str(int(self.clock.get_fps()))
        fps_surface = self.font.render(f"FPS: {fps_text}", True, LIGHT_BLUE)
        self.screen.blit(fps_surface, (10, 10)) 

    def boid_information(self):
        num_boid_text = str(NUM_BOIDS)
        sep_text = str(SEPERATION_FORCE)
        align_text = str(ALIGNEMENT_FORCE)
        coh_text = str(COHESION_FORCE)
        detect_text = str(DETECTION_LIMIT)

        num_boid_surface = self.font.render(f"Entities: {num_boid_text}", True, LIGHT_BLUE)
        sep_surface = self.font.render(f"Seperation: {sep_text}", True, LIGHT_BLUE)
        align_surface = self.font.render(f"Alignement: {align_text}", True, LIGHT_BLUE)
        coh_surface = self.font.render(f"Cohesion: {coh_text}", True, LIGHT_BLUE)
        detect_surface = self.font.render(f"Detection Limit: {detect_text}", True, LIGHT_BLUE)

        self.screen.blit(num_boid_surface, (10, 30))
        self.screen.blit(sep_surface, (10, 50))
        self.screen.blit(align_surface, (10, 70))
        self.screen.blit(coh_surface, (10, 90))
        self.screen.blit(detect_surface, (10, 110)) 
