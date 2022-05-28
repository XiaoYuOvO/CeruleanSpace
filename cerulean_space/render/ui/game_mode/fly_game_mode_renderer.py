from pygame import Color

from cerulean_space.constants import PLAYER_MAX_HEIGHT
from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.render.ui.game_mode.game_mode_ui_renderer import GameModeUIRenderer
from cerulean_space.util.identifier import Identifier
from cerulean_space.util.math.math_helper import MathHelper
from cerulean_space.util.position_method import ABSOLUTE


BAR_TEXTURE = Identifier("bar.png")
HEIGHT_BAR_TEXTURE = Identifier("height_bar.png")


class FlyGameModeUIRenderer(GameModeUIRenderer):
    def __init__(self, world, texture_manager: TextureManager):
        super().__init__(world, texture_manager)
        self.bar_texture = texture_manager.load_or_get_texture(BAR_TEXTURE)
        self.height_bar_texture = texture_manager.load_or_get_texture(HEIGHT_BAR_TEXTURE)

    def render(self, game_renderer: GameRenderer, gamemode):
        # 渲染飞行高度
        height_bar_x = 10
        height_bar_height = 800
        height_bar_y = round((game_renderer.get_rendering_height() - height_bar_height) / 2)
        game_renderer.draw_surface_at(self.height_bar_texture, height_bar_x + 1,
                                      height_bar_y + self.bar_texture.get_height() / 2 - 8, ABSOLUTE)
        player_mark_y = height_bar_y + round(
            height_bar_height * (1 - MathHelper.min(self.world.player.get_y() / PLAYER_MAX_HEIGHT, 1)))
        game_renderer.draw_line(0, player_mark_y, height_bar_x + self.height_bar_texture.get_width(),
                                player_mark_y,
                                10,
                                Color(170, 170, 170), ABSOLUTE)
        game_renderer.draw_string_at_left(
            "当前高度 " + round(self.world.player.get_y()).__str__() + " / " + PLAYER_MAX_HEIGHT.__str__(),
            0, height_bar_y - 40,
            30, Color(170, 170, 170), ABSOLUTE)
        # 渲染当前风向
        if gamemode.wind_force > 0:
            wind_direction = "向右"
        else:
            wind_direction = "向左"
        game_renderer.draw_string_centered(
            "当前风力：" + wind_direction + " - " + MathHelper.abs(round(gamemode.wind_force * 10)).__str__(),
            game_renderer.get_rendering_width() / 2, 20, 50, Color(255, 255, 255), ABSOLUTE)
