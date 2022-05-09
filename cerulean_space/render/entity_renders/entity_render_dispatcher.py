from typing import Dict, TypeVar, Any

from cerulean_space.entity.cloud_entity import CloudEntity
from cerulean_space.entity.entity import Entity
from cerulean_space.entity.garbage_entity import GarbageEntity
from cerulean_space.entity.plane_entity import PlaneEntity
from cerulean_space.entity.player_entity import PlayerEntity
from cerulean_space.entity.rock_entity import RockEntity
from cerulean_space.entity.space_station_entity import SpaceStationEntity
from cerulean_space.render.entity_renders.cloud_renderer import CloudRenderer
from cerulean_space.render.entity_renders.entity_renderer import EntityRenderer
from cerulean_space.render.entity_renders.garbage_renderer import GarbageRenderer
from cerulean_space.render.entity_renders.plane_renderer import PlaneRenderer
from cerulean_space.render.entity_renders.player_renderer import PlayerRenderer
from cerulean_space.render.entity_renders.rock_renderer import RockRenderer
from cerulean_space.render.entity_renders.space_station_renderer import SpaceStationRenderer
from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.render.world_renderer import WorldRenderer
from cerulean_space.world.world import World


class EntityRenderDispatcher(WorldRenderer):

    def render(self, game_renderer: GameRenderer):
        # 遍历所有实体,找到对应的渲染器,进行渲染
        for entity in self.world.entities:
            entity: Entity = entity
            self.renderers.get(type(entity)).render(entity, game_renderer)

    def __init__(self, world: World, texture_manager: TextureManager):
        super().__init__(world, texture_manager)
        self.renderers: Dict[Entity.__class__, EntityRenderer[Any]] = dict()
        # 注册所有实体的渲染器
        self.register_renderers(texture_manager)

    # 注册所有实体的渲染器
    def register_renderers(self, texture_manager: TextureManager):
        self.register_renderer(PlayerEntity, PlayerRenderer(texture_manager))
        self.register_renderer(RockEntity, RockRenderer(texture_manager))
        self.register_renderer(PlaneEntity, PlaneRenderer(texture_manager))
        self.register_renderer(CloudEntity, CloudRenderer(texture_manager))
        self.register_renderer(GarbageEntity, GarbageRenderer(texture_manager))
        self.register_renderer(SpaceStationEntity, SpaceStationRenderer(texture_manager))
        pass

    T = TypeVar("T", bound=Entity)

    # 注册单个实体的渲染器
    def register_renderer(self, entity_class: type(T.__class__), renderer: EntityRenderer[T]):
        self.renderers[entity_class] = renderer
