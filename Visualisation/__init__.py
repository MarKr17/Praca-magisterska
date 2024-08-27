import pygame
import pygame_widgets
from Visualisation.Constants import (grid_background, GREY)
from Visualisation.Controls import Controls
import os


def closestNumber(n, m):
    # Find the quotient
    q = int(n / m)

    # 1st possible closest number
    n1 = m * q

    # 2nd possible closest number
    if ((n * m) > 0):
        n2 = (m * (q + 1))
    else:
        n2 = (m * (q - 1))

    # if true, then n1 is the required closest number
    if (abs(n - n1) < abs(n - n2)):
        return n1

    # else n2 is the required closest number
    return n2


class Visualisation():
    def __init__(self, model):
        self.model = model
        self.size = model.size
        self.screenshot_count = 1
        pygame.init()
        self.infoObject = pygame.display.Info()
        self.screen = pygame.display.set_mode((self.infoObject.current_w*0.99,
                                               self.infoObject.current_h*0.95),
                                              pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.GRID_SIZE = min(self.infoObject.current_h,
                             self.infoObject.current_w)
        self.GRID_SIZE = int(self.GRID_SIZE*0.83)
        self.GRID_SIZE = closestNumber(self.GRID_SIZE, self.size)
        self.grid = pygame.Surface((self.GRID_SIZE, self.GRID_SIZE))
        self.LEGEND_SIZE = (self.GRID_SIZE/2, self.GRID_SIZE)
        self.PAUSE = True
        self.RUNNING = True

    from ._drawAgents import drawAgents
    from ._drawGrid import (drawGrid, drawCytokine, drawBarrier)
    from ._drawLegend import drawLegend

    def run(self):
        self.clock = pygame.time.Clock()
        self.grid.fill(grid_background)
        self.drawGrid(self.GRID_SIZE)
        # self.drawCytokine(self.GRID_SIZE)
        self.screen.blit(self.grid, (0, 0))
        self.controls = Controls(self.screen, self.GRID_SIZE,
                                 self.GRID_SIZE/10,
                                 (50, self.GRID_SIZE +
                                  int(self.GRID_SIZE/35)),
                                 self.PAUSE)
        pygame.display.set_caption('MS model')
        while self.RUNNING:
            PAUSE = self.controls.PAUSE
            self.drawLegend(self.LEGEND_SIZE)
            self.drawAgents(self.GRID_SIZE)
            self.drawGrid(self.GRID_SIZE)
            self.controls.draw(self.model.schedule.steps)
            # Process inputs
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.RUNNING = False
                if event.type == pygame.VIDEORESIZE:
                    width, height = event.size
                    if width < 1000 or height < 500:
                        if width < 1000:
                            width = 1000
                        if height < 600:
                            height = 600
                        self.screen = pygame.display.set_mode((width, height),
                                                              pygame.RESIZABLE)
                    y = self.controls.pos[1]
                    self.infoObject = pygame.display.Info()
                    self.GRID_SIZE = min(self.infoObject.current_h,
                                         self.infoObject.current_w)
                    self.GRID_SIZE = int(self.GRID_SIZE*0.83)
                    self.GRID_SIZE = closestNumber(self.GRID_SIZE, self.size)
                    self.grid = pygame.Surface((self.GRID_SIZE,
                                                self.GRID_SIZE))
                    self.LEGEND_SIZE = (self.GRID_SIZE/2, self.GRID_SIZE)
                    self.controls.width = self.GRID_SIZE
                    self.controls.height = self.GRID_SIZE/10
                    self.controls.pos = (50, self.GRID_SIZE +
                                         int(self.GRID_SIZE/35))
                    y = self.controls.pos[1] - y
                    self.controls.button.moveY(y)
                    self.controls.slider.moveY(y)
                    self.controls.dropdown.moveY(y)
                    self.controls.button.setHeight(int(self.controls.height/2))
                    self.controls.button.setWidth(int(self.controls.height/2))
            if not PAUSE:
                self.model.step()
            if self.model.schedule.steps > 0:
                self.controls.dropdown.disable()
            elif self.controls.dropdown.getSelected():
                self.model.hypothesis = self.controls.dropdown.getSelected()
            if self.model.step() % 100 == 0:
                folder = os.path.join("test", self.model.hypothesis)
                if not os.path.exists(folder):
                    os.makedirs(folder)
                filename = "screenshot" + str(self.screenshot_count) + ".jpg"
                file_path = os.path.join(self.folder, filename)
                pygame.image.save(self.screen, file_path)
                self.screenshot_count += 1
            pygame.display.flip()  # Refresh on-screen display
            self.clock.tick(self.controls.slider.getValue())
            self.screen.fill(GREY)  # Fill the display with a solid color
            pygame_widgets.update(events)
