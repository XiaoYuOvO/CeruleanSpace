import abc
import math
from typing import NoReturn, Tuple

import pygame.math
from pygame import Rect

from cerulean_space.io.codec import Codec


class Entity(metaclass=abc.ABCMeta):

    def __init__(self, world):
        self.bounding_box = self.get_bounding_box()
        self.world = world
        self.velocity = pygame.math.Vector2(0.0, 0.0)
        self.forward_vec = 0
        self.__x: float = 0.0
        self.__y: float = 0.0
        self.rotation = 0.0
        self.rad_rotation = 0.0
        self.tick_exist = 0
        self.mass = 1
        self.removed = False

    @abc.abstractmethod
    def get_bounding_box(self) -> Rect:
        pass

    def on_collided_with(self, other) -> NoReturn:
        pass

    def remove(self) -> NoReturn:
        self.removed = True

    def tick(self):
        if not self.removed:
            self.rad_rotation = math.radians(self.rotation)
            self.set_pos((self.__x + self.velocity.x + self.forward_vec * math.sin(self.rad_rotation),
                          self.__y + self.velocity.y + self.forward_vec * math.cos(self.rad_rotation)))
            self.tick_exist += 1
            self.living_tick()
        pass

    def set_pos(self, pos: Tuple[float, float]) -> NoReturn:
        self.__x = pos[0]
        self.__y = pos[1]
        self.bounding_box.x = self.__x - self.bounding_box.width / 2
        self.bounding_box.y = self.__y - self.bounding_box.height / 2

    def get_x(self) -> float:
        return self.__x

    def get_y(self) -> float:
        return self.__y

    def get_rendering_y(self) -> int:
        return round(-self.__y)

    def get_rendering_x(self) -> int:
        return round(self.__x)

    def living_tick(self):
        pass

    def read_from_json(self, data: dict):
        self.velocity = Codec.decode_vec2(data.get("velocity"))
        self.forward_vec = data["forward_vec"]
        self.__x = data["x"]
        self.__y = data["y"]
        self.rotation = data["rotation"]
        self.tick_exist = data["tick_exist"]
        self.mass = data["mass"]
        self.removed = data["removed"]
        pass

    def write_to_json(self) -> dict:
        return {
            "velocity": Codec.encode_vec2(self.velocity),
            "forward_vec": self.forward_vec,
            "x": self.__x,
            "y": self.__y,
            "rotation": self.rotation,
            "tick_exist": self.tick_exist,
            "mass": self.mass,
            "removed": self.removed
        }

    @staticmethod
    @abc.abstractmethod
    def get_codec_name() -> str:
        pass