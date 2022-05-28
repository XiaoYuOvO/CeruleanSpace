from pygame import Color

from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.world_renderer import WorldRenderer
from cerulean_space.util.position_method import ABSOLUTE


class GameWinScreen(WorldRenderer):
    def render(self, game_renderer: GameRenderer):
        game_renderer.draw_string_centered("任务完成！",
                                           round(game_renderer.get_rendering_width() / 2),
                                           round(game_renderer.get_rendering_height() / 2), 100, Color(168, 50, 50),
                                           ABSOLUTE)
