from typing import NoReturn

from pygame import Rect

import cerulean_space
from cerulean_space.entity.living_entity import LivingEntity
from cerulean_space.util.math.math_helper import MathHelper


class PlayerEntity(LivingEntity):
    def get_bounding_box(self) -> Rect:
        return Rect(0, 0, 115, 184)

    def __init__(self, world: cerulean_space.world.world.World):
        super().__init__(world)
        self.push_strength = 1.0

    def tick(self):
        super().tick()
        if self.tick_exist % 30 == 0:
            self.forward_vec = MathHelper.cutoff(self.forward_vec * 0.5, 0.5, 0)

    def get_default_health(self) -> float:
        return 20.0

    # 由于渲染器的坐标系是以左上角为原点的所以实际是反向的
    def push_reward(self):
        self.forward_vec = MathHelper.max(self.forward_vec - self.push_strength, 0)

    def push_forward(self):
        self.forward_vec += self.push_strength

    def on_collided_with(self, other) -> NoReturn:
        # print(f'Player collided with {type(other)}')
        pass
