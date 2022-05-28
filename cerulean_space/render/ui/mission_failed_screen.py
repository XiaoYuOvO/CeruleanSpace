from pygame import Color

from cerulean_space.constants import MIN_GARBAGE_COUNT_TO_WIN
from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.render.world_renderer import WorldRenderer
from cerulean_space.util.position_method import ABSOLUTE
from cerulean_space.world.world import World


class MissionFailedScreen(WorldRenderer):
    def __init__(self, world: World, texture_manager: TextureManager, garbage_collected: int):
        super().__init__(world, texture_manager)
        self.garbage_collected = garbage_collected

    def render(self, game_renderer: GameRenderer):
        game_renderer.draw_string_centered("任务失败！",
                                           round(game_renderer.get_rendering_width() / 2),
                                           round(game_renderer.get_rendering_height() / 2), 100, Color(255, 255, 255),
                                           ABSOLUTE)
        game_renderer.draw_string_centered(
            "已收集垃圾: " + self.garbage_collected.__str__() + " / " + MIN_GARBAGE_COUNT_TO_WIN.__str__(),
            round(game_renderer.get_rendering_width() / 2),
            round(game_renderer.get_rendering_height() / 3 * 2), 60, Color(255, 255, 255),
            ABSOLUTE)
