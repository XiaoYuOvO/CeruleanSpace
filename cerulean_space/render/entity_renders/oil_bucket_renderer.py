from cerulean_space.entity.oil_bucket_entity import OilBucketEntity
from cerulean_space.render.entity_renders.entity_renderer import EntityRenderer
from cerulean_space.render.texture.simple_texture import SimpleTexture
from cerulean_space.render.texture.texture import Texture
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.util.identifier import Identifier


class OilBucketRenderer(EntityRenderer[OilBucketEntity]):
    def __init__(self, texture_manager: TextureManager):
        self.oil_bucket_texture = SimpleTexture(Identifier("oil_bucket.png"))
        super().__init__(texture_manager)

    def get_texture(self) -> Texture:
        return self.oil_bucket_texture
