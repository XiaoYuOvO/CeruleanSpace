import pygame
from pygame import Surface

from cerulean_space.entity.garbage_entity import GarbageEntity
from cerulean_space.render.entity_renders.entity_renderer import EntityRenderer
from cerulean_space.util.identifier import Identifier

GARBAGE_TEXTURE = Identifier("garbage.png")


class GarbageRenderer(EntityRenderer[GarbageEntity]):
    def preprocess_texture(self, entity: GarbageEntity, surface: Surface) -> Surface:
        # self.texture.set_colorkey((255, 255, 255))
        result = Surface(entity.bounding_box.size)
        result.fill((255, 255, 255))
        pygame.transform.scale(self.texture, entity.bounding_box.size, result)
        result.set_colorkey((255, 255, 255))
        # result = result.convert_alpha()
        return result

    def get_texture(self) -> Identifier:
        return GARBAGE_TEXTURE
