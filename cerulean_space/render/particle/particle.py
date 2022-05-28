import abc

from pygame import Vector2, Surface


# T = TypeVar("T", bound= Particle)


class Particle(metaclass=abc.ABCMeta):
    def __init__(self, particle_type, world, parameter):
        self.__x = 0
        self.__y = 0
        self.vec = Vector2(0, 0)
        self.dead = False
        self.max_lifetime = 0
        self.world = world
        self.particle_type = particle_type
        self.rotation = 0
        parameter.apply(self)
        self.lifetime = self.max_lifetime

    def set_pos(self, x: float, y: float):
        self.__x = x
        self.__y = y

    def tick_particle(self):
        self.lifetime -= 1
        self.__x += self.vec.x
        self.__y += self.vec.y
        if self.lifetime <= 0:
            self.dead = True

    def get_rendering_x(self) -> float:
        return self.__x

    def get_rendering_y(self) -> float:
        return -self.__y

    def get_texture(self) -> Surface:
        return self.particle_type.texture
