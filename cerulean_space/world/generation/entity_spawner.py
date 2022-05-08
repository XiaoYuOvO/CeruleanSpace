from random import Random
from typing import List

from cerulean_space.constants import RENDERING_HEIGHT
from cerulean_space.entity.player_entity import PlayerEntity
# from cerulean_space.world.generation.spawn_entry import SpawnEntry


class EntitySpawner:
    def __init__(self, world):
        self.world = world
        self.spawn_list: List = list()

    def tick_spawn(self, rand: Random, player: PlayerEntity):
        for entry in self.spawn_list:
            if entry.spawn_y <= player.get_y() + RENDERING_HEIGHT:
                entry.factory.on_spawn(self.world, rand, entry.spawn_y)
                self.spawn_list.remove(entry)
