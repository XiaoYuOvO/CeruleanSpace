from typing import Callable

from cerulean_space.world.generation.spawn_factory import SpawnFactory


class SpawnEntry:
    def __init__(self, spawn_y: int, factory: SpawnFactory):
        self.spawn_y = spawn_y
        self.factory = factory
