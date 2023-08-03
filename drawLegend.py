import pygame
WHITE = (250, 250, 250)
BLACK = (0, 0, 0)


def drawLegend(screen, t_gradient):
    pos = (1000, 20)
    surf = pygame.Surface((350, 900))
    surf.fill(WHITE)
    # Add title text
    font_title = pygame.font.SysFont('yugothicui', 24)
    font_small = pygame.font.SysFont('yugothicui', 14)
    text = font_title.render('Legend', True, BLACK)
    textRect = text.get_rect()
    textRect.center = (175, 30)
    surf.blit(text, textRect)
    # Create stripe for gradient of t cells
    stripe = pygame.Surface((300, 20))
    text = pygame.Surface((300, 20))
    x = 0
    h = 0
    width = 300/len(t_gradient)
    for i in range(len(t_gradient)):
        # creating smaller surfaces for speciffic colors
        s = pygame.Surface((width, 20))
        s.fill(t_gradient[i])
        stripe.blit(s, (x, 0))
        
        # Creating annotations
        st = pygame.Surface((width, 20))
        st.fill(WHITE)
        t = font_small.render("{}".format(h), True, BLACK)
        t_rect = text.get_rect()
        st.blit(t, t_rect)
        text.blit(st, (x, 0))
        h += 20/len(t_gradient)
        x += width
    surf.blit(stripe, (25, 50))
    surf.blit(text, (25, 75))
    screen.blit(surf, pos)
