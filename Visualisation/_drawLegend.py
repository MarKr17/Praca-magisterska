import pygame
from Visualisation.Constants import (WHITE, BLACK, B_cells_color, Plasma_color,
                                     Th0_color, Th1_color, Th2_color, Th_color,
                                     Tpato17_color, Treg17_color, font_small,
                                     font_medium,
                                     font_title, virus_color, APC_color,
                                     t_naive_cell_color)
from Visualisation.Gradients import (cytokine_gradient,
                                     neuron_gradient, myelin_gradient)
pygame.font.init()


def drawLegend(self, LEGEND_SIZE):
    pos = (LEGEND_SIZE[1]+LEGEND_SIZE[0]/5, 20)
    surf = pygame.Surface(LEGEND_SIZE)
    surf.fill(WHITE)

    # Add title text
    text = font_title.render('Legend', True, BLACK)
    textRect = text.get_rect()
    textRect.center = (LEGEND_SIZE[0]/2, 30)
    surf.blit(text, textRect)
    width = closestNumber(int(LEGEND_SIZE[0]*0.75), 10)
    Cells_dict = {"B_cells": {"B-cell": B_cells_color,
                              "Plasma cell": Plasma_color},
                  "T_cells": {"T-cell": t_naive_cell_color,
                              "Tpato17-cell": Tpato17_color,
                              "Treg17-cell": Treg17_color},
                  "Th_cells": {"Th-cell": Th_color,
                               "Th0-cell": Th0_color,
                               "Th1-cell": Th1_color,
                               "Th2-cell": Th2_color},
                  "Misc_cells": {"APC": APC_color,
                                 "Virus": virus_color}}

    # figuring out the x of the two columns
    xs = [25, int(width/2) + 25]
    n = False
    y = 80
    # drawing cells legend
    for cells in Cells_dict:
        for cell in Cells_dict[cells]:
            s = pygame.Surface((20, 20), pygame.SRCALPHA, 32)
            pygame.draw.circle(s, Cells_dict[cells][cell], (10, 10), 10)
            name = font_medium.render(cell, True, BLACK)
            surf.blit(name, (xs[int(n)], y))
            surf.blit(s, (xs[int(n)] + 100, y))
            if n:
                y += 50
            n = not n
        y += 60
        n = False

    # drawing gradients
    x = 25
    y += 50
    Gradients_dict = {"Cytokinase": drawStripe(cytokine_gradient,
                                               h_max=100, width=width),
                      "Neuron":  drawStripe(neuron_gradient, h_max=10,
                                            width=width),
                      "Myelin": drawStripe(myelin_gradient, h_max=100,
                                           width=width)}

    for g in Gradients_dict:
        name = font_medium.render(g, True, BLACK)
        surf.blit(name, (x, y))
        surf.blit(Gradients_dict[g], (x, y+20))
        y += 80

    self.screen.blit(surf, pos)


def drawStripe(gradient_matrix, h_max, width):
    x = 0
    h = 1

    segment = width/len(gradient_matrix)
    gradient = pygame.Surface((width, 20))
    annotations = pygame.Surface((width, 20))
    stripe = pygame.Surface((width, 40))
    for i in range(len(gradient_matrix)):
        # creating smaller surfaces for speciffic colors
        g = pygame.Surface((segment, 20))
        g.fill(gradient_matrix[i])
        gradient.blit(g, (x, 0))
        # Creating annotations
        st = pygame.Surface((segment, 20))
        st.fill(WHITE)
        t = font_small.render("{}".format(h), True, BLACK)
        t_rect = t.get_rect()
        st.blit(t, t_rect)
        annotations.blit(st, (x, 0))
        h += h_max//len(gradient_matrix)
        x += segment
    stripe.blit(gradient, (0, 0))
    stripe.blit(annotations, (0, 20))
    return stripe


def closestNumber(n, m):
    # Find the quotient
    q = int(n / m)
    # 1st possible closest number
    n1 = m * q
    # 2nd possible closest number
    if ((n * m) > 0):
        n2 = (m * (q + 1))
    else:
        n2 = (m * (q - 1))

    # if true, then n1 is the required closest number
    if (abs(n - n1) < abs(n - n2)):
        return n1

    # else n2 is the required closest number
    return n2
