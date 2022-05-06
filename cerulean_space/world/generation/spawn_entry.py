from typing import Callable

from cerulean_space.world.world import World


class SpawnEntry:
    def __init__(self, spawn_y: int, on_spawn: Callable[[World, int], None]):
        self.spawn_y = spawn_y
        self.on_spawn = on_spawn
