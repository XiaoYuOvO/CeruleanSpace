import abc
from typing import TypeVar, Generic

from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.world.game_mode.game_mode import GameMode

T = TypeVar("T", bound=GameMode)


class GameModeUIRenderer(Generic[T], metaclass=abc.ABCMeta):
    def __init__(self, world, texture_manager: TextureManager):
        self.world = world
        self.texture_manager = texture_manager

    @abc.abstractmethod
    def render(self, game_renderer: GameRenderer, gamemode: T):
        pass

    def tick(self):
        pass

