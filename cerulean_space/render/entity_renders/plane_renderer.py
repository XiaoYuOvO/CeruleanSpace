import pygame.transform
from pygame import Surface

from cerulean_space.entity.plane_entity import PlaneEntity, DIRECTION_LEFT, PlaneDirection, DIRECTION_RIGHT
from cerulean_space.render.entity_renders.entity_renderer import EntityRenderer
from cerulean_space.render.texture.stated_texture import StatedTexture
from cerulean_space.render.texture.texture import Texture
from cerulean_space.render.texture.transformable_variant_texture import TransformableVariantTexture, \
    TextureStateWithTransforms
from cerulean_space.render.texture.variant_texture import VariantTexture
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.util.identifier import Identifier

PLANE_TEXTURE = Identifier("plane.png")


class PlaneRenderer(EntityRenderer[PlaneEntity]):
    def __init__(self, texture_manager: TextureManager):
        self.plane_texture: TransformableVariantTexture[PlaneDirection] = TransformableVariantTexture({
            DIRECTION_LEFT: PLANE_TEXTURE,
            DIRECTION_RIGHT: PLANE_TEXTURE
        })
        super().__init__(texture_manager)

    def preprocess_texture(self, entity: PlaneEntity):
        if entity.direction == DIRECTION_LEFT:
            self.plane_texture.update(TextureStateWithTransforms(entity.direction, entity.get_bounding_box().size, 180))
        else:
            self.plane_texture.update(TextureStateWithTransforms(entity.direction, entity.get_bounding_box().size, 0))

    def get_texture(self) -> Texture:
        return self.plane_texture
