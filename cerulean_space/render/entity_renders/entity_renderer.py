import abc
from typing import TypeVar, Generic, NoReturn

from pygame import Color

from cerulean_space.entity.entity import Entity
from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.util.identifier import Identifier

T = TypeVar("T", bound=Entity)


class EntityRenderer(Generic[T], metaclass=abc.ABCMeta):
    def __init__(self, texture_manager: TextureManager):
        self.texture = texture_manager.load_or_get_texture(self.get_texture())

    def render(self, entity: T, game_renderer: GameRenderer) -> NoReturn:
        # 翻转游戏坐标系至渲染坐标系
        game_renderer.draw_surface_with_angle(self.texture, entity.get_rendering_x(), entity.get_rendering_y(),
                                              -entity.rotation)
        line_color = Color(0, 0, 0)
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

    @abc.abstractmethod
    def get_texture(self) -> Identifier:
        pass
