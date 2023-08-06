import pygame
import os

from Constants import WHITE, BLACK, assets_path, font_small
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider
pygame.font.init()


class Controls():
    def __init__(self, screen, width, height, pos, PAUSE):
        self.screen = screen
        self.width = width
        self.height = height
        self.PAUSE = PAUSE
        self.panel = pygame.Surface((width, height), pygame.SRCALPHA, 32)
        self.panel.fill(WHITE)
        self.image = pygame.image.load(os.path.join(assets_path,
                                       "pause.png"))
        self.pick_image()
        self.pos = pos
        self.button = Button(
                        # Mandatory Parameters
                        self.screen,  # Surface to place button on
                        50,  # X-coordinate of top left corner
                        930,  # Y-coordinate of top left corner
                        50,  # Width
                        50,  # Height
                        radius=2000,
                        image=self.image,
                        onClick=lambda: self.not_function()
                        )
        self.slider = Slider(self.screen, 200, 945, 100, 20, min=1, max=100,
                             step=1)

    def not_function(self):
        self.PAUSE = not self.PAUSE
        self.pick_image()
        self.button.image = self.image

    def pick_image(self):
        if self.PAUSE is False:
            self.image = pygame.image.load(os.path.join(assets_path,
                                           "pause.png"))
        elif self.PAUSE is True:
            self.image = pygame.image.load(os.path.join(assets_path,
                                           "play.png"))
        self.image = pygame.Surface.convert_alpha(self.image)
        self.image = pygame.transform.smoothscale(self.image, (50, 50))

    def draw(self):
        text = font_small.render("FPS: {}".format(self.slider.getValue()),
                                 True, BLACK)
        textRect = text.get_rect()
        textRect.center = (250, 980)
        self.screen.blit(text, textRect)
