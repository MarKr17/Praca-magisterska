import pygame
from Visualisation.Constants import (WHITE, BLACK, Plasma_color, font_small,
                                     font_medium,
                                     font_title, virus_color, APC_color,
                                     t_naive_cell_color)
from Visualisation.Gradients import (b_gradient, cytokine_gradient,
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

    # Create legend for t_naive cells
    s = pygame.Surface((20, 20), pygame.SRCALPHA, 32)
    pygame.draw.circle(s, t_naive_cell_color, (10, 10), 10)
    name = font_medium.render("Naive T-cell", True, BLACK)
    surf.blit(name, (25, 50))
    surf.blit(s, (130, 50))

    # Create stripe for gradient of b-cells
    stripe = drawStripe(b_gradient, h_max=20, width=width)
    name = font_medium.render("B-cells", True, BLACK)
    surf.blit(name, (25, 130))
    surf.blit(stripe, (25, 150))

    # Create stripe for cytokine gradient
    stripe = drawStripe(cytokine_gradient, h_max=100, width=width)
    name = font_medium.render("Cytokinase", True, BLACK)
    surf.blit(name, (25, 210))
    surf.blit(stripe, (25, 230))

    # Crate stripe for myelin gradient
    stripe = drawStripe(neuron_gradient, h_max=10, width=width)
    name = font_medium.render("Neuron", True, BLACK)
    surf.blit(name, (25, 290))
    surf.blit(stripe, (25, 310))

    # Crate stripe for neuron gradient
    stripe = drawStripe(myelin_gradient, h_max=10, width=width)
    name = font_medium.render("Myelin", True, BLACK)
    surf.blit(name, (25, 370))
    surf.blit(stripe, (25, 390))

    # Create legend for Virus
    s = pygame.Surface((20, 20), pygame.SRCALPHA, 32)
    pygame.draw.circle(s, virus_color, (10, 10), 10)
    name = font_medium.render("Virus", True, BLACK)
    surf.blit(name, (25, 450))
    surf.blit(s, (80, 450))

    # Create legend for APC
    s = pygame.Surface((20, 20), pygame.SRCALPHA, 32)
    pygame.draw.circle(s, APC_color, (10, 10), 10)
    name = font_medium.render("APC", True, BLACK)
    surf.blit(name, (25, 500))
    surf.blit(s, (80, 500))

    # Create legend for Plasma
    s = pygame.Surface((20, 20), pygame.SRCALPHA, 32)
    pygame.draw.circle(s, Plasma_color, (10, 10), 10)
    name = font_medium.render("Plasma cell", True, BLACK)
    surf.blit(name, (25, 550))
    surf.blit(s, (120, 550))

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
