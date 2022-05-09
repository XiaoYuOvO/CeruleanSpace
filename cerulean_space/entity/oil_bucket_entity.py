from typing import NoReturn

from pygame import Rect

from cerulean_space.entity.entity import Entity
from cerulean_space.entity.player_entity import PlayerEntity
from cerulean_space.util.math.math_helper import MathHelper


class OilBucketEntity(Entity):
    def get_bounding_box(self) -> Rect:
        return Rect(0, 0, 50, 75)

    def on_collided_with(self, other) -> NoReturn:
        if type(other) is PlayerEntity:
            player: PlayerEntity = other
            player.fuel = MathHelper.min(player.get_max_fuel(), player.fuel + 50)
            self.remove()

    def can_despawn(self) -> bool:
        return False

    @staticmethod
    def get_codec_name() -> str:
        return "oil_bucket"
