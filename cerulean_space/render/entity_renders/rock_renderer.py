from cerulean_space.entity.rock_entity import RockEntity
from cerulean_space.render.entity_renders.entity_renderer import EntityRenderer
from cerulean_space.render.texture.stated_texture import TextureState
from cerulean_space.render.texture.texture import Texture
from cerulean_space.render.texture.transformable_variant_texture import TransformableVariantTexture, \
    TextureStateWithTransforms
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.util.identifier import Identifier


class RockState(TextureState):
    def __hash__(self):
        return 0


INSTANCE = RockState()


class RockRenderer(EntityRenderer[RockEntity]):
    def __init__(self, texture_manager: TextureManager):
        self.rock_texture = TransformableVariantTexture({INSTANCE: Identifier("rock2.png")})
        super().__init__(texture_manager)

    def preprocess_texture(self, entity: RockEntity):
        # self.texture.set_colorkey((255, 255, 255))
        # result = Surface(entity.bounding_box.size)
        # result.fill((255, 255, 255))
        # pygame.transform.scale(self.texture, entity.bounding_box.size, result)
        # result.set_colorkey((255, 255, 255))
        # result = result.convert_alpha()
        self.rock_texture.update(TextureStateWithTransforms(INSTANCE, entity.bounding_box.size))

    def get_texture(self) -> Texture:
        return self.rock_texture
