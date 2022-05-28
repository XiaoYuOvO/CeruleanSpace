from typing import Callable, Tuple


class PositionMethod:
    def __init__(self, calc: Callable[[float, float, float, float], Tuple[float, float]]):
        self.method = calc

    def calc_draw_pos(self, x: float, y: float, x_off: float, y_off: float) -> Tuple[float, float]:
        return self.method(x, y, x_off, y_off)


ABSOLUTE = PositionMethod(lambda x, y, x_off, y_off: (x, y))
RELATIVE = PositionMethod(lambda x, y, x_off, y_off: (x + x_off, y + y_off))
Y_RELATIVE = PositionMethod(lambda x, y, x_off, y_off: (x, y + y_off))
