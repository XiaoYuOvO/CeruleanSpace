from typing import Tuple, ValuesView

from cerulean_space.component.component_manager import ComponentManager
from cerulean_space.component.component_type import ComponentType
from cerulean_space.component.rocket_component import RocketComponent
from cerulean_space.render.game_renderer import GameRenderer


class ComponentRenderer:
    def __init__(self, manager: ComponentManager):
        self.manager = manager

    def renderer(self, game_renderer: GameRenderer, render_pos: Tuple[int, int]):
        components: ValuesView[ComponentType,RocketComponent] = self.manager.components.values()
        for component in components:
            component

