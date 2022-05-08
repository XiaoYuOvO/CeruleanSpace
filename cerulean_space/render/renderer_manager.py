from typing import List

from cerulean_space.constants import TEXTURE_DIR
from cerulean_space.entity.player_entity import PlayerEntity
from cerulean_space.render.background_renderer import BackgroundRenderer
from cerulean_space.render.camera_renderer import CameraRenderer
from cerulean_space.render.entity_renders.entity_render_dispatcher import EntityRenderDispatcher
from cerulean_space.render.game_over_screen import GameOverScreen
from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.game_win_screen import GameWinScreen
from cerulean_space.render.particle.particle_renderer import ParticleRenderer
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.render.ui_renderer import UIRenderer
from cerulean_space.render.world_renderer import WorldRenderer
from cerulean_space.world.world import World


class RendererManager:
    def __init__(self, game_renderer: GameRenderer):
        self.game_renderer = game_renderer
        self.textureManager = TextureManager(TEXTURE_DIR)
        self.worldRenderers: List[WorldRenderer] = list()

    def render(self):
        self.game_renderer.clear_screen()
        for renderer in self.worldRenderers:
            renderer.render(self.game_renderer)
        self.game_renderer.update_screen()
        pass

    def add_renderer(self, renderer: WorldRenderer):
        self.worldRenderers.append(renderer)

    def init_all_renders(self, world: World, player: PlayerEntity):
        self.add_renderer(CameraRenderer(world, self.textureManager, player))
        self.add_renderer(BackgroundRenderer(world, self.textureManager))
        self.add_renderer(EntityRenderDispatcher(world, self.textureManager))
        self.add_renderer(UIRenderer(world, self.textureManager, player))
        self.add_renderer(ParticleRenderer(world, self.textureManager))

    def switch_to_game_over_screen(self, world: World):
        self.worldRenderers.clear()
        self.add_renderer(BackgroundRenderer(world, self.textureManager))
        self.add_renderer(GameOverScreen(world, self.textureManager))

    def switch_to_game_win_screen(self, world: World):
        self.worldRenderers.clear()
        self.add_renderer(BackgroundRenderer(world, self.textureManager))
        self.add_renderer(GameWinScreen(world, self.textureManager))
