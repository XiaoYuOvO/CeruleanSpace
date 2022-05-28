from random import Random
from typing import NoReturn

from pygame import Rect

from cerulean_space.entity.living_entity import LivingEntity
from cerulean_space.entity.player_entity import PlayerEntity
from cerulean_space.render.particle.particle_types import PLANE_CHUNK
from cerulean_space.render.particle.plane_chunk_particle import PlaneParticleParameter
from cerulean_space.render.texture.stated_texture import TextureState


class PlaneDirection(TextureState):
    def __init__(self, name: str):
        self.name: str = name

    def __hash__(self):
        return self.name.__hash__()

    def __eq__(self, other):
        return type(other) is PlaneDirection and other.name == self.name

DIRECTION_LEFT = PlaneDirection("left")
DIRECTION_RIGHT = PlaneDirection("right")


class PlaneEntity(LivingEntity):
    def __init__(self, world):
        super().__init__(world)
        self.direction = DIRECTION_LEFT

    def get_bounding_box(self) -> Rect:
        return Rect(0, 0, 150, 50)

    @staticmethod
    def get_codec_name() -> str:
        return "plane"

    def get_max_health(self) -> float:
        return 10

    def get_default_health(self) -> float:
        return 10

    def on_collided_with(self, other) -> NoReturn:
        if type(other) is PlayerEntity:
            other.damage(10)
            # for i in range(-count, count):
            left_to_right = False
            if self.direction == DIRECTION_LEFT:
                left_to_right = True
                self.world.add_particle(PLANE_CHUNK,
                                        PlaneParticleParameter(self.get_x(), self.get_y(),
                                                               self.velocity.rotate(45) * 0.8,
                                                               40, False, left_to_right))
                self.world.add_particle(PLANE_CHUNK,
                                        PlaneParticleParameter(self.get_x() - self.bounding_box.width / 2, self.get_y(),
                                                               self.velocity.rotate(45) * 1.1,
                                                               40, True, left_to_right))
            else:
                self.world.add_particle(PLANE_CHUNK,
                                        PlaneParticleParameter(self.get_x(), self.get_y(),
                                                               self.velocity.rotate(-45) * 1.1,
                                                               40, False, left_to_right))
                self.world.add_particle(PLANE_CHUNK,
                                        PlaneParticleParameter(self.get_x() + self.bounding_box.width / 2, self.get_y(),
                                                               self.velocity.rotate(-45) * 0.8,
                                                               40, True, left_to_right))

            self.remove()

    def read_from_json(self, data: dict):
        super(PlaneEntity, self).read_from_json(data)
        self.direction = PlaneDirection(data["direction"])

    def write_to_json(self) -> dict:
        data = super(PlaneEntity, self).write_to_json()
        data["direction"] = self.direction.name
        return data
