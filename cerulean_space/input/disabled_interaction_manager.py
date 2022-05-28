from cerulean_space.entity.player_entity import PlayerEntity
from cerulean_space.input.player_interaction_manager import PlayerInteractionManager


class DisabledInteractionManager(PlayerInteractionManager):
    def handle_left(self, player: PlayerEntity):
        pass

    def handle_right(self, player: PlayerEntity):
        pass

    def handle_up(self, player: PlayerEntity):
        pass

    def handle_down(self, player: PlayerEntity):
        pass

    def handle_space(self, player: PlayerEntity):
        pass
