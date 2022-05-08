from typing import Callable, TypeVar, Generic, List, Any

from pygame import Vector2, Surface

from cerulean_space.render.particle.fire_particle import FireParticle
from cerulean_space.render.particle.particle import Particle
from cerulean_space.render.particle.particle_parameter import ParticleParameter
from cerulean_space.render.particle.plane_chunk_particle import PlaneChunkParticle
from cerulean_space.render.particle.rock_chunk_particle import RockChunkParticle
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.util.identifier import Identifier

T = TypeVar("T", bound=Particle)
P = TypeVar("P", bound=ParticleParameter)


class ParticleType(Generic[T]):
    def __init__(self, name: str, factory: Callable[[Any, Any, ParticleParameter], T]):
        self.factory = factory
        self.name = name
        self.texture_id: Identifier = Identifier("particles/" + name + ".png")
        self.texture: Surface = None

    def create_particle(self, world, parameter: ParticleParameter) -> T:
        return self.factory(self, world, parameter)


PARTICLES: List[ParticleType[Any]] = list()


def register_particle_type(name: str, factory: Callable[[ParticleType, Any, ParticleParameter], T]) -> ParticleType[T]:
    particle_type = ParticleType(name, factory)
    PARTICLES.append(particle_type)
    return particle_type


def load_particle_textures(texture_manager: TextureManager):
    for particle in PARTICLES:
        particle.texture = texture_manager.load_or_get_texture(particle.texture_id)


ROCK_CHUNK = register_particle_type("rock_chunk", RockChunkParticle)
PLANE_CHUNK = register_particle_type("plane_chunk", PlaneChunkParticle)
FIRE = register_particle_type("fire", FireParticle)
