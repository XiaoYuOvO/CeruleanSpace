from cerulean_space.component.rocket_construction import RocketConstruction
from cerulean_space.input.constructing_interaction_manager import ConstructingInteractionManager
from cerulean_space.input.player_interaction_manager import PlayerInteractionManager
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.render.ui.game_mode.constructing_game_mode_renderer import ConstructingGameModeUIRenderer
from cerulean_space.world.game_mode.game_mode import GameMode


class ConstructingGameMode(GameMode):
    def __init__(self):
        self.rocket_construction = RocketConstruction()
        self.interaction_manager = ConstructingInteractionManager(self)

    def get_interaction_manager(self) -> PlayerInteractionManager:
        return self.interaction_manager

    def construct_renderer(self, world, texture_manager: TextureManager):
        return ConstructingGameModeUIRenderer(world, texture_manager)

    @staticmethod
    def get_name() -> str:
        return "constructing"
