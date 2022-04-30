from typing import NoReturn

from pygame import Color

from cerulean_space.entity.player_entity import PlayerEntity
from cerulean_space.render.entity_renders.entity_renderer import EntityRenderer
from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.util.identifier import Identifier
from cerulean_space.util.position_method import RELATIVE, ABSOLUTE

player_texture = Identifier("player.png")


class PlayerRenderer(EntityRenderer[PlayerEntity]):
    def __init__(self, texture_manager: TextureManager):
        super().__init__(texture_manager)

    def render(self, entity: PlayerEntity, game_renderer: GameRenderer) -> NoReturn:
        super().render(entity, game_renderer)
        game_renderer.draw_string_at("Pos(" + entity.x.__str__() + " ," + entity.y.__str__() + ")", 0, 0,
                                     20, Color(0, 0, 0), ABSOLUTE)

    def get_texture(self) -> Identifier:
        return player_texture
