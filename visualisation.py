import pygame
import os
from drawGrid import drawGrid
from drawLegend import drawLegend
from drawAgents import drawAgents
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
    drawLegend(screen)
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
            drawAgents(grid, model, screen, size)
            model.step()
        button.draw(PAUSE)
        pygame.display.flip()  # Refresh on-screen display
        clock.tick(24)         # wait until next frame (at 24 FPS)
