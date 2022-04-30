from pygame import Rect
from pygame.draw_py import BoundingBox

from cerulean_space.entity.entity import Entity


class RockEntity(Entity):
    def get_bounding_box(self) -> Rect:
        return Rect(0, 0, 50, 50)
