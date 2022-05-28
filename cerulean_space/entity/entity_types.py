from typing import TypeVar, Dict

import cerulean_space.entity.cloud_entity as cloud_entity_file
import cerulean_space.entity.entity as entity_file
import cerulean_space.entity.garbage_entity as garbage_entity_file
import cerulean_space.entity.oil_bucket_entity as oil_bucket_entity_file
import cerulean_space.entity.plane_entity as plane_entity_file
import cerulean_space.entity.player_entity as player_entity_file
import cerulean_space.entity.rock_entity as rock_entity_file
import cerulean_space.entity.space_station_entity as space_station_entity_file

T = TypeVar("T", bound=entity_file.Entity)


class EntityType:
    def __init__(self, name: str, ctor: type):  # 构造器应为__init__(self,World),但此处为了防止循环引用,使用Any
        self.name = name
        self.ctor = ctor

    def construct_entity(self, world) -> T:
        return self.ctor(world)


ENTITY_TYPES: Dict[str, EntityType] = dict()


def register_entity_type(entity_class: type(T)):
    ENTITY_TYPES[entity_class.get_codec_name()] = EntityType(entity_class.get_codec_name(), entity_class)


register_entity_type(cloud_entity_file.CloudEntity)
register_entity_type(space_station_entity_file.SpaceStationEntity)
register_entity_type(garbage_entity_file.GarbageEntity)
register_entity_type(oil_bucket_entity_file.OilBucketEntity)
register_entity_type(plane_entity_file.PlaneEntity)
register_entity_type(player_entity_file.PlayerEntity)
register_entity_type(rock_entity_file.RockEntity)
