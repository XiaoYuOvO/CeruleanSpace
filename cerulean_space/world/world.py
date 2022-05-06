from random import Random
from typing import List, Any, NoReturn, Dict

from pygame import Rect
from pygame.draw_py import BoundingBox

from cerulean_space.entity.entity import Entity
from cerulean_space.entity.entity_types import EntityTypes, ENTITY_TYPES
from cerulean_space.entity.player_entity import PlayerEntity
from cerulean_space.world.generation.entity_spawner import EntitySpawner


class World:
    def __init__(self, game_instance):
        # 实体列表,全部继承Entity,为防止循环引用,使用Any
        """
        :var self.rand :该世界的随机函数
        :var self.wind_force todo
        :var self.entities 该世界的实体列表
        :var self.weight 该世界的宽度
        :var self.height 该世界的高度

        """
        self.rand = Random()
        self.wind_force = 0.0
        self.player = PlayerEntity(self)
        # 实体与坐标并无对应关系
        self.entities: List[Entity] = list()

        self.weight = 100
        self.height = 100000
        self.part_height = int(self.height / 10)  # 基块大小
        self.part_amount = 3  # 每个分块中实体生成数量基数
        self.game = game_instance
        self.entity_spawner = EntitySpawner(self)

    def add_entity(self, entity: Entity):
        # if coordinate not in self.entities.key-s():
        if type(entity) is PlayerEntity:
            self.player = entity
        self.entities.append(entity)
        # entity.set_pos(tuple(coordinate))

    def tick(self):
        for e in self.entities:
            e.tick()
            if e.removed:
                self.entities.remove(e)
        self.entity_spawner.tick_spawn(self.player)

    def get_collided_entity(self, entity) -> List:
        result = list()
        for e in self.entities:
            if e is not entity and entity.bounding_box.colliderect(e.bounding_box):
                result.append(e)
        return result

    def read_world(self, data: dict) -> NoReturn:
        for entity_data in data.get("entities"):  # entities: List[Dict[str,? extends Entity]]
            entity_type = ENTITY_TYPES.get(entity_data.get("type"))
            new_entity = entity_type.construct_entity(self)
            new_entity.read_from_json(entity_data.get("data"))
            if type(new_entity) is PlayerEntity:
                self.player = new_entity
            self.add_entity(new_entity)
        self.wind_force = data.get("wind_force")
        pass

    def write_world(self) -> dict:
        result = dict()
        entities = list()
        for entity in self.entities:
            entities.append({
                "type": entity.get_codec_name(),
                "data": entity.write_to_json()
            })
        result["entities"] = entities
        result["wind_force"] = self.wind_force
        return result

    def add_spawn_entry(self, entry):
        self.entity_spawner.spawn_list.append(entry)

    def game_win(self):
        self.game.game_win()

    def game_over(self):
        self.game.game_over()
