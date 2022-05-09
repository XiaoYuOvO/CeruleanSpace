from cerulean_space.entity.garbage_entity import GarbageEntity
from cerulean_space.render.entity_renders.entity_renderer import EntityRenderer
from cerulean_space.util.identifier import Identifier

GARBAGE_TEXTURE = Identifier("garbage.png")


class GarbageRenderer(EntityRenderer[GarbageEntity]):
    def get_texture(self) -> Identifier:
        return GARBAGE_TEXTURE
