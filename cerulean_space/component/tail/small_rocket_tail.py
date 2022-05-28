from pygame import Rect

from cerulean_space.component.tail.rocket_tail_component import RocketTailComponent
from cerulean_space.render.texture.texture import Texture
from cerulean_space.util.identifier import Identifier


class SmallRocketTailComponent(RocketTailComponent):
    def __init__(self):
        super().__init__(100, 1)

    def get_bounding_box(self) -> Rect:
        return Rect(0,0,80,70)

    def get_texture(self) -> Texture:
        return Texture(Identifier("components/tail/small.png"))

    def get_display_name(self) -> str:
        return "小型火箭推进器"

    def get_codec_name(self) -> str:
        return "small_rocket_tail"
