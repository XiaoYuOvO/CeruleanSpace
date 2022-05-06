from typing import NoReturn

from pygame import Rect
from pygame.draw_py import BoundingBox

from cerulean_space.entity.entity import Entity
from cerulean_space.entity.player_entity import PlayerEntity


class RockEntity(Entity):
    @staticmethod
    def get_codec_name() -> str:
        return "rock"

    def get_bounding_box(self) -> Rect:
        return Rect(0, 0, 50, 50)

    def on_collided_with(self, other) -> NoReturn:
        if type(other) is PlayerEntity:
            other.damage(5)
            self.remove()
