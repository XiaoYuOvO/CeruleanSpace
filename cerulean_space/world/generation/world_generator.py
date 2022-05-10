from random import Random

from cerulean_space.constants import PLAYER_COLLECT_MAX_HEIGHT, PLAYER_COLLECT_MIN_HEIGHT
from cerulean_space.world.generation.spawn_entry import SpawnEntry
from cerulean_space.world.generation.spawn_factory import SpawnFactory, SpawnFactories
from cerulean_space.world.world import World


class WorldGenerator:
    @staticmethod
    def generate_in_range(world: World, count: int, rand: Random, height_range: range,
                          factory: SpawnFactory):
        each_distance = (height_range.stop - height_range.start) / count
        for i in range(1, count + 1):
            spawn_height = round(each_distance * i + rand.randint(-100, 100)) + height_range.start
            world.add_spawn_entry(SpawnEntry(spawn_height, factory))

    @staticmethod
    def generate_planes_in_low_range(world: World, count: int, rand: Random):
        WorldGenerator.generate_in_range(world, count, rand, range(1000, 11000), SpawnFactories.PLANE_SPAWN)

    @staticmethod
    def generate_rocks_in_middle_range(world: World, count: int, rand: Random):
        WorldGenerator.generate_in_range(world, count, rand, range(12000, 32000), SpawnFactories.ROCK_SPAWN)

    @staticmethod
    def generate_rocks_in_space(world: World, count: int, rand: Random):
        WorldGenerator.generate_in_range(world, count, rand, range(32000, 50000), SpawnFactories.ROCK_SPAWN_SPACE)

    @staticmethod
    def generate_clouds(world: World, count: int, rand: Random):
        WorldGenerator.generate_in_range(world, count, rand, range(1000, 30000), SpawnFactories.CLOUD_SPAWN)

    @staticmethod
    def generate_garbage(world: World, count: int, rand: Random):
        WorldGenerator.generate_in_range(world, count, rand,
                                         range(PLAYER_COLLECT_MIN_HEIGHT, PLAYER_COLLECT_MAX_HEIGHT),
                                         SpawnFactories.GARBAGE_SPAWN)

    @staticmethod
    def generate_space_station(world: World, count: int, rand: Random):
        area_middle = PLAYER_COLLECT_MIN_HEIGHT + round((PLAYER_COLLECT_MAX_HEIGHT - PLAYER_COLLECT_MIN_HEIGHT) / 2)
        WorldGenerator.generate_in_range(world, count, rand,
                                         range(area_middle, area_middle),
                                         SpawnFactories.SPACE_STATION_SPAWN)

    @staticmethod
    def generate_oil_bucket(world: World, count: int, rand: Random):
        WorldGenerator.generate_in_range(world, count, rand,
                                         range(PLAYER_COLLECT_MIN_HEIGHT, PLAYER_COLLECT_MAX_HEIGHT),
                                         SpawnFactories.OIL_BUCKET_SPAWN)

    @staticmethod
    def generate_world(rand: Random, game) -> World:
        world = World(game)
        WorldGenerator.generate_planes_in_low_range(world, 20, rand)
        WorldGenerator.generate_rocks_in_middle_range(world, 30, rand)
        WorldGenerator.generate_clouds(world, 100, rand)
        WorldGenerator.generate_rocks_in_space(world, 130, rand)
        WorldGenerator.generate_garbage(world, 50, rand)
        WorldGenerator.generate_space_station(world, 1, rand)
        WorldGenerator.generate_oil_bucket(world, 10, rand)
        # world.add_entity(PlayerEntity(world))
        return world
