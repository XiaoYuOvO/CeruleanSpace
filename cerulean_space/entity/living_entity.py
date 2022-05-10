import abc

from cerulean_space.entity.entity import Entity


class LivingEntity(Entity, metaclass=abc.ABCMeta):
    def __init__(self, world):
        super().__init__(world)
        self.health = self.get_default_health()

    @abc.abstractmethod
    def get_default_health(self) -> float:
        pass

    @abc.abstractmethod
    def get_max_health(self) -> float:
        pass

    def damage(self, damage: float):
        self.health -= damage

    def living_tick(self):
        super().living_tick()
        if self.health <= 0:
            self.on_death()
            self.remove()

    def write_to_json(self) -> dict:
        data = super(LivingEntity, self).write_to_json()
        data["health"] = self.health
        return data

    def read_from_json(self, data: dict):
        super().read_from_json(data)
        self.health = data["health"]

    def on_death(self):
        pass

