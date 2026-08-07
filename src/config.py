# Dimensions
WIDTH, HEIGHT = 2000, 1000

# Physics / Boid forces
NUM_BOIDS = 1000
BOIDS_SPEED = 1
MAX_ACCELERATION = 2
FRICTION = 0.85
DETECTION_LIMIT = 50

SEPERATION_FORCE = 1.2
ALIGNEMENT_FORCE = 1.1
COHESION_FORCE = 0.8

# Grid
CELL_SIZE = DETECTION_LIMIT
CELL_BORDER = 1
NEIGHBOR_CELLS = [[(-1, -1), (0, -1), (1, -1)],
                  [(-1, 0), (0, 0), (1, 0)],
                  [(-1, 1), (0, 1), (1, 1)]]

# Displays
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DEEP_SLATE_GREY = (48, 50, 52)
LIGHT_BLUE = (173, 216, 230)

FONT_SYTLE = "Arial"
FONT_SIZE = 12