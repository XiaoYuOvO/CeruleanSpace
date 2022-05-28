import cerulean_space.world.game_mode.game_modes as gamemodes
from cerulean_space.constants import PLAYER_MAX_HEIGHT
from cerulean_space.input.fly_interaction_manager import FlyInteractionManager
from cerulean_space.input.player_interaction_manager import PlayerInteractionManager
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.render.ui.game_mode.fly_game_mode_renderer import FlyGameModeUIRenderer
from cerulean_space.util.math.math_helper import MathHelper
from cerulean_space.world.game_mode.game_mode import GameMode


class FlyGameMode(GameMode):
    def __init__(self):
        self.wind_force = 0.0
        self.time_to_next_wind_force = 0
        self.interaction_manager = FlyInteractionManager(self)

    def construct_renderer(self, world, texture_manager: TextureManager):
        return FlyGameModeUIRenderer(world, texture_manager)

    def tick_game_mode(self, world):
        for e in world.entities:
            if e.tick_exist % 5 == 0:
                e.set_pos((e.get_x() + self.wind_force, e.get_y()))
        if self.time_to_next_wind_force <= 0:
            self.wind_force = world.rand.randrange(-5, 5)
            self.time_to_next_wind_force = world.rand.randrange(300, 1800)
        else:
            self.time_to_next_wind_force -= 1
        if world.player.get_y() >= PLAYER_MAX_HEIGHT:
            world.switch_to_mode(gamemodes.GameModes.CUTSCENE)
            world.player.world.player.switch_to_collect_mode()
        if world.player.tick_exist % 30 == 0:
            world.player.forward_vec = world.player.attribute.min_speed + MathHelper.cutoff(
                world.player.forward_vec * 0.7, world.player.attribute.min_speed,
                world.player.attribute.min_speed)

    def get_interaction_manager(self) -> PlayerInteractionManager:
        return self.interaction_manager

    def read_from_json(self, data: dict):
        super(FlyGameMode, self).read_from_json(data)
        self.wind_force = data.get("wind_force")
        self.time_to_next_wind_force = data.get("time_to_next_wind_force")

    def write_to_json(self) -> dict:
        data = super(FlyGameMode, self).write_to_json()
        data["wind_force"] = self.wind_force
        data['time_to_next_wind_force'] = self.time_to_next_wind_force
        return data

    @staticmethod
    def get_name() -> str:
        return "fly"
