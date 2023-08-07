import pygame
from Visualisation.Constants import (WHITE, BLACK, font_small, font_medium,
                                     font_title)
from Visualisation.Gradients import (t_gradient, b_gradient, cytokine_gradient,
                                     neuron_gradient, myelin_gradient)
pygame.font.init()


def drawLegend(self):
    pos = (1000, 20)
    surf = pygame.Surface((350, 900))
    surf.fill(WHITE)

    # Add title text
    text = font_title.render('Legend', True, BLACK)
    textRect = text.get_rect()
    textRect.center = (175, 30)
    surf.blit(text, textRect)

    # Create stripe for gradient of t cells
    stripe = drawStripe(t_gradient, h_max=20)
    name = font_medium.render("T-cells", True, BLACK)
    surf.blit(name, (25, 50))
    surf.blit(stripe, (25, 70))

    # Create stripe for gradient of b-cells
    stripe = drawStripe(b_gradient, h_max=20)
    name = font_medium.render("B-cells", True, BLACK)
    surf.blit(name, (25, 130))
    surf.blit(stripe, (25, 150))

    # Create stripe for cytokine gradient
    stripe = drawStripe(cytokine_gradient, h_max=100)
    name = font_medium.render("Cytokinase", True, BLACK)
    surf.blit(name, (25, 210))
    surf.blit(stripe, (25, 230))

    # Crate stripe for myelin gradient
    stripe = drawStripe(neuron_gradient, h_max=10)
    name = font_medium.render("Neuron", True, BLACK)
    surf.blit(name, (25, 290))
    surf.blit(stripe, (25, 310))

    # Crate stripe for neuron gradient
    stripe = drawStripe(myelin_gradient, h_max=10)
    name = font_medium.render("Myelin", True, BLACK)
    surf.blit(name, (25, 370))
    surf.blit(stripe, (25, 390))

    self.screen.blit(surf, pos)


def drawStripe(gradient_matrix, h_max):
    x = 0
    h = 1
    width = 300/len(gradient_matrix)
    gradient = pygame.Surface((300, 20))
    annotations = pygame.Surface((300, 20))
    stripe = pygame.Surface((300, 40))
    for i in range(len(gradient_matrix)):
        # creating smaller surfaces for speciffic colors
        g = pygame.Surface((width, 20))
        g.fill(gradient_matrix[i])
        gradient.blit(g, (x, 0))
        # Creating annotations
        st = pygame.Surface((width, 20))
        st.fill(WHITE)
        t = font_small.render("{}".format(h), True, BLACK)
        t_rect = t.get_rect()
        st.blit(t, t_rect)
        annotations.blit(st, (x, 0))
        h += h_max//len(gradient_matrix)
        x += width
    stripe.blit(gradient, (0, 0))
    stripe.blit(annotations, (0, 20))
    return stripe
