from cerulean_space.entity.space_station_entity import SpaceStationEntity
from cerulean_space.render.entity_renders.entity_renderer import EntityRenderer
from cerulean_space.util.identifier import Identifier

SPACE_STATION_TEXTURE = Identifier("space_station.png")


class SpaceStationRenderer(EntityRenderer[SpaceStationEntity]):
    def get_texture(self) -> Identifier:
        return SPACE_STATION_TEXTURE
