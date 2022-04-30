from typing import Dict

import pygame.surface
from pygame import Surface

from cerulean_space.util.identifier import Identifier


class TextureManager:

    def __init__(self, texture_dir: str):
        self.texture_dir = texture_dir
        self.textures: Dict[Identifier, Surface] = dict()

    def load_or_get_texture(self, identifier: Identifier):
        texture = self.textures.get(identifier, None)
        if texture is None:
            # 若材质未加载则从磁盘中加载
            texture = pygame.image.load(self.texture_dir + "/" + identifier.name)
            self.textures[identifier] = texture
        # 返回获得的材质
        return texture

    # @staticmethod
    # def draw_surface(surface: Surface):
    #     surface.get_alpha()

    @staticmethod
    def to_surface(s) -> Surface:
        return s
