from model import MoneyModel
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pygame
model = MoneyModel(100, 10, 10)

SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 1000
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

    #drawing agents
    for (cell_contents, x,y) in model.grid.coord_iter():
        x=x*SCREEN_WIDTH/10
        y=y*SCREEN_HEIGHT/10
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

    

