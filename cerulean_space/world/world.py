from random import Random
from typing import List, Any, NoReturn, Dict

from pygame import Rect
from pygame.draw_py import BoundingBox

from cerulean_space.entity.entity import Entity
from cerulean_space.entity.entity_types import EntityTypes, ENTITY_TYPES
from cerulean_space.entity.player_entity import PlayerEntity


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __iter__(self):
        return [self.x, self.y]


class World:
    def __init__(self):
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
        self.entities: Dict[Coordinate, Entity] = dict()

        self.weight = 100
        self.height = 100000
        self.part_height = int(self.height / 10)  # 基块大小
        self.part_amount = 3  # 每个分块中实体生成数量基数

    def add_entity(self, entity: Entity, coordinate: Coordinate):
        if coordinate not in self.entities.keys():
            self.entities[coordinate] = entity
            entity.set_pos(tuple(coordinate))

    def tick(self):
        for c, e in self.entities.keys(), self.entities.values():
            e.tick()
            if e.removed:
                self.entities.pop(c)

    def get_collided_entity(self, entity) -> List:
        result = list()
        for e in self.entities.values():
            if e is not entity and entity.bounding_box.colliderect(e.bounding_box):
                result.append(e)
        return result

    def read_world(self, data: dict) -> NoReturn:
        for entity_data in data.get("entities"): # entities: List[Dict[str,? extends Entity]]
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
        for entity in self.entities.values():
            entities.append({
                "type": entity.get_codec_name(),
                "data": entity.write_to_json()
            })
        result["entities"] = entities
        result["wind_force"] = self.wind_force
        return result

    def __get_random_coordinate(self, offset):
        while True:
            yield Coordinate(self.rand.randrange(0, 100), self.rand.randrange(offset, offset + self.part_height))

    def create_world(self):
        """
        创建一个新的世界，按照世界高度划分区域并随机生成实体
        :return:
        """
        for i in range(0, 9):
            for each in self.__get_random_coordinate(self.part_height * i):
                for _ in range(0, i * self.part_amount):
                    self.add_entity(Entity(self), each)
