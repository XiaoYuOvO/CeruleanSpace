import abc
import math
from typing import NoReturn

import pygame.math
from pygame import Rect

from cerulean_space.world.world import World


class Entity(metaclass=abc.ABCMeta):

    def __init__(self, world: World):
        self.bounding_box = self.get_bounding_box()
        self.world = world
        self.velocity = pygame.math.Vector2(0.0, 0.0)
        self.forward_vec = 0
        self.x = 0.0
        self.y = 0.0
        self.rotation = 0.0
        self.rad_rotation = 0.0
        self.tick_exist = 0
        self.removed = False

    @abc.abstractmethod
    def get_bounding_box(self) -> Rect:
        pass

    def on_collided_with(self, other) -> NoReturn:
        pass

    def remove(self) -> NoReturn:
        self.removed = True

    def tick(self):
        self.rad_rotation = math.radians(self.rotation)
        # 游戏绘制系统是以左上角为坐标原点
        self.x -= self.velocity.x + self.forward_vec * math.sin(self.rad_rotation)
        self.y -= self.velocity.y + self.forward_vec * math.cos(self.rad_rotation)
        self.bounding_box.x = self.x
        self.bounding_box.y = self.y
        self.tick_exist += 1
        for collides in self.world.get_collided_entity(self):
            self.on_collided_with(collides)
        pass

    def read_from_json(self, json):
        pass
