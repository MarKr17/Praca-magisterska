import pygame
import pygame_widgets
import math
from Visualisation.Constants import (grid_background, GRID_POS, GREY,
                                     font_medium, BLACK)
from Visualisation.Controls import Controls


class Visualisation():
    def __init__(self, model):
        self.model = model
        self.size = model.size
        pygame.init()
        infoObject = pygame.display.Info()
        self.screen = pygame.display.set_mode((infoObject.current_w*0.99,
                                               infoObject.current_h*0.95),
                                            pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.GRID_SIZE = math.floor(infoObject.current_h*0.83)
        self.grid = pygame.Surface((self.GRID_SIZE, self.GRID_SIZE))
        self.PAUSE = True
        self.RUNNING = True

    from ._drawAgents import drawAgents
    from ._drawGrid import (drawGrid, drawCytokine, drawBarrier)
    from ._drawLegend import drawLegend

    def run(self):
        self.clock = pygame.time.Clock()
        self.grid.fill(grid_background)
        self.drawGrid(self.GRID_SIZE)
        self.screen.blit(self.grid, GRID_POS)
        controls = Controls(self.screen, 900, 100, (50, 930), self.PAUSE)
        pygame.display.set_caption('MS model')
        while self.RUNNING:
            PAUSE = controls.PAUSE
            self.drawLegend()
            self.drawAgents(self.GRID_SIZE)
            self.drawGrid(self.GRID_SIZE)
            controls.draw()
            text = font_medium.render("Step: {}".format(
                                       self.model.schedule.steps),
                                      True, BLACK)
            textRect = text.get_rect()
            textRect.center = (400, 960)
            self.screen.blit(text, textRect)
            # Process inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.RUNNING = False
            if not PAUSE:
                self.model.step()
            pygame_widgets.update(event)
            pygame.display.flip()  # Refresh on-screen display
            self.clock.tick(controls.slider.getValue())
            self.screen.fill(GREY)  # Fill the display with a solid color
