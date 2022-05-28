from typing import Tuple, Generic, Dict

import pygame
from pygame import Surface

from cerulean_space.render.texture.stated_texture import TextureState, S
from cerulean_space.render.texture.variant_texture import VariantTexture
from cerulean_space.util.identifier import Identifier


class TextureStateWithTransforms(Generic[S], TextureState):
    def __init__(self, delegate: S, size: Tuple[int, int], rotation: float = 0):
        self.delegate = delegate
        self.size = size
        self.rotation = rotation

    def __hash__(self):
        return self.size.__hash__() * 7 + self.rotation.__hash__()

    def __eq__(self, other):
        return type(other) is TextureStateWithTransforms \
               and other.delegate == self.delegate \
               and other.size == self.size \
               and other.rotation == self.rotation


class TransformableVariantTexture(VariantTexture[TextureStateWithTransforms]):
    def __init__(self, variant_mapper: Dict[S, Identifier]):
        super(TransformableVariantTexture, self).__init__(variant_mapper)

    def _create_texture_from_state(self, s: TextureStateWithTransforms) -> Surface:
        tex = super(TransformableVariantTexture, self)._create_texture_from_state(s.delegate)
        changed = False
        result = Surface(s.size)

        if tex.get_size() is not s.size:
            result.fill((255, 255, 255))
            pygame.transform.scale(tex, s.size, result)
            result.set_colorkey((255, 255, 255))
            changed = True

        if s.rotation is not 0:
            result = pygame.transform.rotate(result, s.rotation)
            changed = True

        if changed:
            return result
        else:
            return tex

    def update(self, s: TextureStateWithTransforms):
        super(TransformableVariantTexture, self).update(s)
