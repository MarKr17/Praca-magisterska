import pygame
import os

from Visualisation.Constants import (WHITE, BLACK, assets_path, font_small,
                                     font_medium)
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider
pygame.font.init()


class Controls():
    def __init__(self, screen, width, height, pos, PAUSE):
        self.screen = screen
        self.width = width
        self.height = height
        self.PAUSE = PAUSE
        self.image = pygame.image.load(os.path.join(assets_path,
                                       "pause.png"))
        self.pick_image()
        self.pos = pos
        self.button = Button(
                        # Mandatory Parameters
                        self.screen,  # Surface to place button on
                        self.pos[0],  # X-coordinate of top left corner
                        self.pos[1],  # Y-coordinate of top left corner
                        int(self.height/2),  # Width
                        int(self.height/2),  # Height
                        radius=2000,
                        image=self.image,
                        onClick=lambda: self.not_function()
                        )
        x = self.button.getX() + int(self.height/2) + int(self.width/30)
        self.slider = Slider(self.screen, x,
                             int(self.pos[1]+self.height/6),
                             int(self.width/6), int(self.height/6), min=1,
                             max=100, initial=10, step=1)

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
        self.image = pygame.transform.smoothscale(self.image, (int(self.height/2),
                                                               int(self.height/2)))

    def draw(self, steps):
        text = font_medium.render("FPS: {}".format(self.slider.getValue()),
                                  True, BLACK)
        textRect = text.get_rect()
        x = self.slider.getX() + self.slider.getWidth() + int(self.width/10)
        textRect.center = (x, self.pos[1]+25)
        self.screen.blit(text, textRect)
        x = x + text.get_width() + int(self.width/20)
        text = font_medium.render("Step: {}".format(steps), True, BLACK)
        textRect = text.get_rect()
        textRect.center = (x, self.pos[1]+25)
        self.screen.blit(text, textRect)
