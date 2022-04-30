import pygame


class GameSettings:
    def __init__(self):
        self.key_forward = pygame.K_w
        self.key_reward = pygame.K_s
        self.key_left = pygame.K_a
        self.key_right = pygame.K_d
        self.game_tick_rate = 60
        self.game_window_width = 1920
        self.game_window_height = 1080
