from enum import Enum


class GameMode:
    def __init__(self, mode_name: str):
        self.mode_name = mode_name


class GameModes(Enum):
    FLY = GameMode("fly")
    COLLECT = GameMode("collect")
