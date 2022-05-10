from cerulean_space.constants import BACKGROUND_SCALE
from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.render.world_renderer import WorldRenderer
from cerulean_space.util.identifier import Identifier

from cerulean_space.world.world import World

BACKGROUND_TEXTURE = Identifier("background.png")


class BackgroundRenderer(WorldRenderer):
    def __init__(self, world: World, texture_manager: TextureManager):
        super().__init__(world, texture_manager)
        self.texture = self.texture_manager.load_or_get_texture(BACKGROUND_TEXTURE)
        self.texture_size = self.texture.get_size()

    def render(self, game_renderer: GameRenderer):
        # pygame.transform.
        texture_rect = self.texture.get_rect(top=self.texture_size[1],
                                             y=round(((game_renderer.draw_offset_y * BACKGROUND_SCALE + game_renderer.get_rendering_height()) -
                                                      self.texture_size[1])),
                                             width=1920)
        game_renderer.draw_surface_on_rect(self.texture, texture_rect)
