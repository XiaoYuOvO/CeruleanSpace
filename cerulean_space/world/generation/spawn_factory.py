from random import Random
from typing import Callable, Dict, Any

from cerulean_space.constants import PLAYER_MAX_X, PLAYER_MIN_X
from cerulean_space.entity.cloud_entity import CloudEntity
from cerulean_space.entity.plane_entity import PlaneEntity, DIRECTION_RIGHT, DIRECTION_LEFT
from cerulean_space.entity.rock_entity import RockEntity


class SpawnFactory:
    def __init__(self, name: str, on_spawn: Callable[[Any, Random, int], None]):
        self.name = name
        self.on_spawn = on_spawn


def on_plane_spawn(world: Any, rand: Random, spawn_y):
    plane = PlaneEntity(world)
    if rand.randint(0, 1) == 0:
        plane.velocity.x = rand.randint(3, 10)
        plane.set_pos((rand.randint(PLAYER_MIN_X, round(PLAYER_MAX_X / 3)), spawn_y))
        plane.direction = DIRECTION_RIGHT
    else:
        plane.velocity.x = -rand.randint(3, 10)
        plane.set_pos((PLAYER_MAX_X - rand.randint(PLAYER_MIN_X, round(PLAYER_MAX_X / 3)), spawn_y))
        plane.direction = DIRECTION_LEFT
    world.add_entity(plane)


def on_rock_spawn(world: Any, rand: Random, spawn_y):
    rock = RockEntity(world)
    rock.velocity.y = -rand.randint(3, 10)
    rock.set_pos((rand.randint(PLAYER_MIN_X, PLAYER_MAX_X), spawn_y))
    rock.set_size(1 + rand.random() * 1.5)
    world.add_entity(rock)


def on_rock_in_space_spawn(world: Any, rand: Random, spawn_y):
    rock = RockEntity(world)
    # rock.velocity.y = -rand.randint(3, 10)
    rock.set_pos((rand.randint(PLAYER_MIN_X, PLAYER_MAX_X), spawn_y))
    rock.set_size(1 + rand.random() * 1.5)
    world.add_entity(rock)


def on_cloud_spawn(world: Any, rand: Random, spawn_y):
    cloud = CloudEntity(world)
    cloud.set_pos((rand.randint(PLAYER_MIN_X, PLAYER_MAX_X), spawn_y))
    # cloud.velocity.x = rand.randint(-5, 5)
    world.add_entity(cloud)


FACTORIES: Dict[str, SpawnFactory] = dict()


def register(name: str, on_spawn: Callable[[Any, Random, int], None]) -> SpawnFactory:
    factory = SpawnFactory(name, on_spawn)
    FACTORIES[name] = factory
    return factory


class SpawnFactories:
    PLANE_SPAWN: SpawnFactory = register("plane_spawn", on_plane_spawn)
    ROCK_SPAWN: SpawnFactory = register("rock_spawn", on_rock_spawn)
    ROCK_SPAWN_SPACE: SpawnFactory = register("rock_spawn_space", on_rock_in_space_spawn)
    CLOUD_SPAWN: SpawnFactory = register("cloud_spawn", on_cloud_spawn)