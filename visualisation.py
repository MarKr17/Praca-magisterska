import pygame
import os
colorb = (250, 0, 0)
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 1000
GRID_SIZE = 800
WHITE = (200, 200, 200)
BLACK = (0, 0, 0)
assets_path = os.path.join(os.getcwd(), "assets")


class Button():
    def __init__(self, screen, color, width, height):
        self.screen = screen,
        self.color = color,
        self.width = width
        self.height = height
        self.surf = pygame.Surface((width, height), pygame.SRCALPHA, 32)
        self.x = 400, 400+width
        self.y = 900, 900+height

    def draw(self, PAUSE):
        # pygame.draw.rect(self.surf, self.color, self.surf.get_rect() )
        print(PAUSE)
        if PAUSE:
            image = pygame.image.load(os.path.join(assets_path,
                                                   "play_button.png"))
        else:
            image = pygame.image.load(os.path.join(assets_path,
                                                   "pause_button.png"))

        image = pygame.transform.scale(image, (self.width, self.height))
        self.screen[0].blit(image, (400, 900))


def drawGrid(screen):
    blockSize = int(GRID_SIZE/10)  # Set the size of the grid block
    for x in range(0, GRID_SIZE, blockSize):
        for y in range(0, GRID_SIZE, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, BLACK, rect, 1)


def draw_agents(grid, model, screen, size):
    color = "#ff0000"
    for (cell_contents, x, y) in model.grid.coord_iter():
        x = x*GRID_SIZE/10+GRID_SIZE/20
        y = y*GRID_SIZE/10+GRID_SIZE/20
        for a in cell_contents:
            surf = pygame.Surface((2*size, 2*size), pygame.SRCALPHA, 32)
            pygame.draw.circle(surf, color, (size, size), size)
            rect = surf.get_rect()
            rect.centerx = int(x)
            rect.centery = int(y)
            grid.blit(surf, rect)
    screen.blit(grid, (300, 20))
    grid.fill("white")
    drawGrid(grid)


def visualisation(model):
    size = model.width
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill("black")  # Fill the display with a solid color
    clock = pygame.time.Clock()
    grid = pygame.Surface((GRID_SIZE, GRID_SIZE))
    grid.fill("white")
    drawGrid(grid)
    screen.blit(grid, (300, 20))

    PAUSE = False
    RUNNING = True

    while RUNNING:
        # Process inputs
        mouse = pygame.mouse.get_pos()
        button = Button(screen, colorb, 50, 50)
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
