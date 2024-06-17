import os
import pygame
GRID_POS = (50, 20)
WHITE = (250, 250, 250)
BLACK = (0, 0, 0)
assets_path = os.path.join(os.getcwd(), "_assets")
GREY = "#D6D7D7"
grid_background = WHITE
t_naive_cell_color = "#bd4089"
m_color = "#F2CC8F"
n_color = "#C1292E"
virus_color = "#50723C"  # "#358600"
APC_color = "#E8871E"
Plasma_color = "#aac0af"
B_cells_color = "#6190bd"
Th_color = "#08415C"
Th0_color = "#93B5C6"
Th1_color = "#D6C3C9"
Th2_color = "#A5D8FF"
Tpato17_color = "#BBE1C3"
Treg17_color = "#324376"
grid_border = 1
barrier_color = "#F3D9A5"
pygame.font.init()
font_title = pygame.font.SysFont('yugothicui', 24)
font_small = pygame.font.SysFont('yugothicui', 14)
font_medium = pygame.font.SysFont('yugothicui', 18)
