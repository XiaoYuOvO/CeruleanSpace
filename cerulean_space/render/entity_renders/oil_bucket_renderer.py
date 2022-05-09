from cerulean_space.entity.oil_bucket_entity import OilBucketEntity
from cerulean_space.render.entity_renders.entity_renderer import EntityRenderer
from cerulean_space.util.identifier import Identifier

OIL_BUCKET_TEXTURE = Identifier("oil_bucket.png")


class OilBucketRenderer(EntityRenderer[OilBucketEntity]):
    def get_texture(self) -> Identifier:
        return OIL_BUCKET_TEXTURE
