from typing import TypeVar, Callable, Dict, Any

from cerulean_space.entity.entity import Entity
from cerulean_space.entity.garbage_entity import GarbageEntity
from cerulean_space.entity.plane_entity import PlaneEntity
from cerulean_space.entity.player_entity import PlayerEntity
from cerulean_space.entity.rock_entity import RockEntity
from cerulean_space.entity.cloud_entity import CloudEntity
from cerulean_space.entity.space_station_entity import SpaceStationEntity

T = TypeVar("T", bound=Entity)


class EntityType:
    def __init__(self, name: str, ctor: type):  # 构造器应为__init__(self,World),但此处为了防止循环引用,使用Any
        self.name = name
        self.ctor = ctor

    def construct_entity(self, world) -> T:
        return self.ctor(world)


ENTITY_TYPES: Dict[str, EntityType] = dict()


def register_entity_type(entity_class: type(T)):
    ENTITY_TYPES[entity_class.get_codec_name()] = EntityType(entity_class.get_codec_name(), entity_class)


register_entity_type(PlayerEntity)
register_entity_type(RockEntity)
register_entity_type(PlaneEntity)
register_entity_type(CloudEntity)
register_entity_type(GarbageEntity)
register_entity_type(SpaceStationEntity)
