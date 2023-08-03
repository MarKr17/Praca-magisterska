import pygame
from drawGrid import drawGrid
from drawGrid import drawCytokine
from Neuron import Neuron
GRID_SIZE = 900
GRID_POS = (50, 20)
grid_background = "#F4F1DE"
t_gradient = [
    "#97798f",
    "#815b79",
    "#693d65",
    "#522052",
    "#390040"
]

neuron_gradient = [
    "#c1292e",
    "#b22531",
    "#a32233",
    "#941f33",
    "#841e33",
    "#751d31",
    "#651c2f",
    "#561b2b",
    "#471927",
    "#381722"
]
myelin_gradient = [
    "#f2cc8f",
    "#e8c68d",
    "#debf8b",
    "#d5b988",
    "#cbb286",
    "#c2ac84",
    "#b9a582",
    "#b09f7f",
    "#a7987d",
    "#9e927b"
]


def drawAgents(grid, model, screen, size):
    grid.fill(grid_background)
    drawGrid(grid, size)
    drawCytokine(model, size, grid)
    for (cell_contents, x, y) in model.grid.coord_iter():
        radius = GRID_SIZE/size/2 - 5
        X = x*GRID_SIZE/size+GRID_SIZE/size/2
        Y = y*GRID_SIZE/size+GRID_SIZE/size/2
        for a in cell_contents:
            if type(a) is Neuron:
                surf = drawNeuron(radius, a)
            else:
                surf = drawLympcocyteT(radius, a)
            rect = surf.get_rect()
            rect.centerx = int(X)
            rect.centery = int(Y)
            grid.blit(surf, rect)
    screen.blit(grid, GRID_POS)


def drawNeuron(radius, neuron):
    i = int(neuron.health/10)
    n_color = neuron_gradient[i]
    i = int(neuron.myelin_health/10)
    m_color = myelin_gradient[i]
    outer = radius+neuron.myelin_health
    surf = pygame.Surface((2*outer, 2*outer), pygame.SRCALPHA, 32)
    pygame.draw.circle(surf, m_color, (outer, outer), outer)
    pygame.draw.circle(surf, n_color, (outer, outer), radius)
    return surf


def drawLympcocyteT(radius, lymphocyte):
    i = int(lymphocyte.health/5)
    color = t_gradient[i]
    surf = pygame.Surface((2*radius, 2*radius),
                          pygame.SRCALPHA, 32)
    pygame.draw.circle(surf, color, (radius, radius), radius)
    return surf
