from cerulean_space.render.particle.particle import Particle


class FireParticle(Particle):
    def __init__(self, particle_type, world, parameter):
        super().__init__(particle_type, world, parameter)
