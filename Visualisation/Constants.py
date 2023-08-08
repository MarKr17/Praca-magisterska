import os
import pygame
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 1000
GRID_SIZE = 900
GRID_POS = (50, 20)
WHITE = (250, 250, 250)
BLACK = (0, 0, 0)
assets_path = os.path.join(os.getcwd(), "_assets")
GREY = "#D6D7D7"
grid_background = WHITE
t_color = "#3D405B"
m_color = "#F2CC8F"
n_color = "#C1292E"
virus_color = "#50723C"  # "#358600"
APC_color = "#E8871E"
grid_border = 1
barrier_color = "#F3D9A5"
pygame.font.init()
font_title = pygame.font.SysFont('yugothicui', 24)
font_small = pygame.font.SysFont('yugothicui', 14)
font_medium = pygame.font.SysFont('yugothicui', 18)
