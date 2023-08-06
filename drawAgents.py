import pygame
from Constants import (grid_background, GRID_SIZE, GRID_POS)
from Gradients import (neuron_gradient, myelin_gradient, t_gradient,
                       b_gradient)
from T_cell import T_cell
from B_cell import B_cell
from drawGrid import drawGrid
from drawGrid import drawCytokine
from drawGrid import drawBarrier
from Neuron import Neuron


def drawAgents(grid, model, screen, size):
    grid.fill(grid_background)
    drawGrid(grid, size)
    drawCytokine(model, size, grid)
    drawBarrier(model, size, grid)
    for (cell_contents, x, y) in model.grid.coord_iter():
        radius = GRID_SIZE/size/2 - 5
        X = x*GRID_SIZE/size+GRID_SIZE/size/2
        Y = y*GRID_SIZE/size+GRID_SIZE/size/2
        for a in cell_contents:
            if type(a) is Neuron:
                surf = drawNeuron(radius, a)
            elif type(a) is T_cell:
                surf = drawT_cell(radius, a)
            elif type(a) is B_cell:
                surf = drawB_cell(radius, a)
            rect = surf.get_rect()
            rect.centerx = int(X)
            rect.centery = int(Y)
            grid.blit(surf, rect)
    screen.blit(grid, GRID_POS)


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
    i = int(Cell.health/5)
    color = t_gradient[i]
    surf = pygame.Surface((2*radius, 2*radius),
                          pygame.SRCALPHA, 32)
    pygame.draw.circle(surf, color, (radius, radius), radius)
    return surf


def drawB_cell(radius, Cell):
    i = int(Cell.health/5)
    color = b_gradient[i]
    surf = pygame.Surface((2*radius, 2*radius),
                          pygame.SRCALPHA, 32)
    pygame.draw.circle(surf, color, (radius, radius), radius)
    return surf
