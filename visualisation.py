import pygame
import pygame_widgets
from Constants import (SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE,
                       grid_background, GRID_POS, GREY)
from drawGrid import drawGrid
from drawLegend import drawLegend
from drawAgents import drawAgents
from Controls import Controls


def visualisation(model):
    size = model.width
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    grid = pygame.Surface((GRID_SIZE, GRID_SIZE))
    grid.fill(grid_background)
    drawGrid(grid, size)
    screen.blit(grid, GRID_POS)
    PAUSE = False
    RUNNING = True
    controls = Controls(screen, 900, 100, (50, 930), PAUSE)
    pygame.display.set_caption('MS model')
    while RUNNING:
        PAUSE = controls.PAUSE
        drawLegend(screen)
        drawAgents(grid, model, screen, size)
        controls.draw()
        # Process inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        if not PAUSE:
            model.step()
        pygame_widgets.update(event)
        pygame.display.flip()  # Refresh on-screen display
        clock.tick(controls.slider.getValue())
        screen.fill(GREY)  # Fill the display with a solid color
