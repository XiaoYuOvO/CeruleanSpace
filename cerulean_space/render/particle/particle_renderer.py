from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.particle.particle_manager import ParticleManager
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.render.world_renderer import WorldRenderer
from cerulean_space.world.world import World
from cerulean_space.render.particle.particle_types import load_particle_textures


class ParticleRenderer(WorldRenderer):
    def __init__(self, world: World, texture_manager: TextureManager):
        super().__init__(world, texture_manager)
        load_particle_textures(texture_manager)
        self.particle_manager = world.particle_manager

    def render(self, game_renderer: GameRenderer):
        for particle in self.particle_manager.particle_list:
            game_renderer.draw_surface_at(particle.get_texture(), particle.get_rendering_x(),
                                          particle.get_rendering_y())
