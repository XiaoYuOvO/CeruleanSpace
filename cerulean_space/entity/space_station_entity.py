from typing import NoReturn

from pygame import Rect

from cerulean_space.entity.entity import Entity
from cerulean_space.entity.player_entity import PlayerEntity


class SpaceStationEntity(Entity):
    def __init__(self, world):
        super().__init__(world)

    @staticmethod
    def get_codec_name() -> str:
        return "space_station"

    def get_bounding_box(self) -> Rect:
        return Rect(0, 0, 500, 300)

    def on_collided_with(self, other) -> NoReturn:
        if type(other) is PlayerEntity:
            player: PlayerEntity = other
            if player.collected_garbage > 0:
                self.world.game_mode.garbage_collected += player.collected_garbage
                player.collected_garbage = 0
                player.update_mass()

    def can_despawn(self) -> bool:
        return False
