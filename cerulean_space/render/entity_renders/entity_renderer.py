import abc
from typing import TypeVar, Generic, NoReturn

from pygame import Surface
from pygame.color import Color

from cerulean_space.entity.entity import Entity
from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.texture.texture import Texture
from cerulean_space.render.texture_manager import TextureManager

T = TypeVar("T", bound=Entity)


class EntityRenderer(Generic[T], metaclass=abc.ABCMeta):
    def __init__(self, texture_manager: TextureManager):
        self.texture = self.get_texture()
        self.texture.load_texture(texture_manager)

    def preprocess_texture(self, entity: T):
        pass

    def render(self, entity: T, game_renderer: GameRenderer) -> NoReturn:
        # 翻转游戏坐标系至渲染坐标系
        self.preprocess_texture(entity)
        self.texture.render_texture(game_renderer, (entity.get_rendering_x(), entity.get_rendering_y()),
                                    entity.rotation)
        # game_renderer.draw_surface_with_angle(self.preprocess_texture(entity, self.texture), entity.get_rendering_x(),
        #                                       entity.get_rendering_y(),
        #                                       -entity.rotation)
        line_color = Color(255, 255, 255)
        render_bottom_left = (entity.bounding_box.bottomleft[0], -entity.bounding_box.bottomleft[1])
        render_bottom_right = (entity.bounding_box.bottomright[0], -entity.bounding_box.bottomright[1])
        render_top_left = (entity.bounding_box.topleft[0], -entity.bounding_box.topleft[1])
        render_top_right = (entity.bounding_box.topright[0], -entity.bounding_box.topright[1])
        game_renderer.draw_line_by_point(render_bottom_left,
                                         render_bottom_right, 2,
                                         line_color)
        game_renderer.draw_line_by_point(render_top_left, render_top_right, 2,
                                         line_color)
        game_renderer.draw_line_by_point(render_bottom_left, render_top_left, 2,
                                         line_color)
        game_renderer.draw_line_by_point(render_bottom_right, render_top_right,
                                         2,
                                         line_color)

    def tick_texture(self):
        self.texture.tick_texture()

    @abc.abstractmethod
    def get_texture(self) -> Texture:
        pass
