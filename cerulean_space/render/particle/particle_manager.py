from typing import List

from cerulean_space.render.particle.particle import Particle


class ParticleManager:

    def __init__(self):
        self.particle_list: List[Particle] = list()

    def tick_particles(self):
        for particle in self.particle_list:
            particle.tick_particle()
            if particle.dead:
                self.particle_list.remove(particle)

    def add_particle(self, particle: Particle):
        self.particle_list.append(particle)
