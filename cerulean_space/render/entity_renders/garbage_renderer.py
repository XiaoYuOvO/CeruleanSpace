from typing import Dict

from cerulean_space.entity.garbage_entity import GarbageEntity, GarbageTypes, GarbageType
from cerulean_space.render.entity_renders.entity_renderer import EntityRenderer
from cerulean_space.render.texture.transformable_variant_texture import TransformableVariantTexture, TextureStateWithTransforms
from cerulean_space.render.texture.texture import Texture
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.util.identifier import Identifier


class GarbageRenderer(EntityRenderer[GarbageEntity]):
    def __init__(self, texture_manager: TextureManager):
        type_map: Dict[GarbageType, Identifier] = dict()
        for e in GarbageTypes.VALUES:
            garbage_type: GarbageType = e
            type_map[garbage_type] = (Identifier(garbage_type.name + ".png"))
        self.garbage_texture: TransformableVariantTexture = TransformableVariantTexture(type_map)
        super().__init__(texture_manager)

    def preprocess_texture(self, entity: GarbageEntity):
        self.garbage_texture.update(TextureStateWithTransforms(entity.get_type(), entity.get_bounding_box().size))

    def get_texture(self) -> Texture:
        return self.garbage_texture
