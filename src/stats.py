import pygame
from config import (
    NUM_BOIDS, 
    SEPERATION_FORCE, 
    ALIGNEMENT_FORCE, 
    COHESION_FORCE, 
    DETECTION_LIMIT, 
    LIGHT_BLUE, 
    FONT_SYTLE, 
    FONT_SIZE
)

class Stats:
    def __init__(self, screen, clock):
        self.clock = clock
        self.screen = screen
        self.font = pygame.font.SysFont(FONT_SYTLE, FONT_SIZE)

    def fps_tracker(self):
        fps_text = str(int(self.clock.get_fps()))
        fps_surface = self.font.render(f"FPS: {fps_text}", True, LIGHT_BLUE)
        self.screen.blit(fps_surface, (10, 10)) 

    def display_info(self):
        info = {
            "Entities": str(NUM_BOIDS),
            "Separation": str(SEPERATION_FORCE),
            "Alignement": str(ALIGNEMENT_FORCE),
            "Cohesion": str(COHESION_FORCE),
            "Detection": str(DETECTION_LIMIT)
        }

        spacing = 20
        for i, (key, value) in enumerate(info.items()):
            text_surface = self.font.render(f"{key}: {value}", True, LIGHT_BLUE)
            self.screen.blit(text_surface, (10, 10 + (spacing * i)))