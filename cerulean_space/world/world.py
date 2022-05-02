from random import Random
from typing import List, Any, NoReturn

from pygame import Rect
from pygame.draw_py import BoundingBox

from cerulean_space.entity.entity import Entity
from cerulean_space.entity.entity_types import EntityTypes, ENTITY_TYPES
from cerulean_space.entity.player_entity import PlayerEntity


class World:
    def __init__(self):
        # 实体列表,全部继承Entity,为防止循环引用,使用Any
        self.rand = Random()
        self.wind_force = 0.0
        self.player = PlayerEntity(self)
        self.entities: List[Entity] = list()

    def add_entity(self, entity):
        self.entities.append(entity)

    def tick(self):
        for e in self.entities:
            e.tick()
            if e.removed:
                self.entities.remove(e)

    def get_collided_entity(self, entity) -> List:
        result = list()
        for e in self.entities:
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
        for entity in self.entities:
            entities.append({
                "type": entity.get_codec_name(),
                "data": entity.write_to_json()
            })
        result["entities"] = entities
        result["wind_force"] = self.wind_force
        return result

