from typing import NoReturn

from pygame import Rect
from pygame.draw_py import BoundingBox

from cerulean_space.entity.entity import Entity
from cerulean_space.entity.player_entity import PlayerEntity


class RockEntity(Entity):

    def __init__(self, world):
        self.__size: float = 10
        super().__init__(world)

    @staticmethod
    def get_codec_name() -> str:
        return "rock"

    def get_bounding_box(self) -> Rect:
        return Rect(0, 0, 50 * self.__size, 50 * self.__size)

    def on_collided_with(self, other) -> NoReturn:
        if type(other) is PlayerEntity:
            other.damage(5 * self.__size)
            self.remove()

    def set_size(self, size: float):
        self.__size = size
        self.update_bounding_box()
