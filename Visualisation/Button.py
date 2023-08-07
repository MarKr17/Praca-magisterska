import pygame
import os
from Visualisation.Constants import assets_path, GREY


class Button():
    def __init__(self, screen, width, height, pos):
        self.screen = screen,
        self.width = width
        self.height = height
        self.surf = pygame.Surface((width, height), pygame.SRCALPHA, 32)
        self.pos = pos
        self.x = pos[0], pos[0]+width
        self.y = pos[1], pos[1]+height

    def draw(self, PAUSE):

        if PAUSE:
            image = pygame.image.load(os.path.join(assets_path,
                                                   "play.png"))
        else:
            image = pygame.image.load(os.path.join(assets_path,
                                                   "pause.png"))

        image = pygame.transform.smoothscale(image, (self.width, self.height))
        surf = pygame.Surface((self.width, self.width), pygame.SRCALPHA, 32)
        surf.fill(GREY)
        # surf.set_alpha(30)
        # pygame.draw.circle(surf, color, (radius, radius), radius)
        self.screen[0].blit(surf, self.pos)
        self.screen[0].blit(image, self.pos)
