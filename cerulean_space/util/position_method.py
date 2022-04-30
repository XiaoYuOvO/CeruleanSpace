from enum import Enum
from typing import Callable, Tuple


class PositionMethod:
    def __init__(self, calc: Callable[[int, int, int, int], Tuple[int, int]]):
        self.method = calc
        pass

    def calc_draw_pos(self, x: int, y: int, x_off: int, y_off: int) -> Tuple[int, int]:
        return self.method(x, y, x_off, y_off)


ABSOLUTE = PositionMethod(lambda x, y, x_off, y_off: (x, y))
RELATIVE = PositionMethod(lambda x, y, x_off, y_off: (x + x_off, y + y_off))
