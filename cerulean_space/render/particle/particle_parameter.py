from typing import Generic, TypeVar

from pygame import Vector2

from cerulean_space.render.particle.particle import Particle

T = TypeVar("T", bound=Particle)


class ParticleParameter(Generic[T]):
    def __init__(self, x: float, y: float, vec: Vector2,lifetime: int):
        self.x = x
        self.y = y
        self.vec = vec
        self.lifetime = lifetime

    def apply(self, particle: T):
        particle.set_pos(self.x, self.y)
        particle.vec = self.vec
        particle.max_lifetime = self.lifetime
