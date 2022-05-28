import abc

import cerulean_space
from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.texture_manager import TextureManager


class WorldRenderer(metaclass=abc.ABCMeta):
    def __init__(self, world: 'cerulean_space.world.world.World', texture_manager: TextureManager):
        self.world = world
        self.texture_manager = texture_manager

    @abc.abstractmethod
    def render(self, game_renderer: GameRenderer):
        pass

    def tick(self):
        pass
