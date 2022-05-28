import abc
from typing import TypeVar, Generic, Dict

from pygame import Surface

from cerulean_space.render.texture.dynamic_texture import DynamicTexture
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.util.identifier import Identifier


class TextureState(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __hash__(self):
        pass


S = TypeVar("S", bound=TextureState)


class StatedTexture(Generic[S], DynamicTexture, metaclass=abc.ABCMeta):
    def __init__(self):
        super().__init__(Identifier(""))
        self.state_cache: Dict[S, Surface] = dict()
        self.current_state: S = None
        self.texture_loader: TextureManager = None

    def update(self, state: S):
        self.current_state = state

    def load_texture(self, texture_manager: TextureManager):
        self.state_cache.clear()
        self.texture_loader = texture_manager

    def preprocess_texture(self, surface: Surface) -> Surface:
        if not self.state_cache.__contains__(self.current_state):
            self.state_cache[self.current_state] = self._create_texture_from_state(self.current_state)
        return self.state_cache[self.current_state]

    @abc.abstractmethod
    def _create_texture_from_state(self, s: S) -> Surface:
        pass
