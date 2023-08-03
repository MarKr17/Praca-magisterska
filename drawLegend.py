import pygame
WHITE = (250, 250, 250)
BLACK = (0, 0, 0)
pygame.font.init()
font_title = pygame.font.SysFont('yugothicui', 24)
font_small = pygame.font.SysFont('yugothicui', 14)
font_medium = pygame.font.SysFont('yugothicui', 18)
t_gradient = [
    "#97798f",
    "#815b79",
    "#693d65",
    "#522052",
    "#390040"
]
cytokine_gradient = [
    "#e4e6d4",
    "#d5dacb",
    "#c7cfc2",
    "#bac3b9",
    "#adb7b0",
    "#a2aba6",
    "#97a09c",
    "#8d9492",
    "#838888",
    "#7a7d7d"
]
neuron_gradient = [
    "#c1292e",
    "#b22531",
    "#a32233",
    "#941f33",
    "#841e33",
    "#751d31",
    "#651c2f",
    "#561b2b",
    "#471927",
    "#381722"
]
myelin_gradient = [
    "#f2cc8f",
    "#e8c68d",
    "#debf8b",
    "#d5b988",
    "#cbb286",
    "#c2ac84",
    "#b9a582",
    "#b09f7f",
    "#a7987d",
    "#9e927b"
]


def drawLegend(screen):
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

    # Create stripe for cytokine gradient
    stripe = drawStripe(cytokine_gradient, h_max=100)
    name = font_medium.render("Cytokinase", True, BLACK)
    surf.blit(name, (25, 130))
    surf.blit(stripe, (25, 150))

    # Crate stripe for myelin gradient
    stripe = drawStripe(neuron_gradient, h_max=10)
    name = font_medium.render("Neuron", True, BLACK)
    surf.blit(name, (25, 210))
    surf.blit(stripe, (25, 230))

    # Crate stripe for neuron gradient
    stripe = drawStripe(myelin_gradient, h_max=10)
    name = font_medium.render("Myelin", True, BLACK)
    surf.blit(name, (25, 280))
    surf.blit(stripe, (25, 300))

    screen.blit(surf, pos)


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
