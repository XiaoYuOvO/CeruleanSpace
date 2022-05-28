from random import Random
from typing import NoReturn

from pygame import Rect

from cerulean_space.entity.entity import Entity
from cerulean_space.entity.player_entity import PlayerEntity
from cerulean_space.render.particle.particle_parameter import ParticleParameter
from cerulean_space.render.particle.particle_types import ROCK_CHUNK
from cerulean_space.sounds.sound_events import SoundEvents


class RockEntity(Entity):

    def __init__(self, world):
        self.__size: float = 10
        super().__init__(world)

    @staticmethod
    def get_codec_name() -> str:
        return "rock"

    def get_bounding_box(self) -> Rect:
        return Rect(0, 0, 50 * self.__size, 50 * self.__size)

    def on_collided_with(self, other) -> NoReturn:
        if type(other) is PlayerEntity:
            other.damage(5 * self.__size)
            count = round(2 * self.__size)
            rand: Random = self.world.rand
            for i in range(-count, count):
                self.world.add_particle(ROCK_CHUNK,
                                        ParticleParameter(self.get_x(), self.get_y(),
                                                          self.velocity.rotate(10 * i + rand.randint(-10, 10)) * (
                                                              rand.random()),
                                                          40))
            SoundEvents.ROCK_CRACK.play()
            self.remove()

    def set_size(self, size: float):
        self.__size = size
        self.update_bounding_box()
