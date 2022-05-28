import abc
from abc import ABC
from typing import Tuple

from pygame import Surface

from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.texture.simple_texture import SimpleTexture


class DynamicTexture(SimpleTexture, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def preprocess_texture(self, surface: Surface) -> Surface:
        pass

    def render_texture(self, game_renderer: GameRenderer, pos: Tuple[int, int], rotation=0):
        if rotation is not 0:
            game_renderer.draw_surface_with_angle(self.preprocess_texture(self.cached_surface), pos[0],
                                                  pos[1],
                                                  -rotation)
        else:
            game_renderer.draw_surface_at(self.preprocess_texture(self.cached_surface), pos[0],
                                          pos[1])
