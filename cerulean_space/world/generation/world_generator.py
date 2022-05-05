from random import Random

from cerulean_space.world.world import World


class WorldGenerator:
    @staticmethod
    def generate_world(rand: Random) -> World:
        world = World()
        