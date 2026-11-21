import pygame
from src.config import (
    NUM_BOIDS, 
    SEPARATION_FORCE, 
    ALIGNMENT_FORCE, 
    COHESION_FORCE, 
    DETECTION_LIMIT, 
    LIGHT_BLUE, 
    FONT_STYLE, 
    FONT_SIZE
)

class Stats:
    def __init__(self, screen, clock):
        self.clock = clock
        self.screen = screen
        self.font = pygame.font.SysFont(FONT_STYLE, FONT_SIZE)

    def display_info(self):
        info = {
            "Entities": str(NUM_BOIDS),
            "Separation": str(SEPARATION_FORCE),
            "Alignment": str(ALIGNMENT_FORCE),
            "Cohesion": str(COHESION_FORCE),
            "Detection": str(DETECTION_LIMIT),
            "FPS": str(int(self.clock.get_fps()))
        }

        spacing = 20
        for i, (key, value) in enumerate(info.items()):
            text_surface = self.font.render(f"{key}: {value}", True, LIGHT_BLUE)
            self.screen.blit(text_surface, (10, 10 + (spacing * i)))
