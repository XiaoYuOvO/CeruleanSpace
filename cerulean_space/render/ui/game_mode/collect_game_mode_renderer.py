from pygame import Color

from cerulean_space.constants import MIN_GARBAGE_COUNT_TO_WIN, GAME_TICK_RATE
from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.star_renderer import StarRenderer
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.render.ui.game_mode.game_mode_ui_renderer import GameModeUIRenderer, T
from cerulean_space.util.identifier import Identifier
from cerulean_space.util.math.math_helper import MathHelper
from cerulean_space.util.position_method import ABSOLUTE

BAR_TEXTURE = Identifier("bar.png")
GARBAGE_BAR_TEXTURE = Identifier("garbage_bar.png")


class CollectGameModeUIRenderer(GameModeUIRenderer):
    def __init__(self, world, texture_manager: TextureManager):
        super().__init__(world, texture_manager)
        self.garbage_bar_texture = texture_manager.load_or_get_texture(GARBAGE_BAR_TEXTURE)
        self.bar_texture = texture_manager.load_or_get_texture(BAR_TEXTURE)
        self.star_renderer = StarRenderer(world, texture_manager)

    def render(self, game_renderer: GameRenderer, gamemode: T):
        self.star_renderer.render(game_renderer)
        # 渲染垃圾收集数量
        mass_bar_x = 10
        mass_bar_height = 800
        mass_bar_y = round((game_renderer.get_rendering_height() - mass_bar_height) / 2)
        game_renderer.draw_surface_at(self.bar_texture, mass_bar_x + 1,
                                      mass_bar_y + self.bar_texture.get_height() / 2 - 8, ABSOLUTE)
        game_renderer.draw_line(mass_bar_x, round(mass_bar_y + mass_bar_height), mass_bar_x,
                                mass_bar_y + (
                                        1 - self.world.player.collected_garbage / self.world.player.get_max_garbage()) * mass_bar_height,
                                10,
                                Color(170, 170, 170), ABSOLUTE)
        game_renderer.draw_string_at_left(
            "飞船已收集垃圾 " + self.world.player.collected_garbage.__str__() + " / " + self.world.player.get_max_garbage().__str__(),
            0, mass_bar_y - 40,
            30, Color(170, 170, 170), ABSOLUTE)
        # 渲染已提交垃圾数量
        garbage_bar_y = game_renderer.get_rendering_height() - self.garbage_bar_texture.get_height()
        game_renderer.draw_surface_at(self.garbage_bar_texture, game_renderer.get_rendering_width() / 2,
                                      garbage_bar_y,
                                      ABSOLUTE)
        garbage_bar_x = (game_renderer.get_rendering_width() - self.garbage_bar_texture.get_width()) / 2 + 5
        game_renderer.draw_line(garbage_bar_x,
                                garbage_bar_y,
                                garbage_bar_x + self.garbage_bar_texture.get_width() * MathHelper.min(
                                    self.world.game_mode.garbage_collected / MIN_GARBAGE_COUNT_TO_WIN, 1),
                                garbage_bar_y, 10, Color(190, 80, 80), ABSOLUTE)
        game_renderer.draw_string_at_left(
            "已提交垃圾 " + self.world.game_mode.garbage_collected.__str__() + " / " + MIN_GARBAGE_COUNT_TO_WIN.__str__(),
            garbage_bar_x, garbage_bar_y - 20, 30, Color(255, 255, 255), ABSOLUTE)
        # 渲染剩余时间
        game_renderer.draw_string_centered(
            "剩余收集时间：" + round(self.world.game_mode.collect_time / GAME_TICK_RATE).__str__() + "秒",
            game_renderer.get_rendering_width() / 2, 50, 50, Color(255, 255, 255), ABSOLUTE)

    def tick(self):
        self.star_renderer.tick()
