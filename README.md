# Boids Simulation

A real-time flocking simulation built with Python and Pygame, implementing Craig
Reynolds' classic [boids](https://en.wikipedia.org/wiki/Boids) model.

Each boid follows three simple steering rules that, together, produce emergent
flocking behaviour:

- **Separation** - steer away from nearby boids to avoid crowding.
- **Alignment** - steer towards the average heading of nearby boids.
- **Cohesion** - steer towards the average position of nearby boids.

Neighbour lookups use a spatial grid, so each boid only checks nearby cells
instead of every other boid. This keeps the simulation fast with thousands of
boids on screen.

## Features

- 1000 boids by default, updated at 30 FPS.
- Spatial-grid neighbour search for efficient collision avoidance.
- Toroidal (wrap-around) world edges.
- Live on-screen stats: entity count, force weights, detection range and FPS.

## Requirements

- Python 3.8+
- [pygame](https://www.pygame.org/) or [pygame-ce](https://pyga.me/)

Install the dependency:

```bash
pip install pygame-ce
```

## Running

From the project root:

```bash
python main.py
```

Close the window to quit.

## Configuration

All tunable values live in `src/config.py`:

| Setting | Description |
| --- | --- |
| `WIDTH`, `HEIGHT` | Window and world size in pixels. |
| `NUM_BOIDS` | Number of boids spawned. |
| `BOIDS_SPEED` | How strongly acceleration translates into velocity. |
| `MAX_ACCELERATION` | Per-frame acceleration cap. |
| `FRICTION` | Velocity damping factor (closer to 1 = less drag). |
| `DETECTION_LIMIT` | Neighbour search radius. |
| `SEPARATION_FORCE` | Weight of the separation rule. |
| `ALIGNMENT_FORCE` | Weight of the alignment rule. |
| `COHESION_FORCE` | Weight of the cohesion rule. |

## Project structure

```
BoidsSimulation/
├── main.py              # Entry point
├── README.md
└── src/
    ├── config.py        # Tunable constants and colours
    ├── boid.py          # Boid state, drawing and steering forces
    ├── grid.py          # Spatial grid for neighbour lookup
    ├── simulation.py    # Main loop: init, update, draw
    └── stats.py         # On-screen statistics overlay
```

## License

See [LICENSE](LICENSE).
