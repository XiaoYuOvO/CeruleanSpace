from pygame import Surface, Rect

from cerulean_space.render.texture.dynamic_texture import DynamicTexture
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.util.identifier import Identifier


class AnimatedTexture(DynamicTexture):
    def __init__(self, tex_id: Identifier, single_width: int, single_height: int, loop_per_sec: int = 1):
        super().__init__(tex_id)
        self.single_width = single_width
        self.single_height = single_height
        self.animation_total_frame = 0
        self.texture_animation = []
        self.tick = 0
        self.loop_per_sec = loop_per_sec

    def tick_texture(self):
        self.tick += 1

    def load_texture(self, texture_manager: TextureManager):
        super(AnimatedTexture, self).load_texture(texture_manager)
        self.animation_total_frame = round(self.cached_surface.get_height() / self.single_height)
        for i in range(self.animation_total_frame):
            img = self.cached_surface.subsurface(
                Rect((0, i * self.single_height), (self.single_width, self.single_height)))
            self.texture_animation.append(img)

    def preprocess_texture(self, surface: Surface) -> Surface:
        return self.texture_animation[self.tick % self.animation_total_frame // self.loop_per_sec]
