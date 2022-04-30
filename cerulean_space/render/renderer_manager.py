from typing import List

from cerulean_space.render.entity_renders.entity_render_dispatcher import EntityRenderDispatcher
from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.render.world_renderer import WorldRenderer
from cerulean_space.world.world import World

texture_dir = '../img'


class RendererManager:
    def __init__(self, game_renderer: GameRenderer):
        self.game_renderer = game_renderer
        self.textureManager = TextureManager(texture_dir)
        self.worldRenderers: List[WorldRenderer] = list()

    def render(self):
        self.game_renderer.clear_screen()
        for renderer in self.worldRenderers:
            renderer.render(self.game_renderer)
        self.game_renderer.update_screen()
        pass

    def add_renderer(self, renderer: WorldRenderer):
        self.worldRenderers.append(renderer)

    def add_world_renderer(self, world: World):
        self.add_renderer(EntityRenderDispatcher(world, self.textureManager))
