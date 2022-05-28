from cerulean_space.constants import COLLECT_MODE_TIME, MIN_GARBAGE_COUNT_TO_WIN, PLAYER_COLLECT_MIN_HEIGHT, \
    PLAYER_COLLECT_MAX_HEIGHT
from cerulean_space.input.collect_interaction_manager import CollectInteractionManager
from cerulean_space.input.player_interaction_manager import PlayerInteractionManager
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.render.ui.game_mode.collect_game_mode_renderer import CollectGameModeUIRenderer
from cerulean_space.render.ui.hover_text import HoverText
from cerulean_space.world.game_mode.game_mode import GameMode


class CollectGameMode(GameMode):
    def construct_renderer(self, world, texture_manager: TextureManager):
        return CollectGameModeUIRenderer(world, texture_manager)

    def __init__(self):
        self.interaction_manager = CollectInteractionManager(self)
        self.garbage_collected = 0
        self.collect_time = COLLECT_MODE_TIME

    def on_mode_start(self, world):
        world.player.min_y = PLAYER_COLLECT_MIN_HEIGHT
        world.player.max_y = PLAYER_COLLECT_MAX_HEIGHT
        world.player.lock_rotation = False
        world.player.start_collect_mode()
        world.add_hover_text(HoverText("在有限的时间内收集足够的太空垃圾！",
                                       world.game.game_renderer.get_rendering_width() / 2,
                                       world.game.game_renderer.get_rendering_height() / 3, 300, 50))

    def tick_game_mode(self, world):
        if self.collect_time >= 0:
            self.collect_time -= 1
            if self.collect_time <= 0:
                if self.garbage_collected < MIN_GARBAGE_COUNT_TO_WIN:
                    world.collect_failed(self.garbage_collected)
                else:
                    world.game_win()
        if self.garbage_collected >= MIN_GARBAGE_COUNT_TO_WIN:
            world.game_win()

    def write_to_json(self) -> dict:
        data = super(CollectGameMode, self).write_to_json()
        data["collect_time"] = self.collect_time
        data["garbage_collected"] = self.garbage_collected
        return data

    def read_from_json(self, data: dict):
        super(CollectGameMode, self).read_from_json(data)
        self.collect_time = data.get("collect_time")
        self.garbage_collected = data.get("garbage_collected")

    def get_interaction_manager(self) -> PlayerInteractionManager:
        return self.interaction_manager

    @staticmethod
    def get_name() -> str:
        return "collect"
