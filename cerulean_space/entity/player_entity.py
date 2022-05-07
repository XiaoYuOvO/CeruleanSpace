from typing import NoReturn

from pygame import Rect

import cerulean_space
from cerulean_space.constants import PLAYER_MAX_HEIGHT, PLAYER_MIN_HEIGHT, PLAYER_MIN_X, PLAYER_MAX_X
from cerulean_space.entity.living_entity import LivingEntity
from cerulean_space.util.math.math_helper import MathHelper


class PlayerEntity(LivingEntity):
    @staticmethod
    def get_codec_name() -> str:
        return "player"

    def get_bounding_box(self) -> Rect:
        return Rect(0, 0, 115, 184)

    def __init__(self, world):
        super().__init__(world)
        self.push_strength = 1.5
        self.min_speed = 2.5
        self.fuel = self.get_max_fuel()
        self.max_rotation = 30

    def get_max_fuel(self) -> int:
        return 250

    def living_tick(self):
        super().living_tick()
        if self.tick_exist % 30 == 0:
            self.forward_vec = self.min_speed + MathHelper.cutoff(self.forward_vec * 0.7, self.min_speed,
                                                                  self.min_speed)
        if self.get_y() >= PLAYER_MAX_HEIGHT:
            self.world.game_win()
        self.set_pos((MathHelper.max(MathHelper.min(self.get_x(), PLAYER_MAX_X), PLAYER_MIN_X),
                      MathHelper.max(MathHelper.min(PLAYER_MAX_HEIGHT, self.get_y()), PLAYER_MIN_HEIGHT)))
        for collides in self.world.get_collided_entity(self):
            collides.on_collided_with(self)
            self.on_collided_with(collides)

    def on_death(self):
        self.world.game_over()

    def get_default_health(self) -> float:
        return 100.0

    def get_max_health(self) -> float:
        return 100.0

    def push_reward(self):
        self.forward_vec = MathHelper.max(self.forward_vec - self.push_strength, self.min_speed)

    def push_forward(self):
        if self.fuel > 0:
            self.forward_vec += self.push_strength
            self.fuel -= 1

    def rotate_left(self):
        self.rotation = MathHelper.max(-self.max_rotation, self.rotation - 3)

    def rotate_right(self):
        self.rotation = MathHelper.min(self.max_rotation, self.rotation + 3)

    def on_collided_with(self, other) -> NoReturn:
        # print(f'Player collided with {type(other)}')
        pass

    def write_to_json(self) -> dict:
        data = super(PlayerEntity, self).write_to_json()
        data["push_strength"] = self.push_strength
        data["fuel"] = self.fuel
        return data

    def read_from_json(self, data: dict):
        super(PlayerEntity, self).read_from_json(data)
        self.push_strength = data["push_strength"]
        self.fuel = data["fuel"]
