from typing import Tuple

import pygame
from pygame import Surface

from cerulean_space.render.particle.particle import Particle
from cerulean_space.render.particle.particle_parameter import ParticleParameter


class RockChunkParticle(Particle):
    def __init__(self, particle_type, world, parameter: ParticleParameter):
        super().__init__(particle_type, world, parameter)

    def get_texture(self) -> Surface:
        src: Surface = self.particle_type.texture
        rect = src.get_rect()
        scale = 2 * self.lifetime / self.max_lifetime
        size: Tuple[int, int] = (rect.width * scale, rect.height * scale)
        result = Surface(size)
        result.fill((255, 255, 255))
        pygame.transform.scale(src, size, result)
        result.set_colorkey((255, 255, 255))
        return result
