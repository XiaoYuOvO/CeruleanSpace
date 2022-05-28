import os.path
import threading
import traceback
from random import Random
from tkinter.messagebox import showerror

import pygame.time

from cerulean_space.constants import GAME_TICK_RATE
from cerulean_space.entity.player_entity import PlayerEntity
from cerulean_space.input.keyboard import Keyboard
from cerulean_space.io.world_storage import WorldStorage
from cerulean_space.render.game_renderer import GameRenderer
from cerulean_space.render.renderer_manager import RendererManager
from cerulean_space.render.ui.hover_text import HoverText
from cerulean_space.settings.game_settings import GameSettings
from cerulean_space.sounds.sound_events import SoundEvents
from cerulean_space.world.generation.world_generator import WorldGenerator

lock = threading.Lock()


class CeruleanSpace:
    def __init__(self, settings: GameSettings):
        if os.path.exists(settings.world_file):
            try:
                self.world = WorldStorage.read_world_from_file(settings.world_file, self)
            except KeyError as err:
                self.world = WorldGenerator.generate_world(Random(), self)
                self.player = PlayerEntity(self.world)
                self.world.add_entity(self.player)
                showerror("世界加载错误", "无法加载世界" + settings.world_file.__str__() + ": " + err.__str__())
                traceback.print_exc()
                raise err
        else:
            self.world = WorldGenerator.generate_world(Random(), self)
            self.player = PlayerEntity(self.world)
            self.world.add_entity(self.player)
        self.running = False
        self.is_game_over = False
        self.settings = settings
        self.game_renderer: GameRenderer = GameRenderer(settings.game_window_width, settings.game_window_height)
        self.keyboard = Keyboard()
        self.renderer_manager = RendererManager(self.game_renderer)
        self.player = self.world.player
        self.renderer_manager.init_all_renders(self.world, self.player)
        self.register_key_callbacks(settings)
        SoundEvents.play_bgm()

    def start_game_loop(self):
        self.running = True
        clock = pygame.time.Clock()
        self.start_world_tick()
        while self.running:
            lock.acquire()
            self.renderer_manager.render()
            self.handle_game_events()
            lock.release()
            clock.tick(self.settings.game_tick_fps)
            pygame.display.set_caption("蔚蓝浩空 " + clock.get_fps().__str__())
        pygame.quit()

    def start_world_tick(self):
        clock = pygame.time.Clock()

        def tick_world_tick():
            while self.running and not self.is_game_over:
                lock.acquire()
                self.keyboard.tick()
                self.world.tick()
                self.renderer_manager.tick()
                lock.release()
                clock.tick(GAME_TICK_RATE)

        threading.Thread(target=tick_world_tick, args=()).start()

    def handle_game_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def register_key_callbacks(self, game_settings: GameSettings):
        def handle_key_forward():
            self.world.game_mode.get_interaction_manager().handle_up(self.player)

        def handle_key_reward():
            self.world.game_mode.get_interaction_manager().handle_down(self.player)

        def handle_key_left():
            self.world.game_mode.get_interaction_manager().handle_left(self.player)

        def handle_key_right():
            self.world.game_mode.get_interaction_manager().handle_right(self.player)

        def handle_save_world():
            WorldStorage.write_world_to_file(self.settings.world_file, self.world)
            self.world.add_hover_text(HoverText("世界已保存",
                                                round(self.game_renderer.get_rendering_width() / 2),
                                                round(self.game_renderer.get_rendering_height() / 3),
                                                60, 50))

        self.keyboard.register_key(game_settings.key_forward, handle_key_forward)
        self.keyboard.register_key(game_settings.key_reward, handle_key_reward)
        self.keyboard.register_key(game_settings.key_left, handle_key_left)
        self.keyboard.register_key(game_settings.key_right, handle_key_right)
        self.keyboard.register_key(game_settings.key_save_world, handle_save_world)

    def game_win(self):
        self.renderer_manager.switch_to_game_win_screen(self.world)
        self.is_game_over = True

    def game_over(self):
        self.renderer_manager.switch_to_game_over_screen(self.world)
        self.is_game_over = True

    def collect_failed(self, garbage_collected: int):
        self.renderer_manager.switch_to_collect_failed_screen(self.world, garbage_collected)
        self.is_game_over = True
