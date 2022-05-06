from typing import NoReturn

import pygame.transform
from pygame import Surface

from cerulean_space.entity.plane_entity import PlaneEntity, DIRECTION_LEFT
from cerulean_space.render.entity_renders.entity_renderer import EntityRenderer, T
from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.util.identifier import Identifier

PLANE_TEXTURE = Identifier("plane.png")


class PlaneRenderer(EntityRenderer[PlaneEntity]):
    def __init__(self, texture_manager: TextureManager):
        super().__init__(texture_manager)
        self.left_texture = pygame.transform.flip(self.texture, True, False)

    def preprocess_texture(self, entity: PlaneEntity, surface: Surface) -> Surface:
        if entity.direction == DIRECTION_LEFT:
            return self.left_texture
        return surface

    def get_texture(self) -> Identifier:
        return PLANE_TEXTURE
