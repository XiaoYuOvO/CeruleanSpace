import abc

import cerulean_space.world.world
from cerulean_space.entity.entity import Entity


class LivingEntity(Entity, metaclass=abc.ABCMeta):
    def __init__(self, world: cerulean_space.world.world.World):
        super().__init__(world)
        self.health = self.get_default_health()

    @abc.abstractmethod
    def get_default_health(self) -> float:
        pass

    def tick(self):
        super().tick()
        if self.health < 0:
            self.remove()
