import pygame
from pygame import Surface

from cerulean_space.render.particle.particle import Particle
from cerulean_space.render.particle.particle_parameter import ParticleParameter


class PlaneParticleParameter(ParticleParameter):
    def __init__(self, x: float, y: float, vec: pygame.Vector2, lifetime: int, left_part: bool, left_to_right: bool):
        super().__init__(x, y, vec, lifetime)
        self.left_part = left_part
        self.left_to_right = left_to_right

    def apply(self, particle):
        super(PlaneParticleParameter, self).apply(particle)
        particle.left_part = self.left_part
        particle.left_to_right = self.left_to_right


class PlaneChunkParticle(Particle):
    def __init__(self, particle_type, world, parameter: ParticleParameter):
        self.left_part = False
        self.left_to_right = False
        super().__init__(particle_type, world, parameter)

    def get_texture(self) -> Surface:
        src: Surface = self.particle_type.texture
        if self.left_part:
            src = pygame.transform.chop(src, pygame.Rect(0, 0, src.get_width() / 2, 0))
            src = pygame.transform.rotate(src, 90)
        else:
            src = pygame.transform.chop(src, pygame.Rect(src.get_width() / 2, 0, src.get_width(), 0))
            src = pygame.transform.rotate(src, -90)
        scale = 255 * self.lifetime / self.max_lifetime
        src.set_alpha(scale)
        src = pygame.transform.flip(src, self.left_to_right, False)
        return src
