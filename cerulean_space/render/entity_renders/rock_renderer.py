from cerulean_space.entity.rock_entity import RockEntity
from cerulean_space.render.entity_renders.entity_renderer import EntityRenderer
from cerulean_space.util.identifier import Identifier

rock_texture = Identifier("rock.png")


class RockRenderer(EntityRenderer[RockEntity]):
    def get_texture(self) -> Identifier:
        return rock_texture
