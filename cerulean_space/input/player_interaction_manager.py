import abc
from typing import TypeVar

import cerulean_space
from cerulean_space.entity.player_entity import PlayerEntity


class PlayerInteractionManager(metaclass=abc.ABCMeta):
    def __init__(self, game_mode: 'cerulean_space.world.game_mode.game_mode.GameMode'):
        self.game_mode = game_mode

    @abc.abstractmethod
    def handle_left(self, player: PlayerEntity):
        pass

    @abc.abstractmethod
    def handle_right(self, player: PlayerEntity):
        pass

    @abc.abstractmethod
    def handle_up(self, player: PlayerEntity):
        pass

    @abc.abstractmethod
    def handle_down(self, player: PlayerEntity):
        pass

    @abc.abstractmethod
    def handle_space(self, player: PlayerEntity):
        pass
