from typing import NoReturn

from pygame import Color, Surface, Rect

from cerulean_space.entity.player_entity import PlayerEntity
from cerulean_space.render.entity_renders.entity_renderer import EntityRenderer
from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.util.identifier import Identifier
from cerulean_space.util.position_method import RELATIVE, ABSOLUTE

player_texture = Identifier("player.png")
fire_texture = Identifier("player_fire.png")


class PlayerRenderer(EntityRenderer[PlayerEntity]):
    def __init__(self, texture_manager: TextureManager):
        super().__init__(texture_manager)
        self.fire_textures = []
        src_img = texture_manager.load_or_get_texture(fire_texture).convert_alpha()
        for i in range(round(src_img.get_height() / 184)):
            img = src_img.subsurface(Rect((0, i * 184), (115, 184)))
            self.fire_textures.append(img)
        # self.texture.subsurface()

    def render(self, entity: PlayerEntity, game_renderer: GameRenderer) -> NoReturn:
        super().render(entity, game_renderer)
        # game_renderer.draw_string_at_left("Pos(" + entity.get_x().__str__() + " ," + entity.get_y().__str__() + ")", 0, 0,
        #                                   20, Color(0, 0, 0), ABSOLUTE)

    def get_texture(self) -> Identifier:
        return player_texture

    def preprocess_texture(self, entity: PlayerEntity, surface: Surface) -> Surface:
        return self.fire_textures[entity.tick_exist % 26]
