from pygame import Color
from pygame.freetype import STYLE_DEFAULT

from cerulean_space.entity.player_entity import PlayerEntity
from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.render.world_renderer import WorldRenderer
from cerulean_space.util.identifier import Identifier
from cerulean_space.util.position_method import ABSOLUTE
from cerulean_space.world.world import World

BAR_TEXTURE = Identifier("bar.png")


class UIRenderer(WorldRenderer):
    def __init__(self, world: World, texture_manager: TextureManager, player: PlayerEntity):
        super().__init__(world, texture_manager)
        self.bar_texture = texture_manager.load_or_get_texture(BAR_TEXTURE)
        self.player = player

    def render(self, game_renderer: GameRenderer):
        # 渲染玩家燃料条
        fuel_bar_x = game_renderer.get_rendering_width() - 20
        fuel_bar_height = 800
        fuel_bar_y = (game_renderer.get_rendering_height() - fuel_bar_height) / 2
        game_renderer.draw_surface_at(self.bar_texture, fuel_bar_x + 1,
                                      fuel_bar_y + self.bar_texture.get_height() / 2 - 8, ABSOLUTE)
        game_renderer.draw_line(fuel_bar_x, round(fuel_bar_y + fuel_bar_height), fuel_bar_x,
                                fuel_bar_y + (1 - self.player.attribute.fuel / self.player.get_max_fuel()) * fuel_bar_height, 10,
                                Color(255, 20, 20), ABSOLUTE)
        if self.player.attribute.fuel <= 0:
            game_renderer.draw_string_at_right("燃料不足,无法加速!", fuel_bar_x, round(game_renderer.get_rendering_height()),
                                               30, Color(200, 50, 50), ABSOLUTE)
        # 渲染玩家血条
        x = self.player.get_rendering_x() - self.player.get_bounding_box().width / 2
        y = self.player.get_rendering_y() + self.player.get_bounding_box().height / 2
        health_bar_width = self.player.get_bounding_box().width * (self.player.health / self.player.get_max_health())
        game_renderer.draw_line(x, y, health_bar_width + x, y, 10, Color(255, 0, 0))
        for t in self.world.hover_texts:
            if t.cached_img is None:
                t.cached_img = game_renderer.font_renderer.surface_from_font(t.content, t.size, 0, STYLE_DEFAULT,
                                                                             t.color)
            if not t.no_fade:
                t.cached_img.set_alpha(round(t.display_time / t.max_display_time * 255))
            game_renderer.draw_surface_at(t.cached_img, t.x, t.y, ABSOLUTE)
