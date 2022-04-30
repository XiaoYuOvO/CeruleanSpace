import abc
from typing import TypeVar, Generic, NoReturn

from cerulean_space.entity.entity import Entity
from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.util.identifier import Identifier

T = TypeVar("T", bound=Entity)


class EntityRenderer(Generic[T], metaclass=abc.ABCMeta):
    def __init__(self, texture_manager: TextureManager):
        self.texture = texture_manager.load_or_get_texture(self.get_texture())

    def render(self, entity: T, game_renderer: GameRenderer) -> NoReturn:
        game_renderer.draw_surface_with_angle(self.texture, entity.x, entity.y, entity.rotation)

    @abc.abstractmethod
    def get_texture(self) -> Identifier:
        pass
