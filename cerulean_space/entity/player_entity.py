from pygame import Rect

from cerulean_space.component.component_manager import ComponentManager
from cerulean_space.constants import PLAYER_MAX_HEIGHT, PLAYER_MIN_HEIGHT, PLAYER_MIN_X, PLAYER_MAX_X, \
    PLAYER_COLLECT_MIN_HEIGHT, PLAYER_COLLECT_MAX_HEIGHT
from cerulean_space.entity.living_entity import LivingEntity
from cerulean_space.sounds.sound_events import SoundEvents
from cerulean_space.util.math.math_helper import MathHelper
from pygame import Rect

from cerulean_space.component.component_manager import ComponentManager
from cerulean_space.constants import PLAYER_MAX_HEIGHT, PLAYER_MIN_HEIGHT, PLAYER_MIN_X, PLAYER_MAX_X, \
    PLAYER_COLLECT_MIN_HEIGHT, PLAYER_COLLECT_MAX_HEIGHT
from cerulean_space.entity.living_entity import LivingEntity
from cerulean_space.sounds.sound_events import SoundEvents
from cerulean_space.util.math.math_helper import MathHelper


class PlayerAttribute:
    def __init__(self, push_strength, min_speed, rotation_speed, max_fuel, mass, capacity, max_health):
        self.mass = mass
        self.max_fuel = max_fuel
        self.rotation_speed = rotation_speed
        self.min_speed = min_speed
        self.push_strength = push_strength
        self.capacity = capacity
        self.fuel = self.max_fuel
        self.max_health = max_health

    def read_from_json(self, data: dict):
        self.mass = data["mass"]
        self.max_fuel = data["max_fuel"]
        self.rotation_speed = data["rotation_speed"]
        self.min_speed = data["min_speed"]
        self.fuel = data["fuel"]
        self.push_strength = data["push_strength"]
        self.capacity = data["capacity"]
        self.max_fuel = data["max_health"]

    def write_to_json(self) -> dict:
        data = dict()
        data["mass"] = self.mass
        data["max_fuel"] = self.max_fuel
        data["fuel"] = self.fuel
        data["rotation_speed"] = self.rotation_speed
        data["min_speed"] = self.min_speed
        data["push_strength"] = self.push_strength
        data["capacity"] = self.capacity
        data["max_health"] = self.max_health
        return data


class PlayerAttributeBuilder:
    def __init__(self):
        self.max_fuel = 250
        self.max_health = 80
        self.push_strength = 2.0
        self.min_speed = 3.0
        self.max_rotation = 30
        self.rotation_speed = 3
        self.base_mass = 60
        self.capacity = 300

    def build(self) -> PlayerAttribute:
        return PlayerAttribute(self.push_strength, self.min_speed, self.rotation_speed, self.max_fuel, self.base_mass,
                               self.capacity, self.max_health)


class PlayerEntity(LivingEntity):
    @staticmethod
    def get_codec_name() -> str:
        return "player"

    def get_bounding_box(self) -> Rect:
        return Rect(0, 0, 115, 184)

    def __init__(self, world):
        self.attribute = PlayerAttributeBuilder().build()
        super().__init__(world)
        self.min_y = PLAYER_MIN_HEIGHT
        self.max_y = PLAYER_MAX_HEIGHT
        self.lock_rotation = True
        self.max_rotation = 30
        self.max_rotation_speed = 4
        self.max_push_strength = 2.0
        self.collected_garbage = 0
        self.component_manager: ComponentManager = ComponentManager()
        self.update_mass()

    def get_max_fuel(self) -> int:
        return self.attribute.max_fuel

    def get_max_garbage(self) -> int:
        return self.attribute.capacity

    def damage(self, damage: float):
        super(PlayerEntity, self).damage(damage)
        SoundEvents.METAL_HIT.play()

    def update_mass(self):
        self.mass = self.attribute.fuel * 0.7 + self.collected_garbage + self.attribute.mass
        self.attribute.min_speed = 2.0 / MathHelper.max(self.mass / 80, 1)
        self.attribute.rotation_speed = self.max_rotation_speed / (self.mass / 80)
        self.attribute.push_strength = self.max_push_strength / (self.mass / 100)

    def can_collect(self, amount: int) -> bool:
        return self.get_max_garbage() - self.collected_garbage >= amount

    def can_despawn(self) -> bool:
        return False

    def living_tick(self):
        super().living_tick()
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
        return self.attribute.max_health

    def get_max_health(self) -> float:
        return self.attribute.max_health

    def write_to_json(self) -> dict:
        data = super(PlayerEntity, self).write_to_json()
        data["player_attribute"] = self.attribute.write_to_json()
        data["collected_garbage"] = self.collected_garbage
        return data

    def read_from_json(self, data: dict):
        super(PlayerEntity, self).read_from_json(data)
        self.attribute.read_from_json(data["player_attribute"])
        self.collected_garbage = data["collected_garbage"]
