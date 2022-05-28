from typing import List, Type

from cerulean_space.constants import TEXTURE_DIR
from cerulean_space.entity.player_entity import PlayerEntity
from cerulean_space.render.background_renderer import BackgroundRenderer
from cerulean_space.render.camera_renderer import CameraRenderer
from cerulean_space.render.entity_renders.entity_render_dispatcher import EntityRenderDispatcher
from cerulean_space.render.ui.game_mode.game_mode_ui_render_dispatcher import GameModeUIRenderDispatcher
from cerulean_space.render.ui.game_over_screen import GameOverScreen
from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.ui.game_win_screen import GameWinScreen
from cerulean_space.render.particle.particle_renderer import ParticleRenderer
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.render.ui.mission_failed_screen import MissionFailedScreen
from cerulean_space.render.ui.ui_renderer import UIRenderer
from cerulean_space.render.world_renderer import WorldRenderer
from cerulean_space.world.world import World


class RendererManager:
    def __init__(self, game_renderer: GameRenderer):
        self.game_renderer = game_renderer
        self.texture_manager = TextureManager(TEXTURE_DIR)
        self.world_renderers: List[WorldRenderer] = list()

    def render(self):
        self.game_renderer.clear_screen()
        for renderer in self.world_renderers:
            renderer.render(self.game_renderer)
        self.game_renderer.update_screen()

    def tick(self):
        for renderer in self.world_renderers:
            renderer.tick()

    def add_renderer(self, renderer: WorldRenderer):
        self.world_renderers.append(renderer)

    def remove_renderer(self, renderer_t: Type):
        for renderer in self.world_renderers:
            if type(renderer) is renderer_t:
                self.world_renderers.remove(renderer)

    def insert_renderer_after(self, renderer_to_add: WorldRenderer, renderer_t: Type):
        for renderer in self.world_renderers:
            if type(renderer) is renderer_t:
                self.world_renderers.insert(self.world_renderers.index(renderer) + 1, renderer_to_add)

    def init_all_renders(self, world: World, player: PlayerEntity):
        self.add_renderer(CameraRenderer(world, self.texture_manager, player))
        self.add_renderer(BackgroundRenderer(world, self.texture_manager))
        self.add_renderer(EntityRenderDispatcher(world, self.texture_manager))
        self.add_renderer(UIRenderer(world, self.texture_manager, player))
        self.add_renderer(ParticleRenderer(world, self.texture_manager))
        self.add_renderer(GameModeUIRenderDispatcher(world, self.texture_manager))

    def switch_to_game_over_screen(self, world: World):
        self.remove_renderer(UIRenderer)
        self.remove_renderer(EntityRenderDispatcher)
        self.remove_renderer(GameModeUIRenderDispatcher)
        self.add_renderer(GameOverScreen(world, self.texture_manager))

    def switch_to_collect_failed_screen(self, world: World, garbage_collected: int):
        self.remove_renderer(UIRenderer)
        self.remove_renderer(EntityRenderDispatcher)
        self.remove_renderer(GameModeUIRenderDispatcher)
        self.add_renderer(MissionFailedScreen(world, self.texture_manager, garbage_collected))

    def switch_to_game_win_screen(self, world: World):
        self.remove_renderer(UIRenderer)
        self.remove_renderer(EntityRenderDispatcher)
        self.remove_renderer(GameModeUIRenderDispatcher)
        self.add_renderer(GameWinScreen(world, self.texture_manager))
