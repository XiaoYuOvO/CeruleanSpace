from typing import Generic, Dict

from pygame import Surface

from cerulean_space.render.texture.stated_texture import StatedTexture, S
from cerulean_space.util.identifier import Identifier


class VariantTexture(Generic[S], StatedTexture[S]):
    def __init__(self, variant_mapper: Dict[S, Identifier]):
        super().__init__()
        self.variant_mapper = variant_mapper

    def _create_texture_from_state(self, s: S) -> Surface:
        return self.texture_loader.load_or_get_texture(self.variant_mapper[s])
