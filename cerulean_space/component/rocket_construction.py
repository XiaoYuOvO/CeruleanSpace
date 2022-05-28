from typing import List

from cerulean_space.component.component_manager import ComponentManager
from cerulean_space.component.component_type import ComponentType, ComponentTypes
from cerulean_space.component.rocket_component import RocketComponent
from cerulean_space.entity.player_entity import PlayerAttribute, PlayerEntity, PlayerAttributeBuilder
from cerulean_space.util.math.math_helper import MathHelper


class RocketConstruction:

    def __init__(self):
        self.component_manager = ComponentManager()
        self.selected_part: int = 0

    def move_cursor_up(self):
        self.selected_part = MathHelper.min(self.selected_part + 1, self.component_manager.size())

    def move_cursor_down(self):
        self.selected_part = MathHelper.max(self.selected_part - 1, 0)

    def switch_next_component(self):
        t: ComponentType = ComponentTypes.VALUES[self.selected_part]
        available_component: List[RocketComponent] = t.components
        self.component_manager.set_component(t, available_component[
            MathHelper.min(self.selected_part + 1, available_component.__len__() - 1)])

    def switch_former_component(self):
        t: ComponentType = ComponentTypes.VALUES[self.selected_part]
        available_component: List[RocketComponent] = t.components
        self.component_manager.set_component(t, available_component[
            MathHelper.min(self.selected_part - 1, 0)])

    def apply_to_player(self, player: PlayerEntity):
        player.components = self.component_manager
        player.attribute = self.__build_attributes()

    def __build_attributes(self) -> PlayerAttribute:
        return self.component_manager.apply_component_to_player_attribute(PlayerAttributeBuilder()).build()
