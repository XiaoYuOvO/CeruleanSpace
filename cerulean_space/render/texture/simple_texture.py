from typing import Tuple

from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.texture.texture import Texture
from cerulean_space.render.texture_manager import TextureManager


class SimpleTexture(Texture):
    def load_texture(self, texture_manager: TextureManager):
        self.cached_surface = texture_manager.load_or_get_texture(self.tex_id)

    def render_texture(self, game_renderer: GameRenderer, pos: Tuple[int, int], rotation=0):
        if rotation is not 0:
            game_renderer.draw_surface_with_angle(self.cached_surface, pos[0],
                                                  pos[1],
                                                  -rotation)
        else:
            game_renderer.draw_surface_at(self.cached_surface, pos[0],
                                          pos[1])
