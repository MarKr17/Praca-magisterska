import pygame
from Visualisation.Constants import (grid_background, GRID_SIZE, GRID_POS,
                                     virus_color)
from Visualisation.Gradients import (neuron_gradient, myelin_gradient,
                                     t_gradient, b_gradient)
from Agents.T_cell import T_cell
from Agents.B_cell import B_cell
from Agents.Neuron import Neuron
from Agents.Virus import Virus


def drawAgents(self):
    self.grid.fill(grid_background)
    self.drawGrid()
    self.drawCytokine()
    self.drawBarrier()
    for (cell_contents, x, y) in self.model.grid.coord_iter():
        radius = GRID_SIZE/self.size/2 - 5
        X = x*GRID_SIZE/self.size+GRID_SIZE/self.size/2
        Y = y*GRID_SIZE/self.size+GRID_SIZE/self.size/2
        for a in cell_contents:
            if type(a) is Neuron:
                surf = drawNeuron(radius, a)
            elif type(a) is T_cell:
                surf = drawT_cell(radius, a)
            elif type(a) is B_cell:
                surf = drawB_cell(radius, a)
            elif type(a) is Virus:
                surf = drawVirus(radius/2, a)
            rect = surf.get_rect()
            rect.centerx = int(X)
            rect.centery = int(Y)
            self.grid.blit(surf, rect)
    self.screen.blit(self.grid, GRID_POS)


def drawNeuron(radius, neuron):
    i = int(neuron.health-1)
    n_color = neuron_gradient[i]
    i = int(neuron.myelin_health-1)
    m_color = myelin_gradient[i]
    outer = radius+neuron.myelin_health
    surf = pygame.Surface((2*outer, 2*outer), pygame.SRCALPHA, 32)
    pygame.draw.circle(surf, m_color, (outer, outer), outer)
    pygame.draw.circle(surf, n_color, (outer, outer), radius)
    return surf


def drawT_cell(radius, Cell):
    i = int(Cell.health/2-1)
    color = t_gradient[i]
    surf = pygame.Surface((2*radius, 2*radius),
                          pygame.SRCALPHA, 32)
    pygame.draw.circle(surf, color, (radius, radius), radius)
    return surf


def drawB_cell(radius, Cell):
    i = int(Cell.health/2-1)
    color = b_gradient[i]
    surf = pygame.Surface((2*radius, 2*radius),
                          pygame.SRCALPHA, 32)
    pygame.draw.circle(surf, color, (radius, radius), radius)
    return surf


def drawVirus(radius, Virus):
    surf = pygame.Surface((2*radius, 2*radius),
                          pygame.SRCALPHA, 32)
    pygame.draw.circle(surf, virus_color, (radius, radius), radius)
    return surf
