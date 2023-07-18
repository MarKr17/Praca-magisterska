import pygame
colorb=(250,0,0)
class Button():
    def __init__(self, screen, color, width, height):
        self.screen = screen,
        self.color = color,
        self.width = width
        self.height = height
        self.surf = pygame.Surface((height, width), pygame.SRCALPHA, 32)
    def draw(self):
        pygame.draw.rect(self.surf, self.color, self.surf.get_rect() )

def visualisation(model):
    SCREEN_WIDTH = 1400
    SCREEN_HEIGHT = 1000
    GRID_WIDTH = 1200
    GRID_HEIGHT = 700
    size = 10
    color = "#ff0000"
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    while True:
    # Process inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        
        screen.fill("black")  # Fill the display with a solid color
        button = Button(screen, colorb, 200, 100)
        button.draw()

        #drawing agents
        for (cell_contents, x,y) in model.grid.coord_iter():
            x=x*SCREEN_WIDTH/10+50
            y=y*SCREEN_HEIGHT/10+50
            for a in cell_contents:
                surf = pygame.Surface((2*size, 2*size), pygame.SRCALPHA, 32)
                pygame.draw.circle(surf, color, (size, size), size)
                rect = surf.get_rect()
                rect.centerx = int(x)
                rect.centery = int(y)
                screen.blit(surf, rect)
        pygame.display.flip()  # Refresh on-screen display
        clock.tick(24)         # wait until next frame (at 24 FPS)
        model.step()


    