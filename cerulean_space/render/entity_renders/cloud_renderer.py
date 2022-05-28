from cerulean_space.render.entity_renders.entity_renderer import EntityRenderer
from cerulean_space.render.texture.simple_texture import SimpleTexture
from cerulean_space.render.texture.texture import Texture
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.util.identifier import Identifier


class CloudRenderer(EntityRenderer):
    def __init__(self, texture_manager: TextureManager):
        self.cloud_texture = SimpleTexture(Identifier("cloud.png"))
        super().__init__(texture_manager)

    def get_texture(self) -> Texture:
        return self.cloud_texture

