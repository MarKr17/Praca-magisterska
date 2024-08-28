import pygame
from Agents.Plasma_cell import Plasma_cell
from Visualisation.Constants import (Th0_color, Th1_color, Th2_color, Th_color,
                                     Tpato17_color, Treg17_color,
                                     grid_background, GRID_POS,
                                     virus_color, APC_color,
                                     t_naive_cell_color, Plasma_color,
                                     B_cells_color)
from Visualisation.Gradients import (neuron_gradient, myelin_gradient)
from Agents.T_naive_cell import T_naive_cell
from Agents.B_cell import B_cell
from Agents.Neuron import Neuron
from Agents.Virus import Virus
from Agents.APC import APC
from Agents.Th_cell import Th_cell
from Agents.Th0 import Th0
from Agents.Th1 import Th1
from Agents.Th2 import Th2
from Agents.Tpato17 import Tpato17
from Agents.Treg17 import Treg17


def drawAgents(self, GRID_SIZE):
    self.grid.fill(grid_background)
    self.drawGrid(GRID_SIZE)
    self.drawCytokine(GRID_SIZE)
    self.drawBarrier(GRID_SIZE)
    for (cell_contents, x, y) in self.model.grid.coord_iter():
        radius = GRID_SIZE/self.size/2 - 5
        radius2 = radius * 0.8
        X = x*GRID_SIZE/self.size+GRID_SIZE/self.size/2
        Y = y*GRID_SIZE/self.size+GRID_SIZE/self.size/2
        for a in cell_contents:
            if type(a) is Neuron:
                surf = drawNeuron(radius, a)
            elif type(a) is T_naive_cell:
                surf = drawT_naive_cell(radius2)
            elif type(a) is B_cell:
                surf = drawB_cell(radius)
            elif type(a) is Virus:
                surf = drawVirus(radius/2)
            elif type(a) is APC:
                surf = drawAPC(radius)
            elif type(a) is Plasma_cell:
                surf = drawPlasma(radius)
            elif type(a) is Th_cell:
                surf = drawTh_cell(radius2)
            elif type(a) is Th0:
                surf = drawTh0(radius2)
            elif type(a) is Th1:
                surf = drawTh1(radius2)
            elif type(a) is Th2:
                surf = drawTh2(radius2)
            elif type(a) is Tpato17:
                surf = drawTpato17(radius2)
            elif type(a) is Treg17:
                surf = drawTreg17(radius2)

            rect = surf.get_rect()
            rect.centerx = int(X)
            rect.centery = int(Y)
            self.grid.blit(surf, rect)
    self.screen.blit(self.grid, GRID_POS)


def drawNeuron(radius, neuron):
    i = int(neuron.health)-1
    n_color = neuron_gradient[i]
    i = int(neuron.current_myelin_health/10)-1
    m_color = myelin_gradient[i]
    outer = radius+int(neuron.current_myelin_health/10)
    surf = pygame.Surface((2*outer, 2*outer), pygame.SRCALPHA, 32)
    pygame.draw.circle(surf, m_color, (outer, outer), outer)
    pygame.draw.circle(surf, n_color, (outer, outer), radius)
    return surf


def drawT_naive_cell(radius):
    surf = pygame.Surface((2*radius, 2*radius),
                          pygame.SRCALPHA, 32)
    pygame.draw.circle(surf, t_naive_cell_color, (radius, radius), radius)
    return surf


def drawB_cell(radius):
    surf = pygame.Surface((2*radius, 2*radius),
                          pygame.SRCALPHA, 32)
    pygame.draw.circle(surf, B_cells_color, (radius, radius), radius)
    return surf


def drawVirus(radius):
    surf = pygame.Surface((2*radius, 2*radius),
                          pygame.SRCALPHA, 32)
    pygame.draw.circle(surf, virus_color, (radius, radius), radius)
    return surf


def drawAPC(radius):
    surf = pygame.Surface((2*radius, 2*radius),
                          pygame.SRCALPHA, 32)
    pygame.draw.circle(surf, APC_color, (radius, radius), radius)
    return surf


def drawPlasma(radius):
    surf = pygame.Surface((2*radius, 2*radius),
                          pygame.SRCALPHA, 32)
    pygame.draw.circle(surf, Plasma_color, (radius, radius), radius)
    return surf


def drawTh_cell(radius):
    surf = pygame.Surface((2*radius, 2*radius),
                          pygame.SRCALPHA, 32)
    pygame.draw.circle(surf, Th_color, (radius, radius), radius)
    return surf


def drawTh0(radius):
    surf = pygame.Surface((2*radius, 2*radius),
                          pygame.SRCALPHA, 32)
    pygame.draw.circle(surf, Th0_color, (radius, radius), radius)
    return surf


def drawTh1(radius):
    surf = pygame.Surface((2*radius, 2*radius),
                          pygame.SRCALPHA, 32)
    pygame.draw.circle(surf, Th1_color, (radius, radius), radius)
    return surf


def drawTh2(radius):
    surf = pygame.Surface((2*radius, 2*radius),
                          pygame.SRCALPHA, 32)
    pygame.draw.circle(surf, Th2_color, (radius, radius), radius)
    return surf


def drawTpato17(radius):
    surf = pygame.Surface((2*radius, 2*radius),
                          pygame.SRCALPHA, 32)
    pygame.draw.circle(surf, Tpato17_color, (radius, radius), radius)
    return surf


def drawTreg17(radius):
    surf = pygame.Surface((2*radius, 2*radius),
                          pygame.SRCALPHA, 32)
    pygame.draw.circle(surf, Treg17_color, (radius, radius), radius)
    return surf
