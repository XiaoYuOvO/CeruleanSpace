from random import Random
from typing import NoReturn

from pygame import Rect

from cerulean_space.entity.living_entity import LivingEntity
from cerulean_space.entity.player_entity import PlayerEntity
from cerulean_space.render.particle.particle_parameter import ParticleParameter
from cerulean_space.render.particle.particle_types import PLANE_CHUNK
from cerulean_space.render.particle.plane_chunk_particle import PlaneParticleParameter

DIRECTION_LEFT = -1
DIRECTION_RIGHT = 1


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
            count = 3
            rand: Random = self.world.rand
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
