import abc

import cerulean_space
from cerulean_space.input.player_interaction_manager import PlayerInteractionManager
from cerulean_space.render.texture_manager import TextureManager


class GameMode(metaclass=abc.ABCMeta):
    def on_mode_start(self, world):
        pass

    def on_mode_end(self, world):
        pass

    def tick_game_mode(self, world: 'cerulean_space.world.world.World'):
        pass

    def camera_locked(self) -> bool:
        return True

    @abc.abstractmethod
    def get_interaction_manager(self) -> PlayerInteractionManager:
        pass

    @abc.abstractmethod
    def construct_renderer(self, world, texture_manager: TextureManager):
        pass

    def write_to_json(self) -> dict:
        return dict()

    def read_from_json(self, data: dict):
        pass

    @staticmethod
    @abc.abstractmethod
    def get_name() -> str:
        pass
