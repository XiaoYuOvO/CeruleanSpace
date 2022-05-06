from random import Random
from typing import Callable

from cerulean_space.constants import PLAYER_MIN_X, PLAYER_MAX_X
from cerulean_space.entity.plane_entity import PlaneEntity, DIRECTION_RIGHT, DIRECTION_LEFT
from cerulean_space.entity.player_entity import PlayerEntity
from cerulean_space.entity.rock_entity import RockEntity
from cerulean_space.world.generation.spawn_entry import SpawnEntry
from cerulean_space.world.world import World


class WorldGenerator:
    @staticmethod
    def create_plane_spawn_func(rand: Random) -> Callable[[World, int], None]:
        def on_spawn(world: World, spawn_y):
            plane = PlaneEntity(world)
            if rand.randint(0, 1) == 0:
                plane.velocity.x = rand.randint(5, 15)
                plane.set_pos((PLAYER_MIN_X, spawn_y))
                plane.direction = DIRECTION_RIGHT
            else:
                plane.velocity.x = -rand.randint(5, 15)
                plane.set_pos((PLAYER_MAX_X, spawn_y))
                plane.direction = DIRECTION_LEFT
            world.add_entity(plane)

        return on_spawn

    @staticmethod
    def create_rock_spawn_func(rand: Random) -> Callable[[World, int], None]:
        def on_spawn(world: World, spawn_y):
            rock = RockEntity(world)
            if rand.randint(0, 1) == 0:
                rock.velocity.x = rand.randint(5, 15)
                rock.set_pos((PLAYER_MIN_X, spawn_y))
            else:
                rock.velocity.x = -rand.randint(5, 15)
                rock.set_pos((PLAYER_MAX_X, spawn_y))
            world.add_entity(rock)

        return on_spawn

    @staticmethod
    def generate_in_range(world: World, count: int, rand: Random, height_range: range,
                          entity_creating_func: Callable[[Random], Callable[[World, int], None]]):
        each_distance = (height_range.start - height_range.stop) / count
        for i in range(1, count + 1):
            spawn_height = round(each_distance * i + rand.randint(-100, 100)) + height_range.start
            world.add_spawn_entry(SpawnEntry(spawn_height, entity_creating_func(rand)))

    @staticmethod
    def generate_planes_in_low_range(world: World, count: int, rand: Random):
        WorldGenerator.generate_in_range(world, count, rand, range(1000, 11000), WorldGenerator.create_plane_spawn_func)

    @staticmethod
    def generate_rocks_in_middle_range(world: World, count: int, rand: Random):
        WorldGenerator.generate_in_range(world, count, rand, range(12000, 22000), WorldGenerator.create_rock_spawn_func)

    @staticmethod
    def generate_world(rand: Random, game) -> World:
        world = World(game)
        WorldGenerator.generate_planes_in_low_range(world, 10, rand)
        # world.add_entity(PlayerEntity(world))
        return world


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __iter__(self):
        return [self.x, self.y]

    def __get_random_coordinate(self, offset):
        while True:
            yield Coordinate(self.rand.randrange(0, 100), self.rand.randrange(offset, offset + self.part_height))
    #
    # def create_world(self):
    #     """
    #     创建一个新的世界，按照世界高度划分区域并随机生成实体
    #     :return:
    #     """
    #     for i in range(0, 9):
    #         for each in self.__get_random_coordinate(self.part_height * i):
    #             for _ in range(0, i * self.part_amount):
    #                 self.add_entity(Entity(self), each)
