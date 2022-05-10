from typing import NoReturn

from pygame import Rect

from cerulean_space.constants import PLAYER_MAX_HEIGHT, PLAYER_MIN_HEIGHT, PLAYER_MIN_X, PLAYER_MAX_X, \
    PLAYER_COLLECT_MIN_HEIGHT, PLAYER_COLLECT_MAX_HEIGHT
from cerulean_space.entity.living_entity import LivingEntity
from cerulean_space.sounds.sound_events import SoundEvents
from cerulean_space.util.math.math_helper import MathHelper


class PlayerEntity(LivingEntity):
    @staticmethod
    def get_codec_name() -> str:
        return "player"

    def get_bounding_box(self) -> Rect:
        return Rect(0, 0, 115, 184)

    def __init__(self, world):
        super().__init__(world)
        self.push_strength = 2.0
        self.min_speed = 3.0
        self.min_y = PLAYER_MIN_HEIGHT
        self.max_y = PLAYER_MAX_HEIGHT
        self.fuel = self.get_max_fuel()
        self.lock_rotation = True
        self.max_rotation = 30
        self.rotation_speed = 3
        self.max_rotation_speed = 4
        self.max_push_strength = 2.0
        self.collected_garbage = 0
        self.base_mass = 60
        self.has_switched_to_collect = False
        self.update_mass()

    def get_max_fuel(self) -> int:
        return 250

    def get_max_garbage(self) -> int:
        return 300

    def damage(self, damage: float):
        super(PlayerEntity, self).damage(damage)
        SoundEvents.METAL_HIT.play()

    def update_mass(self):
        self.mass = self.fuel * 0.7 + self.collected_garbage + self.base_mass
        self.min_speed = 2.0 / MathHelper.max(self.mass / 100, 1)
        self.rotation_speed = self.max_rotation_speed / (self.mass / 100)
        self.push_strength = self.max_push_strength / (self.mass / 125)

    def can_collect(self,amount: int) -> bool:
        return self.get_max_garbage() - self.collected_garbage >= amount

    def can_despawn(self) -> bool:
        return False

    def living_tick(self):
        super().living_tick()
        if self.tick_exist % 30 == 0 and not self.world.is_collect_mode():
            self.forward_vec = self.min_speed + MathHelper.cutoff(self.forward_vec * 0.7, self.min_speed,
                                                                  self.min_speed)
        if not self.world.is_collect_mode():
            if self.get_y() >= PLAYER_COLLECT_MIN_HEIGHT:
                self.world.start_collect_mode()
            elif self.get_y() >= PLAYER_MAX_HEIGHT and not self.has_switched_to_collect:
                self.world.switch_to_collect_mode()
                self.has_switched_to_collect = True

        self.set_pos((MathHelper.max(MathHelper.min(self.get_x(), PLAYER_MAX_X), PLAYER_MIN_X),
                      MathHelper.max(MathHelper.min(self.max_y, self.get_y()), self.min_y)))
        for collides in self.world.get_collided_entity(self):
            collides.on_collided_with(self)
            self.on_collided_with(collides)

    def switch_to_collect_mode(self):
        self.lock_rotation = False
        self.max_y = PLAYER_COLLECT_MAX_HEIGHT

    def start_collect_mode(self):
        self.min_y = PLAYER_COLLECT_MIN_HEIGHT

    def on_death(self):
        self.world.game_over()

    def get_default_health(self) -> float:
        return 100.0

    def get_max_health(self) -> float:
        return 1000.0

    def push_reward(self):
        self.forward_vec = MathHelper.max(self.forward_vec - self.push_strength, self.min_speed)

    def push_forward(self):
        if self.fuel > 0:
            self.forward_vec += self.push_strength
            self.fuel -= 1
            self.update_mass()

    def rotate_left(self):
        if self.lock_rotation:
            self.rotation = MathHelper.max(-self.max_rotation, self.rotation - self.rotation_speed)
        else:
            self.rotation = self.rotation - self.rotation_speed

    def rotate_right(self):
        if self.lock_rotation:
            self.rotation = MathHelper.min(self.max_rotation, self.rotation + 3)
        else:
            self.rotation = self.rotation + self.rotation_speed

    def write_to_json(self) -> dict:
        data = super(PlayerEntity, self).write_to_json()
        data["push_strength"] = self.push_strength
        data["fuel"] = self.fuel
        data["collected_garbage"] = self.collected_garbage
        return data

    def read_from_json(self, data: dict):
        super(PlayerEntity, self).read_from_json(data)
        self.push_strength = data["push_strength"]
        self.fuel = data["fuel"]
        self.collected_garbage = data["collected_garbage"]
