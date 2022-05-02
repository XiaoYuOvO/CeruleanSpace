from cerulean_space.entity.player_entity import PlayerEntity
from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.texture_manager import TextureManager
from cerulean_space.render.world_renderer import WorldRenderer
from cerulean_space.world.world import World


# 用于移动绘制偏移以达到镜头移动的效果
class CameraRenderer(WorldRenderer):
    def __init__(self, world: World, texture_manager: TextureManager, player: PlayerEntity):
        super().__init__(world, texture_manager)
        self.player = player

    def render(self, game_renderer: GameRenderer):
        pass
