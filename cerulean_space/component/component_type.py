from typing import List

from cerulean_space.component.rocket_component import RocketComponent


class ComponentType:
    def __init__(self, components: List[RocketComponent]):
        self.components = components


class ComponentTypes:
    VALUES: List[ComponentType] = list()

    @staticmethod
    def register_type(t: ComponentType) -> ComponentType:
        ComponentTypes.VALUES.append(t)
        return t

