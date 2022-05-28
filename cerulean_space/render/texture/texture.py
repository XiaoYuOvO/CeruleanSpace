import abc
from typing import Tuple

from pygame import Surface

from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.util.identifier import Identifier


class Texture(metaclass=abc.ABCMeta):
    def __init__(self, tex_id: Identifier):
        self.tex_id = tex_id
        self.cached_surface: Surface = None

    @abc.abstractmethod
    def load_texture(self, texture_manager: TextureManager):
        pass

    @abc.abstractmethod
    def render_texture(self, game_renderer: GameRenderer, pos: Tuple[int, int], rotation: int = 0):
        pass

    def tick_texture(self):
        pass
