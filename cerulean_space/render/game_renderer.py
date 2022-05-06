from typing import Tuple

import pygame
from pygame._freetype import STYLE_DEFAULT
from pygame.rect import Rect
from pygame.surface import Surface

from cerulean_space.constants import DEFAULT_FONT_NAME, RENDERING_WIDTH, RENDERING_HEIGHT
from cerulean_space.render.font_renderer import FontRenderer
from cerulean_space.util.position_method import PositionMethod, RELATIVE


class GameRenderer:
    def __init__(self, width: int, height: int):
        pygame.init()
        # 设置绘制偏移,以模拟镜头移动效果
        self.draw_offset_x = 0
        self.draw_offset_y = 0
        self.screen = pygame.display.set_mode((width, height), flags=pygame.HWSURFACE | pygame.RESIZABLE)
        pygame.display.set_caption("蔚蓝深空")
        self.render_scale = 1
        self.font_renderer = FontRenderer(DEFAULT_FONT_NAME)
        self.canvas = Surface((RENDERING_WIDTH, RENDERING_HEIGHT))

    def set_draw_offset(self, x: int, y: int):
        self.draw_offset_x = x
        self.draw_offset_y = y

    def draw_surface_on_rect(self, surface: Surface, rect: Rect):
        self.canvas.blit(surface, rect)

    def draw_surface_with_angle(self, surface: Surface, x: int, y: int, rotation: float,
                                pos_method: PositionMethod = RELATIVE):
        img_copy = pygame.transform.rotate(surface, rotation)
        rotated_rect = img_copy.get_rect(
            center=(pos_method.calc_draw_pos(x, y, self.draw_offset_x, self.draw_offset_y)))
        self.canvas.blit(img_copy, rotated_rect)

    # 在屏幕上绘制字符串,字符串图像的中心点为(x,y)
    def draw_string_centered(self, content: str, x: int, y: int, size: float = 10,
                             color: pygame.Color = (255, 255, 255),
                             pos_method: PositionMethod = RELATIVE,
                             rotation: int = 0,
                             style: int = STYLE_DEFAULT):
        self.draw_surface_at(self.font_renderer.surface_from_font(content, size, rotation, style, color), x, y,
                             pos_method)

    # 在屏幕上绘制字符串,字符串图像的左上角为(x,y)
    def draw_string_at(self, content: str, x: int, y: int, size: float = 10, color: pygame.Color = (255, 255, 255),
                       pos_method: PositionMethod = RELATIVE,
                       rotation: int = 0,
                       style: int = STYLE_DEFAULT):
        text_surface = self.font_renderer.surface_from_font(content, size, rotation, style, color)
        text_bounds: Rect = text_surface.get_rect()
        self.draw_surface_at(text_surface, round(x + text_bounds.width / 2), round(y + text_bounds.height / 2),
                             pos_method)

    def draw_surface_at(self, surface: Surface, x: int, y: int,
                        pos_method: PositionMethod = RELATIVE):
        self.draw_surface_with_angle(surface, x, y, 0, pos_method)

    def clear_screen(self):
        self.canvas.fill((255, 255, 255))

    def draw_line(self, start_x: int, start_y: int, end_x: int, end_y: int, width: int = 1,
                  color: pygame.Color = (255, 255, 255),
                  pos_mehtod: PositionMethod = RELATIVE):
        pygame.draw.line(self.canvas, color,
                         pos_mehtod.calc_draw_pos(start_x, start_y, self.draw_offset_x, self.draw_offset_y),
                         pos_mehtod.calc_draw_pos(end_x, end_y, self.draw_offset_x, self.draw_offset_y),
                         width)

    def draw_line_by_point(self, start: Tuple[int, int], end: Tuple[int, int], width: int = 1,
                           color: pygame.Color = (255, 255, 255),
                           pos_mehtod: PositionMethod = RELATIVE):
        self.draw_line(start[0], start[1], end[0], end[1], width, color, pos_mehtod)

    def get_rendering_width(self) -> int:
        return self.canvas.get_width()

    def get_rendering_height(self) -> int:
        return self.canvas.get_height()

    def update_screen(self):
        resized = pygame.transform.scale(self.canvas, self.screen.get_size(), self.screen)
        self.screen.blit(resized, resized.get_rect())
        pygame.display.flip()
        pygame.display.update()
