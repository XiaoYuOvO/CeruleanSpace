from cerulean_space.render.entity_renders.entity_renderer import EntityRenderer
from cerulean_space.util.identifier import Identifier

CLOUD_TEXTURE = Identifier("cloud.png")


class CloudRenderer(EntityRenderer):
    def get_texture(self) -> Identifier:
        return CLOUD_TEXTURE
