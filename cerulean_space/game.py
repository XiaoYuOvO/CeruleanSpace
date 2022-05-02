import json
import threading

import pygame.time

from cerulean_space.entity.player_entity import PlayerEntity
from cerulean_space.entity.rock_entity import RockEntity
from cerulean_space.input.keyboard import Keyboard
from cerulean_space.io.world_storage import WorldStorage
from cerulean_space.render.background_renderer import BackgroundRenderer
from cerulean_space.render.renderer_manager import RendererManager
from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.settings.game_settings import GameSettings
from cerulean_space.world.world import World


class CeruleanSpace:
    def __init__(self, settings: GameSettings):
        self.running = False
        self.settings = settings
        self.game_renderer = GameRenderer(settings.game_window_width, settings.game_window_height)
        self.keyboard = Keyboard()
        self.renderer_manager = RendererManager(self.game_renderer)
        self.world = WorldStorage.read_world_from_file(settings.world_file)
        # self.player = PlayerEntity(self.world)
        # self.world.add_entity(self.player)
        # testrock = RockEntity(self.world)
        # testrock.set_pos((0, 500))
        # self.world.add_entity(testrock)
        self.player = self.world.player
        self.renderer_manager.init_all_renders(self.world, self.player)
        self.register_key_callbacks(settings)

    def start_game_loop(self):
        self.running = True
        clock = pygame.time.Clock()
        self.start_world_tick()
        while self.running:
            self.renderer_manager.render()
            self.handle_game_events()
            clock.tick(self.settings.game_tick_fps)
        pygame.quit()

    def start_world_tick(self):
        clock = pygame.time.Clock()
        def tick_world_tick(self):
            while self.running:
                self.keyboard.tick()
                self.world.tick()
                self.game_renderer.set_draw_offset(
                    -self.player.get_rendering_x() + (
                            self.game_renderer.screen.get_width() - self.player.get_bounding_box().left) / 2,
                    self.player.get_y() + (
                            self.game_renderer.screen.get_height() - self.player.get_bounding_box().right) / 3 * 2)
                clock.tick(self.settings.game_tick_rate)

        threading.Thread(target=tick_world_tick, args=(self,)).start()

    def handle_game_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # if event.type == pygame.KEYDOWN:
            #     self.keyboard.handle_key_event(event.key)

    def register_key_callbacks(self, game_settings: GameSettings):
        # 由于渲染器的坐标系是以左上角为原点的所以实际是反向的
        def handle_key_forward():
            self.player.push_forward()

        def handle_key_reward():
            self.player.push_reward()

        def handle_key_left():
            self.player.rotate_left()

        def handle_key_right():
            self.player.rotate_right()

        def handle_save_world():
            WorldStorage.write_world_to_file(self.settings.world_file, self.world)

        self.keyboard.register_key(game_settings.key_forward, handle_key_forward)
        self.keyboard.register_key(game_settings.key_reward, handle_key_reward)
        self.keyboard.register_key(game_settings.key_left, handle_key_left)
        self.keyboard.register_key(game_settings.key_right, handle_key_right)
        self.keyboard.register_key(game_settings.key_save_world, handle_save_world)
