import abc
from typing import List

import cerulean_space
from cerulean_space.component.rocket_component import RocketComponent


class RocketBodyComponent(RocketComponent, metaclass=abc.ABCMeta):
    def __init__(self,strength: int, capacity: int):
        self.capacity = capacity
        self.strength = strength

    def apply_to_player(self, builder: 'cerulean_space.entity.player_entity.PlayerAttributeBuilder'):
        builder.capacity = self.capacity
        builder.max_health += self.strength
        pass

    def get_mass(self) -> int:
        pass

    def get_info_list(self) -> List[str]:
        pass