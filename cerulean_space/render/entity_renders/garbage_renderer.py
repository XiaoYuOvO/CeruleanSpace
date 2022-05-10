import pygame
from pygame import Surface

from cerulean_space.entity.garbage_entity import GarbageEntity, GarbageTypes, GarbageType
from cerulean_space.render.entity_renders.entity_renderer import EntityRenderer
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.util.identifier import Identifier

GARBAGE_TEXTURE = Identifier("garbage.png")


class GarbageRenderer(EntityRenderer[GarbageEntity]):
    def __init__(self, texture_manager: TextureManager):
        super().__init__(texture_manager)
        for e in GarbageTypes.VALUES:
            garbage_type: GarbageType = e
            garbage_type.texture = texture_manager.load_or_get_texture(Identifier(garbage_type.name + ".png"))

    def preprocess_texture(self, entity: GarbageEntity, surface: Surface) -> Surface:
        # self.texture.set_colorkey((255, 255, 255))
        result = Surface(entity.bounding_box.size)
        result.fill((255, 255, 255))
        pygame.transform.scale(entity.get_type().texture, entity.bounding_box.size, result)
        result.set_colorkey((255, 255, 255))
        # result = result.convert_alpha()
        return result

    def get_texture(self) -> Identifier:
        return GARBAGE_TEXTURE
