import pygame
import math
from Visualisation.Constants import (GREY, barrier_color,
                                     grid_border)
from Visualisation.Gradients import cytokine_gradient


def drawGrid(self, GRID_SIZE):
    blockSize = int(GRID_SIZE/self.size)  # Set the size of the grid block
    for x in range(0, GRID_SIZE, blockSize):
        for y in range(0, GRID_SIZE, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(self.grid, GREY, rect, grid_border)


def drawCytokine(self, GRID_SIZE):
    a = GRID_SIZE/self.size
    for x in range(self.size):
        for y in range(self.size):
            X = x*GRID_SIZE/self.size
            Y = y*GRID_SIZE/self.size
            if self.model.cytokin_matrix[x][y] > 0:
                if self.model.cytokin_matrix[x][y] > 100:
                    color = cytokine_gradient[9]
                else:
                    c = math.floor(self.model.cytokin_matrix[x][y]/10)
                    color = cytokine_gradient[c]
                s = pygame.Surface((a, a), pygame.SRCALPHA)   # per-pixel alpha
                s.fill(color)
                rect = s.get_rect()
                pygame.draw.rect(s, GREY, rect, grid_border)
                self.grid.blit(s, (X, Y))


def drawBarrier(self, GRID_SIZE):
    a = GRID_SIZE/self.size
    for x in range(self.size):
        for y in range(self.size):
            X = x*GRID_SIZE/self.size
            Y = y*GRID_SIZE/self.size
            if self.model.areas[x][y] == 1:
                s = pygame.Surface((a, a), pygame.SRCALPHA)   # per-pixel alpha
                s.fill(barrier_color)
                rect = s.get_rect()
                pygame.draw.rect(s, GREY, rect, grid_border)
                self.grid.blit(s, (X, Y))
