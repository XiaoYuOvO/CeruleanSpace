from pygame import Color, Surface


class HoverText:
    def __init__(self, content: str, x: int, y: int, display_time: int, size: int = 10,no_fade: bool = False,
                 color: Color = Color(255, 255, 255)):
        self.content = content
        self.x = x
        self.y = y
        self.max_display_time = display_time
        self.display_time = display_time
        self.size = size
        self.no_fade = no_fade
        self.color = color
        self.cached_img: Surface = None
