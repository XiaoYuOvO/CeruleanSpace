from typing import NoReturn

from pygame import Rect

from cerulean_space.entity.living_entity import LivingEntity
from cerulean_space.entity.player_entity import PlayerEntity

DIRECTION_LEFT = -1
DIRECTION_RIGHT = 1


class PlaneEntity(LivingEntity):
    def __init__(self, world):
        super().__init__(world)
        self.direction = DIRECTION_LEFT

    def get_bounding_box(self) -> Rect:
        return Rect(0, 0, 150, 50)

    @staticmethod
    def get_codec_name() -> str:
        return "plane"

    def get_max_health(self) -> float:
        return 10

    def get_default_health(self) -> float:
        return 10

    def on_collided_with(self, other) -> NoReturn:
        if type(other) is PlayerEntity:
            other.damage(10)
            self.remove()
