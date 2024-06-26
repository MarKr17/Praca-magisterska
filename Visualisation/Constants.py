import os
import pygame
GRID_POS = (50, 20)
WHITE = (250, 250, 250)
BLACK = (0, 0, 0)
assets_path = os.path.join(os.getcwd(), "_assets")
GREY = "#D6D7D7"
grid_background = WHITE

m_color = "#F2CC8F"
n_color = "#C1292E"
virus_color = "#50723C"  # "#358600"


APC_color = "#CE8147"

Plasma_color = "#DB3069"
B_cells_color = "#AE1E4E"

t_naive_cell_color = "#D114A7"
Tpato17_color = "#AD0A9B"
Treg17_color = "#88008F"


Th_color = "#4EA9D0"
Th0_color = "#4696BA"
Th1_color = "#35708C"
Th2_color = "#2c5c75"


grid_border = 1
barrier_color = "#F3D9A5"
pygame.font.init()
font_title = pygame.font.SysFont('yugothicui', 24)
font_small = pygame.font.SysFont('yugothicui', 14)
font_medium = pygame.font.SysFont('yugothicui', 18)
