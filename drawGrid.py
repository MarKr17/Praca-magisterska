import pygame
import math
from Constants import (GRID_SIZE, GREY, m_color, grid_border)
from Gradients import cytokine_gradient


def drawGrid(screen, size):
    blockSize = int(GRID_SIZE/size)  # Set the size of the grid block
    for x in range(0, GRID_SIZE, blockSize):
        for y in range(0, GRID_SIZE, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, GREY, rect, grid_border)


def drawCytokine(model, size, grid):
    a = GRID_SIZE/size
    for x in range(size):
        for y in range(size):
            X = x*GRID_SIZE/size
            Y = y*GRID_SIZE/size
            if model.areas[x][y] == 1:
                s = pygame.Surface((a, a), pygame.SRCALPHA)   # per-pixel alpha
                s.fill(m_color)
                grid.blit(s, (X, Y))
            if model.cytokine_matrix[x][y] > 0:
                if model.cytokine_matrix[x][y] > 100:
                    color = cytokine_gradient[9]
                else:
                    c = math.floor(model.cytokine_matrix[x][y]/10)
                    color = cytokine_gradient[c]
                s = pygame.Surface((a, a), pygame.SRCALPHA)   # per-pixel alpha
                s.fill(color)
                rect = s.get_rect()
                pygame.draw.rect(s, GREY, rect, grid_border)
                grid.blit(s, (X, Y))
