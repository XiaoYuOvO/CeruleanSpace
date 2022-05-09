from pygame import Color
from pygame.freetype import STYLE_DEFAULT

from cerulean_space.constants import PLAYER_MAX_HEIGHT, MIN_GARBAGE_COUNT_TO_WIN, GAME_TICK_RATE
from cerulean_space.entity.player_entity import PlayerEntity
from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.render.world_renderer import WorldRenderer
from cerulean_space.util.identifier import Identifier
from cerulean_space.util.math.math_helper import MathHelper
from cerulean_space.util.position_method import ABSOLUTE
from cerulean_space.world.world import World

BAR_TEXTURE = Identifier("bar.png")
HEIGHT_BAR_TEXTURE = Identifier("height_bar.png")
GARBAGE_BAR_TEXTURE = Identifier("garbage_bar.png")


class UIRenderer(WorldRenderer):
    def __init__(self, world: World, texture_manager: TextureManager, player: PlayerEntity):
        super().__init__(world, texture_manager)
        self.bar_texture = texture_manager.load_or_get_texture(BAR_TEXTURE)
        self.height_bar_texture = texture_manager.load_or_get_texture(HEIGHT_BAR_TEXTURE)
        self.garbage_bar_texture = texture_manager.load_or_get_texture(GARBAGE_BAR_TEXTURE)
        self.player = player

    def render(self, game_renderer: GameRenderer):
        # 渲染玩家燃料条
        fuel_bar_x = game_renderer.get_rendering_width() - 20
        fuel_bar_height = 800
        fuel_bar_y = (game_renderer.get_rendering_height() - fuel_bar_height) / 2
        game_renderer.draw_surface_at(self.bar_texture, fuel_bar_x + 1,
                                      fuel_bar_y + self.bar_texture.get_height() / 2 - 8, ABSOLUTE)
        game_renderer.draw_line(fuel_bar_x, round(fuel_bar_y + fuel_bar_height), fuel_bar_x,
                                fuel_bar_y + (1 - self.player.fuel / self.player.get_max_fuel()) * fuel_bar_height, 10,
                                Color(255, 20, 20), ABSOLUTE)
        if self.player.fuel <= 0:
            game_renderer.draw_string_at_right("燃料不足,无法加速!", fuel_bar_x, round(game_renderer.get_rendering_height()),
                                               30, Color(200, 50, 50), ABSOLUTE)
        # 渲染玩家血条
        x = self.player.get_rendering_x() - self.player.get_bounding_box().width / 2
        y = self.player.get_rendering_y() + self.player.get_bounding_box().height / 2
        health_bar_width = self.player.get_bounding_box().width * (self.player.health / self.player.get_max_health())
        game_renderer.draw_line(x, y, health_bar_width + x, y, 10, Color(255, 0, 0))
        if self.world.is_collect_mode():
            # 渲染垃圾收集数量
            mass_bar_x = 10
            mass_bar_height = 800
            mass_bar_y = round((game_renderer.get_rendering_height() - mass_bar_height) / 2)
            game_renderer.draw_surface_at(self.bar_texture, mass_bar_x + 1,
                                          mass_bar_y + self.bar_texture.get_height() / 2 - 8, ABSOLUTE)
            game_renderer.draw_line(mass_bar_x, round(mass_bar_y + mass_bar_height), mass_bar_x,
                                    mass_bar_y + (
                                            1 - self.player.collected_garbage / self.player.get_max_garbage()) * mass_bar_height,
                                    10,
                                    Color(170, 170, 170), ABSOLUTE)
            game_renderer.draw_string_at_left(
                "飞船已收集垃圾 " + self.player.collected_garbage.__str__() + " / " + self.player.get_max_garbage().__str__(),
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
                                        self.world.garbage_collected / MIN_GARBAGE_COUNT_TO_WIN, 1),
                                    garbage_bar_y, 10, Color(190, 80, 80), ABSOLUTE)
            game_renderer.draw_string_at_left(
                "已提交垃圾 " + self.world.garbage_collected.__str__() + " / " + MIN_GARBAGE_COUNT_TO_WIN.__str__(),
                garbage_bar_x, garbage_bar_y - 20, 30, Color(255, 255, 255), ABSOLUTE)
            # 渲染剩余时间
            game_renderer.draw_string_centered(
                "剩余收集时间：" + round(self.world.collect_time / GAME_TICK_RATE).__str__() + "秒",
                game_renderer.get_rendering_width() / 2, 50, 50, Color(255, 255, 255), ABSOLUTE)
        else:
            # 渲染飞行高度
            height_bar_x = 10
            height_bar_height = 800
            height_bar_y = round((game_renderer.get_rendering_height() - height_bar_height) / 2)
            game_renderer.draw_surface_at(self.height_bar_texture, height_bar_x + 1,
                                          height_bar_y + self.bar_texture.get_height() / 2 - 8, ABSOLUTE)
            player_mark_y = height_bar_y + round(height_bar_height * (1 - MathHelper.min(self.player.get_y() / PLAYER_MAX_HEIGHT, 1)))
            game_renderer.draw_line(0, player_mark_y, height_bar_x + self.height_bar_texture.get_width(),
                                    player_mark_y,
                                    10,
                                    Color(170, 170, 170), ABSOLUTE)
            game_renderer.draw_string_at_left(
                "当前高度 " + round(self.player.get_y()).__str__() + " / " + PLAYER_MAX_HEIGHT.__str__(),
                0, height_bar_y - 40,
                30, Color(170, 170, 170), ABSOLUTE)
            # 渲染当前风向
            wind_direction = ""
            if self.world.wind_force > 0:
                wind_direction = "向右"
            else:
                wind_direction = "向左"
            game_renderer.draw_string_centered("当前风力：" + wind_direction + " - " + MathHelper.abs(round(self.world.wind_force * 10)).__str__(),
                                               game_renderer.get_rendering_width() / 2,20,50,Color(255,255,255),ABSOLUTE)
        for t in self.world.hover_texts:
            if t.cached_img is None:
                t.cached_img = game_renderer.font_renderer.surface_from_font(t.content, t.size, 0, STYLE_DEFAULT,
                                                                             t.color)
            if not t.no_fade:
                t.cached_img.set_alpha(round(t.display_time / t.max_display_time * 255))
            game_renderer.draw_surface_at(t.cached_img, t.x, t.y, ABSOLUTE)
