from random import Random
from typing import List, NoReturn

import cerulean_space
import cerulean_space.entity.entity as et
import cerulean_space.world.game_mode.game_modes as game_modes_file
from cerulean_space.entity.entity_types import ENTITY_TYPES
from cerulean_space.entity.player_entity import PlayerEntity, PlayerAttributeBuilder
from cerulean_space.render.particle.particle_manager import ParticleManager
from cerulean_space.render.particle.particle_parameter import ParticleParameter
from cerulean_space.render.particle.particle_types import ParticleType
from cerulean_space.render.ui.hover_text import HoverText
from cerulean_space.world.game_mode.game_mode import GameMode
from cerulean_space.world.generation.entity_spawner import EntitySpawner
from cerulean_space.world.generation.spawn_entry import SpawnEntry
from cerulean_space.world.generation.spawn_factory import FACTORIES


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
        self.player: PlayerEntity = PlayerEntity(self)
        # 实体列表,全部继承Entity
        self.entities: List[et.Entity] = list()
        self.weight: int = 100
        self.height: int = 100000
        self.game: 'cerulean_space.game.CeruleanSpace' = game_instance
        self.entity_spawner = EntitySpawner(self)
        self.particle_manager = ParticleManager()
        self.game_mode: GameMode = game_modes_file.GameModes.FLY
        self.hover_texts: List[HoverText] = list()

    def add_entity(self, entity: 'cerulean_space.entity.entity.Entity'):
        # if coordinate not in self.entities.key-s():
        if type(entity) is PlayerEntity:
            self.player = entity
        self.entities.append(entity)
        # entity.set_pos(tuple(coordinate))

    def add_hover_text(self, text: HoverText):
        self.hover_texts.append(text)

    def tick(self):
        for e in self.entities:
            e.tick()
            if e.removed:
                self.entities.remove(e)
        self.entity_spawner.tick_spawn(self.rand, self.player)
        self.particle_manager.tick_particles()
        for t in self.hover_texts:
            t.display_time -= 1
            if t.display_time <= 0:
                self.hover_texts.remove(t)
        self.game_mode.tick_game_mode(self)

    def add_particle(self, particle_type: ParticleType, parameter: ParticleParameter):
        self.particle_manager.add_particle(particle_type.create_particle(self, parameter))

    def get_collided_entity(self, entity) -> List[et.Entity]:
        result = list()
        for e in self.entities:
            if e is not entity and not e.no_collide() and entity.bounding_box.colliderect(e.bounding_box):
                result.append(e)
        return result

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
        gamemode = game_modes_file.GameModes.get_from_name(data.get("game_mode"))
        self.switch_to_mode(gamemode)
        self.game_mode = gamemode
        self.game_mode.read_from_json(data.get("game_mode_data"))

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
        result["game_mode"] = self.game_mode.get_name()
        result["game_mode_data"] = self.game_mode.write_to_json()
        return result

    def add_spawn_entry(self, entry):
        self.entity_spawner.spawn_list.append(entry)

    def game_win(self):
        self.game.game_win()

    def game_over(self):
        self.game.game_over()

    def collect_failed(self, garbage_collected: int):
        self.game.collect_failed(garbage_collected)

    def switch_to_mode(self, gamemode):
        if gamemode is not self.game_mode:
            self.game_mode.on_mode_end(self)
            self.game_mode = gamemode
            self.game_mode.on_mode_start(self)
