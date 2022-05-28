from pygame import Color

from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.world_renderer import WorldRenderer
from cerulean_space.util.position_method import ABSOLUTE


class GameOverScreen(WorldRenderer):
    def render(self, game_renderer: GameRenderer):
        game_renderer.draw_string_centered("任务失败！",
                                           round(game_renderer.get_rendering_width() / 2),
                                           round(game_renderer.get_rendering_height() / 2), 100, Color(255,255,255),
                                           ABSOLUTE)
        game_renderer.draw_string_centered("当前高度: " + self.world.player.get_y().__str__(),
                                           round(game_renderer.get_rendering_width() / 2),
                                           round(game_renderer.get_rendering_height() / 3 * 2), 60, Color(255,255,255),
                                           ABSOLUTE)
