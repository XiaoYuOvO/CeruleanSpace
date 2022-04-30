from typing import Tuple

import pygame.freetype
from pygame import Color, Surface
from pygame._freetype import STYLE_DEFAULT

pygame.freetype.init()


class FontRenderer:
    def __init__(self, font_name: str):
        self.font: pygame.freetype.Font = pygame.freetype.SysFont(font_name, 10, False, False)

    def surface_from_font(self, content: str, size: float = 10, rotation: int = 0,
                          style: int = STYLE_DEFAULT,
                          color: Color = (255, 255, 255)) -> Surface:
        return self.font.render(content, color, None, style, rotation, size)[0]
