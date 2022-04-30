from typing import Callable, Dict

import pygame.key


class Keyboard:
    def __init__(self):
        self.key_registries: Dict[int, Callable] = dict()
        pygame.key.set_repeat(50, 10)

    def tick(self):
        key_states = pygame.key.get_pressed()
        for item in self.key_registries.items():
            if key_states[item[0]]: item[1]()

    def register_key(self, key: int, callback):
        self.key_registries[key] = callback
