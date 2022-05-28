from abc import ABCMeta

from cerulean_space.entity.player_entity import PlayerEntity
from cerulean_space.input.player_interaction_manager import PlayerInteractionManager


class DefaultInteractionManager(PlayerInteractionManager, metaclass=ABCMeta):
    def handle_up(self, player: PlayerEntity):
        if player.attribute.fuel > 0:
            player.forward_vec += player.attribute.push_strength
            player.attribute.fuel -= 1
            player.update_mass()
