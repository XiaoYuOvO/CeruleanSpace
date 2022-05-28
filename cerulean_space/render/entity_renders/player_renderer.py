from typing import NoReturn

from pygame import Surface, Rect

from cerulean_space.entity.player_entity import PlayerEntity
from cerulean_space.render.entity_renders.entity_renderer import EntityRenderer
from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.texture.animated_texture import AnimatedTexture
from cerulean_space.render.texture.texture import Texture
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.util.identifier import Identifier


class PlayerRenderer(EntityRenderer[PlayerEntity]):
    def __init__(self, texture_manager: TextureManager):
        self.player_texture = AnimatedTexture(Identifier("player_fire.png"),115,184)
        super().__init__(texture_manager)

        # self.texture.subsurface()

    def render(self, entity: PlayerEntity, game_renderer: GameRenderer) -> NoReturn:
        super().render(entity, game_renderer)
        # game_renderer.draw_string_at_left("Pos(" + entity.get_x().__str__() + " ," + entity.get_y().__str__() + ")", 0, 0,
        #                                   20, Color(0, 0, 0), ABSOLUTE)

    def get_texture(self) -> Texture:
        return self.player_texture
