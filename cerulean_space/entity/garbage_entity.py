from typing import NoReturn

from pygame import Rect

from cerulean_space.entity.entity import Entity
from cerulean_space.entity.player_entity import PlayerEntity


class GarbageEntity(Entity):
    def __init__(self, world):
        self.__amount = 10
        super().__init__(world)

    def get_bounding_box(self) -> Rect:
        return Rect(0, 0, 5 * self.__amount, 5 * self.__amount)

    def set_amount(self, amount: int):
        self.__amount = amount
        self.update_bounding_box()

    @staticmethod
    def get_codec_name() -> str:
        return "garbage"

    def on_collided_with(self, other) -> NoReturn:
        if type(other) is PlayerEntity:
            player: PlayerEntity = other
            player.collected_garbage += self.__amount
            player.update_mass()
            self.remove()

    def can_despawn(self) -> bool:
        return False
