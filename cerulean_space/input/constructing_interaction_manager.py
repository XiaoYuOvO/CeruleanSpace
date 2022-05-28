from cerulean_space.component.rocket_construction import RocketConstruction
from cerulean_space.entity.player_entity import PlayerEntity
from cerulean_space.input.player_interaction_manager import PlayerInteractionManager


class ConstructingInteractionManager(PlayerInteractionManager):
    def __init__(self, game_mode):
        super().__init__(game_mode)

    def handle_left(self, player: PlayerEntity):
        self.game_mode.rocket_construction.switch_former_component()

    def handle_right(self, player: PlayerEntity):
        self.game_mode.rocket_construction.switch_next_component()

    def handle_up(self, player: PlayerEntity):
        self.game_mode.rocket_construction.

    def handle_down(self, player: PlayerEntity):
        pass

    def handle_space(self, player: PlayerEntity):
        pass