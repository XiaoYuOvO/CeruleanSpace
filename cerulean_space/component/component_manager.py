import collections
from collections import OrderedDict

import cerulean_space
from cerulean_space.component.component_type import ComponentType, ComponentTypes
from cerulean_space.component.rocket_component import RocketComponent


class ComponentManager:
    def __init__(self):
        self.components: OrderedDict[ComponentType, RocketComponent] = collections.OrderedDict()
        for t in ComponentTypes.VALUES:
            self.components[t] = t.components[0]

    def size(self) -> int:
        return self.components.__len__()

    def set_component(self, t: ComponentType, component: RocketComponent):
        self.components[t] = component

    def apply_component_to_player_attribute(self, builder: 'cerulean_space.entity.player_entity.PlayerAttributeBuilder') \
            -> 'cerulean_space.entity.player_entity.PlayerAttributeBuilder':
        for component in self.components.values():
            component.apply_to_player(builder)
        return builder
