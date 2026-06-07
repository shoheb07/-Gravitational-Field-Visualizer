import pygame
import numpy as np

pygame.init()

WIDTH = 1000
HEIGHT = 700

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "Gravitational Field Visualizer"
)

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,100,255)

clock = pygame.time.Clock()

# Gravitational Constant (scaled)
G = 5000

# Masses (x, y, mass)
masses = [
    (300, 350, 50),
    (700, 350, 100)
]

running = True

while running:

    screen.fill(WHITE)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    spacing = 30

    # Draw Field Vectors
    for x in range(
        0,
        WIDTH,
        spacing
    ):

        for y in range(
            0,
            HEIGHT,
            spacing
        ):

            Fx = 0
            Fy = 0

            for mx, my, mass in masses:

                dx = mx - x
                dy = my - y

                r = np.sqrt(
                    dx**2 + dy**2
                )

                if r < 20:
                    continue

                F = G * mass / (r**2)

                Fx += F * dx / r
                Fy += F * dy / r

            magnitude = np.sqrt(
                Fx**2 + Fy**2
            )

            if magnitude == 0:
                continue

            Fx /= magnitude
            Fy /= magnitude

            end_x = x + Fx * 12
            end_y = y + Fy * 12

            pygame.draw.line(
                screen,
                BLACK,
                (x, y),
                (end_x, end_y),
                1
            )

    # Draw Masses
    for mx, my, mass in masses:

        radius = int(
            np.sqrt(mass) * 2
        )

        pygame.draw.circle(
            screen,
            BLUE,
            (mx, my),
            radius
        )

    pygame.display.update()

    clock.tick(60)

pygame.quit()
