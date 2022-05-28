from typing import Dict

from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.render.ui.game_mode.game_mode_ui_renderer import GameModeUIRenderer
from cerulean_space.render.world_renderer import WorldRenderer
from cerulean_space.world.game_mode.game_mode import GameMode
from cerulean_space.world.game_mode.game_modes import GameModes
from cerulean_space.world.world import World


class GameModeUIRenderDispatcher(WorldRenderer):

    def __init__(self, world: World, texture_manager: TextureManager):
        super().__init__(world, texture_manager)
        self.game_mode_renderer_map: Dict[GameMode, GameModeUIRenderer] = dict()
        for game_mode in GameModes.get_all_modes():
            self.game_mode_renderer_map[game_mode] = game_mode.construct_renderer(world, texture_manager)

    def render(self, game_renderer: GameRenderer):
        self.game_mode_renderer_map[self.world.game_mode].render(game_renderer, self.world.game_mode)

    def tick(self):
        self.game_mode_renderer_map[self.world.game_mode].tick()
