import json
import os
from typing import NoReturn

from cerulean_space.world.world import World



class WorldStorage:
    @staticmethod
    def read_world_from_file(filename: str, game) -> World:
        file = open(filename, "r", encoding="utf-8")
        world_data: dict = json.load(file)
        result: World = World(game)
        result.read_world(world_data)
        file.close()
        return result

    @staticmethod
    def write_world_to_file(filename: str, world: World) -> NoReturn:
        with open(filename, "w", encoding="utf-8", newline='\n') as file:
            data = json.dumps(world.write_world())
            file.write(data)
