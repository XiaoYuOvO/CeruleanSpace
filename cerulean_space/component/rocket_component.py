import abc
from typing import List

from pygame import Rect

import cerulean_space
from cerulean_space.render.texture.texture import Texture


class RocketComponent(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def apply_to_player(self, builder: 'cerulean_space.entity.player_entity.PlayerAttributeBuilder'):
        pass

    @abc.abstractmethod
    def get_bounding_box(self) -> Rect:
        pass

    @abc.abstractmethod
    def get_mass(self) -> int:
        pass

    @abc.abstractmethod
    def get_texture(self) -> Texture:
        pass

    @abc.abstractmethod
    def get_display_name(self) -> str:
        pass

    @abc.abstractmethod
    def get_codec_name(self) -> str:
        pass

    @abc.abstractmethod
    def get_info_list(self) -> List[str]:
        pass
