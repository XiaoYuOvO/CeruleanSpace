from pygame import Rect

from cerulean_space.entity.entity import Entity


class CloudEntity(Entity):
    def get_bounding_box(self) -> Rect:
        return Rect(0, 0, 140, 60)

    @staticmethod
    def get_codec_name() -> str:
        return "cloud"

    def no_collide(self) -> bool:
        return True
