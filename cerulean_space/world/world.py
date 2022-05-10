from random import Random
from typing import List, Any, NoReturn, Dict

from pygame import Rect
from pygame.draw_py import BoundingBox

from cerulean_space.constants import PLAYER_COLLECT_MAX_HEIGHT, COLLECT_MODE_TIME, MIN_GARBAGE_COUNT_TO_WIN
from cerulean_space.entity.entity import Entity
from cerulean_space.entity.entity_types import EntityType, ENTITY_TYPES
from cerulean_space.entity.player_entity import PlayerEntity
from cerulean_space.render.particle.particle_manager import ParticleManager
from cerulean_space.render.particle.particle_parameter import ParticleParameter
from cerulean_space.render.particle.particle_types import ParticleType
from cerulean_space.render.ui.hover_text import HoverText
from cerulean_space.world.game_mode import GameModes
from cerulean_space.world.generation.entity_spawner import EntitySpawner
from cerulean_space.world.generation.spawn_entry import SpawnEntry
from cerulean_space.world.generation.spawn_factory import SpawnFactories, FACTORIES


class World:
    def __init__(self, game_instance):
        """
        :var self.rand :该世界的随机函数
        :var self.wind_force todo
        :var self.entities 该世界的实体列表
        :var self.weight 该世界的宽度
        :var self.height 该世界的高度

        """
        self.rand: Random = Random()
        self.wind_force = 0.0
        self.time_to_next_wind_force = 0
        self.player = PlayerEntity(self)
        # 实体列表,全部继承Entity
        self.entities: List[Entity] = list()

        self.weight = 100
        self.height = 100000
        self.game = game_instance
        self.entity_spawner = EntitySpawner(self)
        self.particle_manager = ParticleManager()
        self.game_mode = GameModes.FLY
        self.hover_texts: List[HoverText] = list()
        self.collect_time = COLLECT_MODE_TIME
        self.garbage_collected = 0

    def add_entity(self, entity: Entity):
        # if coordinate not in self.entities.key-s():
        if type(entity) is PlayerEntity:
            self.player = entity
        self.entities.append(entity)
        # entity.set_pos(tuple(coordinate))

    def add_hover_text(self, text: HoverText):
        self.hover_texts.append(text)
        pass

    def tick(self):
        for e in self.entities:
            e.tick()
            if e.tick_exist % 5 == 0:
                e.set_pos((e.get_x() + self.wind_force, e.get_y()))
            if e.removed:
                self.entities.remove(e)
        self.entity_spawner.tick_spawn(self.rand, self.player)
        self.particle_manager.tick_particles()
        for t in self.hover_texts:
            t.display_time -= 1
            if t.display_time <= 0:
                self.hover_texts.remove(t)
        if not self.is_collect_mode():
            if self.time_to_next_wind_force <= 0:
                self.wind_force = self.rand.randrange(-5, 5)
                self.time_to_next_wind_force = self.rand.randrange(300, 1800)
            else:
                self.time_to_next_wind_force -= 1
        if self.is_collect_mode() and self.collect_time >= 0:
            self.collect_time -= 1
            if self.collect_time <= 0:
                self.finish_collect()

    def add_particle(self, particle_type: ParticleType, parameter: ParticleParameter):
        self.particle_manager.add_particle(particle_type.create_particle(self, parameter))

    def get_collided_entity(self, entity) -> List[Entity]:
        result = list()
        for e in self.entities:
            if e is not entity and not e.no_collide() and entity.bounding_box.colliderect(e.bounding_box):
                result.append(e)
        return result

    def finish_collect(self):
        if self.garbage_collected < MIN_GARBAGE_COUNT_TO_WIN:
            self.collect_failed()
        else:
            self.game_win()

    def try_commit_collecting(self):
        if self.garbage_collected >= MIN_GARBAGE_COUNT_TO_WIN:
            self.game_win()

    def is_collect_mode(self) -> bool:
        return self.game_mode is GameModes.COLLECT

    def init_game_mode(self):
        if self.is_collect_mode():
            self.start_with_collect_mode()

    def switch_to_collect_mode(self):
        self.player.switch_to_collect_mode()
        self.add_hover_text(HoverText("你已成功飞入太空！",
                                      self.game.game_renderer.get_rendering_width() / 2,
                                      self.game.game_renderer.get_rendering_height() / 3, 300, 50))
        self.game.unlock_camera()
        self.wind_force = 0

    def start_collect_mode(self):
        self.player.start_collect_mode()
        self.game.lock_camera()
        self.wind_force = 0
        self.game_mode = GameModes.COLLECT
        self.add_hover_text(HoverText("在有限的时间内收集足够的太空垃圾！",
                                      self.game.game_renderer.get_rendering_width() / 2,
                                      self.game.game_renderer.get_rendering_height() / 3, 300, 50))

    def start_with_collect_mode(self):
        self.add_hover_text(HoverText("在有限的时间内收集足够的太空垃圾！",
                                      self.game.game_renderer.get_rendering_width() / 2,
                                      self.game.game_renderer.get_rendering_height() / 3, 300, 50))
        self.player.switch_to_collect_mode()
        self.player.start_collect_mode()

    def read_world(self, data: dict) -> NoReturn:
        for entity_data in data.get("entities"):  # entities: List[Dict[str,? extends Entity]]
            entity_type = ENTITY_TYPES.get(entity_data.get("type"))
            new_entity = entity_type.construct_entity(self)
            new_entity.read_from_json(entity_data.get("data"))
            if type(new_entity) is PlayerEntity:
                self.player = new_entity
            self.add_entity(new_entity)
        for spawn_entry_data in data.get("spawn_entries"):
            self.entity_spawner.spawn_list.append(SpawnEntry(spawn_entry_data.get("spawn_y"),
                                                             FACTORIES.get(
                                                                 spawn_entry_data.get("factory"))))
        self.game_mode = GameModes[(data.get("game_mode"))]
        self.wind_force = data.get("wind_force")
        self.collect_time = data.get("collect_time")
        self.garbage_collected = data.get("garbage_collected")
        self.time_to_next_wind_force = data.get("time_to_next_wind_force")
        self.init_game_mode()

    def write_world(self) -> dict:
        result = dict()
        entities = list()
        for entity in self.entities:
            entities.append({
                "type": entity.get_codec_name(),
                "data": entity.write_to_json()
            })
        spawn_entries = list()
        for spawn_entry in self.entity_spawner.spawn_list:
            spawn_entries.append({
                "spawn_y": spawn_entry.spawn_y,
                "factory": spawn_entry.factory.name
            })
        result["spawn_entries"] = spawn_entries
        result["entities"] = entities
        result["wind_force"] = self.wind_force
        result["game_mode"] = self.game_mode.name
        result["collect_time"] = self.collect_time
        result["garbage_collected"] = self.garbage_collected
        result['time_to_next_wind_force'] = self.time_to_next_wind_force
        return result

    def add_spawn_entry(self, entry):
        self.entity_spawner.spawn_list.append(entry)

    def game_win(self):
        self.game.game_win()

    def game_over(self):
        self.game.game_over()

    def collect_failed(self):
        self.game.collect_failed()
