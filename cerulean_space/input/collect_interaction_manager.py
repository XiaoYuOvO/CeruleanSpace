from cerulean_space.entity.player_entity import PlayerEntity
from cerulean_space.input.default_interaction_manager import DefaultInteractionManager
from cerulean_space.util.math.math_helper import MathHelper


class CollectInteractionManager(DefaultInteractionManager):
    def handle_left(self, player: PlayerEntity):
        player.rotation = player.rotation - player.attribute.rotation_speed
        pass

    def handle_right(self, player: PlayerEntity):
        player.rotation = player.rotation + player.attribute.rotation_speed
        pass

    def handle_down(self, player: PlayerEntity):
        player.forward_vec = MathHelper.max(player.forward_vec - player.attribute.push_strength, player.attribute.min_speed)
        pass

    def handle_space(self, player: PlayerEntity):
        pass
