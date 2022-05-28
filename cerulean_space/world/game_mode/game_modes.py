from typing import Dict, List

import cerulean_space.world.game_mode.collect_game_mode as collect_game_mode_file
import cerulean_space.world.game_mode.cutscene_game_mode as cutscene_game_mode_file
import cerulean_space.world.game_mode.fly_game_mode as fly_game_mode_file
from cerulean_space.world.game_mode.game_mode import GameMode

GAME_MODE_MAP: Dict[str, GameMode] = dict()


def register_game_mode(gamemode: GameMode) -> GameMode:
    GAME_MODE_MAP[gamemode.get_name()] = gamemode
    return gamemode


class GameModes:
    FLY: GameMode = register_game_mode(fly_game_mode_file.FlyGameMode())
    COLLECT: GameMode = register_game_mode(collect_game_mode_file.CollectGameMode())
    CUTSCENE: GameMode = register_game_mode(cutscene_game_mode_file.CutsceneGameMode())

    @staticmethod
    def get_from_name(name: str) -> GameMode:
        return GAME_MODE_MAP[name]

    @staticmethod
    def get_all_modes() -> List[GameMode]:
        return list(GAME_MODE_MAP.values())
