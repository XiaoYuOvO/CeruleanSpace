from pygame import Color

from cerulean_space.constants import MIN_GARBAGE_COUNT_TO_WIN
from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.world_renderer import WorldRenderer
from cerulean_space.util.position_method import ABSOLUTE


class MissionFailedScreen(WorldRenderer):
    def render(self, game_renderer: GameRenderer):
        game_renderer.draw_string_centered("游戏结束！",
                                           round(game_renderer.get_rendering_width() / 2),
                                           round(game_renderer.get_rendering_height() / 2), 100, Color(0, 0, 0),
                                           ABSOLUTE)
        game_renderer.draw_string_centered(
            "已收集垃圾: " + self.world.garbage_collected.__str__() + " / " + MIN_GARBAGE_COUNT_TO_WIN.__str__(),
            round(game_renderer.get_rendering_width() / 2),
            round(game_renderer.get_rendering_height() / 3 * 2), 60, Color(0, 0, 0),
            ABSOLUTE)
