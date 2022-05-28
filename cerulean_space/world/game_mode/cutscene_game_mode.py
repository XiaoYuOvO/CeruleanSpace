from cerulean_space.constants import PLAYER_COLLECT_MIN_HEIGHT
from cerulean_space.entity.player_entity import PlayerEntity
from cerulean_space.input.disabled_interaction_manager import DisabledInteractionManager
from cerulean_space.input.player_interaction_manager import PlayerInteractionManager
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.render.ui.game_mode.empty_game_mode_renderer import EmptyGameModeUIRenderer
from cerulean_space.render.ui.hover_text import HoverText
from cerulean_space.world.game_mode.game_mode import GameMode
import cerulean_space.world.game_mode.game_modes as gamemodes



class CutsceneGameMode(GameMode):
    def construct_renderer(self, world, texture_manager: TextureManager):
        return EmptyGameModeUIRenderer(world, texture_manager)

    def __init__(self):
        self.interaction_manager = DisabledInteractionManager(self)

    def on_mode_start(self, world):
        world.player.switch_to_collect_mode()
        world.add_hover_text(HoverText("你已成功飞入太空！",
                                       world.game.game_renderer.get_rendering_width() / 2,
                                       world.game.game_renderer.get_rendering_height() / 3, 300, 50))

    def camera_locked(self) -> bool:
        return False

    def get_interaction_manager(self) -> PlayerInteractionManager:
        return self.interaction_manager

    def tick_game_mode(self, world):
        if world.player.get_y() >= PLAYER_COLLECT_MIN_HEIGHT:
            world.player.min_y = PLAYER_COLLECT_MIN_HEIGHT
            world.switch_to_mode(gamemodes.GameModes.COLLECT)

    @staticmethod
    def get_name() -> str:
        return "cutscene"
