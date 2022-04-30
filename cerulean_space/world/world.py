from typing import List, Any

from pygame import Rect
from pygame.draw_py import BoundingBox


class World:
    def __init__(self):
        # 实体列表,全部继承Entity,为防止循环引用,使用Any
        self.entities: List[Any] = list()

    def add_entity(self, entity):
        self.entities.append(entity)

    def tick(self):
        for e in self.entities:
            e.tick()

    def get_collided_entity(self, entity) -> List:
        result = list()
        for e in self.entities:
            if e is not entity and entity.bounding_box.colliderect(e.bounding_box):
                result.append(e)
        return result
