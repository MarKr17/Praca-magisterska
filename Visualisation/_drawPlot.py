import pygame
import pygame.display
import os
from Plots import Plots

from Visualisation.Constants import (WHITE, BLACK, font_small, font_medium,
                                     font_title, virus_color, APC_color,
                                     t_naive_cell_color)
from Visualisation.Gradients import (b_gradient, cytokine_gradient,
                                     neuron_gradient, myelin_gradient)
pygame.font.init()
folder_path = os.path.join(os.getcwd(), "test")
filepath = os.path.join(folder_path, "realtime.png")


def drawPlot(self):
    plots = Plots(self.model.datacollector)
    raw_data, size = plots.Plot_realtime()

    pos = (1400, 20)
    surf = pygame.Surface((450, 350))
    surf.fill(WHITE)

    # Add title text
    text = font_title.render('Population plot', True, BLACK)
    textRect = text.get_rect()
    textRect.center = (175, 30)
    surf.blit(text, textRect)

    # Loading image
    #imp = pygame.image.load(filepath).convert()
    #imp = pygame.transform.smoothscale_by(imp, 0.2)
    #surf.blit(imp, (50, 50))

    # Drawing plot
    s = pygame.image.fromstring(raw_data, size, "RGB")
    s = pygame.transform.smoothscale_by(s, 0.6)
    surf.blit(s, (50, 50))

    self.screen.blit(surf, pos)
