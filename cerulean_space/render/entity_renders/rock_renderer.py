import pygame.transform
from pygame import Surface, Color

from cerulean_space.entity.rock_entity import RockEntity
from cerulean_space.render.entity_renders.entity_renderer import EntityRenderer
from cerulean_space.util.identifier import Identifier

rock_texture = Identifier("rock.png")


class RockRenderer(EntityRenderer[RockEntity]):
    def preprocess_texture(self, entity: RockEntity, surface: Surface) -> Surface:
        # self.texture.set_colorkey((255, 255, 255))
        result = Surface(entity.bounding_box.size)
        # result.fill((255, 255, 255))
        result = pygame.transform.scale(self.texture, entity.bounding_box.size, result)
        result.set_colorkey((255, 255, 255))
        # result = result.convert_alpha()
        return result

    def get_texture(self) -> Identifier:
        return rock_texture
