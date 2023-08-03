import pygame
import os
import math
from Neuron import Neuron
from drawLegend import drawLegend
colorb = (250, 0, 0)
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 1000
GRID_SIZE = 900
GRID_POS = (50, 20)
WHITE = (250, 250, 250)
BLACK = (0, 0, 0)
assets_path = os.path.join(os.getcwd(), "assets")
GREY = (204, 191, 190)
grid_background = "#F4F1DE"
t_color = "#3D405B"
m_color = "#F2CC8F"
n_color = "#C1292E"
t_gradient = [
    "#97798f",
    "#815b79",
    "#693d65",
    "#522052",
    "#390040"
]
cytokine_gradient = [
    "#e4e6d4",
    "#d5dacb",
    "#c7cfc2",
    "#bac3b9",
    "#adb7b0",
    "#a2aba6",
    "#97a09c",
    "#8d9492",
    "#838888",
    "#7a7d7d"
]


class Button():
    def __init__(self, screen, color, width, height, pos):
        self.screen = screen,
        self.color = color,
        self.width = width
        self.height = height
        self.surf = pygame.Surface((width, height), pygame.SRCALPHA, 32)
        self.pos = pos
        self.x = pos[0], pos[0]+width
        self.y = pos[1], pos[1]+height

    def draw(self, PAUSE):
        # pygame.draw.rect(self.surf, self.color, self.surf.get_rect() )
        if PAUSE:
            image = pygame.image.load(os.path.join(assets_path,
                                                   "play_button.png"))
        else:
            image = pygame.image.load(os.path.join(assets_path,
                                                   "pause_button.png"))

        image = pygame.transform.scale(image, (self.width, self.height))
        self.screen[0].blit(image, self.pos)


def drawGrid(screen, size):
    blockSize = int(GRID_SIZE/size)  # Set the size of the grid block
    for x in range(0, GRID_SIZE, blockSize):
        for y in range(0, GRID_SIZE, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, GREY, rect, 1)


def drawNeuron(radius, neuron):
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
                pygame.draw.rect(s, GREY, rect, 1)
                grid.blit(s, (X, Y))


def draw_agents(grid, model, screen, size):
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


def visualisation(model):
    size = model.width
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill("black")  # Fill the display with a solid color
    clock = pygame.time.Clock()
    grid = pygame.Surface((GRID_SIZE, GRID_SIZE))
    grid.fill(grid_background)
    drawGrid(grid, size)
    screen.blit(grid, GRID_POS)
    drawLegend(screen, t_gradient, cytokine_gradient)
    PAUSE = False
    RUNNING = True
    pygame.display.set_caption('MS model')
    while RUNNING:
        # Process inputs
        mouse = pygame.mouse.get_pos()
        button = Button(screen, colorb, 50, 50, (400, 930))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (button.x[0] <= mouse[0] <= button.x[1] and button.y[0] <=
                        mouse[1] <= button.y[1]):
                    PAUSE = not PAUSE
        if not PAUSE:
            draw_agents(grid, model, screen, size)
            model.step()
        button.draw(PAUSE)
        pygame.display.flip()  # Refresh on-screen display
        clock.tick(24)         # wait until next frame (at 24 FPS)
