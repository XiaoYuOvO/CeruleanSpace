import abc
from typing import List

import cerulean_space
from cerulean_space.component.rocket_component import RocketComponent


class RocketTailComponent(metaclass=abc.ABCMeta, RocketComponent):
    def __init__(self, fuel_count: int, push_strength: float):
        self.fuel_count = fuel_count
        self.push_strength = push_strength
        self.info_list = ["火箭的尾部推进器以及燃料储存仓",
                          "燃料数量:" + self.fuel_count.__str__(),
                          "推进强度:" + self.push_strength.__str__(),
                          "重量:" + self.get_mass().__str__()]

    def apply_to_player(self, builder: 'cerulean_space.entity.player_entity.PlayerAttributeBuilder'):
        builder.max_fuel = self.fuel_count
        builder.push_strength = self.push_strength

    def get_mass(self) -> int:
        return round(self.fuel_count / 10 + self.push_strength * 2)

    def get_info_list(self) -> List[str]:
        return self.info_list
