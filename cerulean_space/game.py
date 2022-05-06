import threading
from random import Random

import pygame.time

from cerulean_space.constants import PLAYER_MAX_X
from cerulean_space.entity.player_entity import PlayerEntity
from cerulean_space.input.keyboard import Keyboard
from cerulean_space.io.world_storage import WorldStorage
from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.renderer_manager import RendererManager
from cerulean_space.settings.game_settings import GameSettings
from cerulean_space.world.generation.world_generator import WorldGenerator
lock = threading.Lock()


class CeruleanSpace:
    def __init__(self, settings: GameSettings):
        self.running = False
        self.settings = settings
        self.game_renderer: GameRenderer = GameRenderer(settings.game_window_width, settings.game_window_height)
        self.keyboard = Keyboard()
        self.renderer_manager = RendererManager(self.game_renderer)
        self.world = WorldGenerator.generate_world(Random(), self)
        self.player = PlayerEntity(self.world)
        self.world.add_entity(self.player)
        # self.world.add_entity(self.player)
        # testrock = RockEntity(self.world)
        # testrock2 = RockEntity(self.world)
        # testrock.set_pos((0, 500))
        # testrock2.set_pos((0, 1000))
        # self.world.add_entity(testrock2)
        # self.world.add_entity(testrock)
        self.player = self.world.player
        self.renderer_manager.init_all_renders(self.world, self.player)
        self.register_key_callbacks(settings)

    def start_game_loop(self):
        self.running = True
        clock = pygame.time.Clock()
        self.start_world_tick()
        while self.running:
            lock.acquire()
            self.renderer_manager.render()
            self.handle_game_events()
            lock.release()
            clock.tick(self.settings.game_tick_rate)
        pygame.quit()

    def start_world_tick(self):
        clock = pygame.time.Clock()

        def tick_world_tick():
            while self.running:
                lock.acquire()
                self.keyboard.tick()
                self.world.tick()
                self.game_renderer.set_draw_offset(
                    PLAYER_MAX_X,
                    self.player.get_y() + (
                            self.game_renderer.get_rendering_height()) / 4 * 3)
                lock.release()
                clock.tick(self.settings.game_tick_rate)

        threading.Thread(target=tick_world_tick, args=()).start()

    def handle_game_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # if event.type == pygame.WINDOWRESIZED:
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

    def game_win(self):
        self.renderer_manager.switch_to_game_win_screen(self.world)

    def game_over(self):
        self.renderer_manager.switch_to_game_over_screen(self.world)
