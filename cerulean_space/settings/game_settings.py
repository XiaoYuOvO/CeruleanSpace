import pygame


class GameSettings:
    def __init__(self):
        self.key_forward = pygame.K_w
        self.key_reward = pygame.K_s
        self.key_left = pygame.K_a
        self.key_right = pygame.K_d
        self.key_save_world = pygame.K_r
        self.game_tick_rate = 60
        self.game_tick_fps = 120
        self.game_window_width = 1600
        self.game_window_height = 900
        self.world_file = "../world.json"
