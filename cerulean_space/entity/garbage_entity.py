from typing import NoReturn

from pygame import Rect

from cerulean_space.constants import PLAYER_MAX_X, PLAYER_MIN_X, PLAYER_COLLECT_MAX_HEIGHT, PLAYER_COLLECT_MIN_HEIGHT
from cerulean_space.entity.entity import Entity
from cerulean_space.entity.player_entity import PlayerEntity
from cerulean_space.sounds.sound_events import SoundEvents
from cerulean_space.util.math.math_helper import MathHelper


class GarbageEntity(Entity):
    def __init__(self, world):
        self.__amount = 10
        super().__init__(world)

    def get_bounding_box(self) -> Rect:
        return Rect(0, 0, 5 * self.__amount, 5 * self.__amount)

    def set_amount(self, amount: int):
        self.__amount = amount
        self.update_bounding_box()

    def tick(self):
        self.set_pos((MathHelper.max(MathHelper.min(self.get_x(), PLAYER_MAX_X), PLAYER_MIN_X),
                      MathHelper.max(MathHelper.min(PLAYER_COLLECT_MAX_HEIGHT, self.get_y()), PLAYER_COLLECT_MIN_HEIGHT)))

    @staticmethod
    def get_codec_name() -> str:
        return "garbage"

    def on_collided_with(self, other) -> NoReturn:
        if type(other) is PlayerEntity:
            player: PlayerEntity = other
            if player.can_collect(self.__amount):
                player.collected_garbage += self.__amount
                player.update_mass()
                self.world.try_predicate_win()
                SoundEvents.DING.play()
                self.remove()

    def can_despawn(self) -> bool:
        return False

    def read_from_json(self, data: dict):
        super(GarbageEntity, self).read_from_json(data)
        self.__amount = data["amount"]

    def write_to_json(self) -> dict:
        data = super(GarbageEntity, self).write_to_json()
        data["amount"] = self.__amount
        return data
