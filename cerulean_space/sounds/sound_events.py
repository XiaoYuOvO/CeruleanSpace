import pygame.mixer

pygame.mixer.init()
SOUND_DIR = "./cerulean_space/sounds/"


class SoundEvent:
    def __init__(self, name: str):
        self.sound = pygame.mixer.Sound("./cerulean_space/sounds/" + name)

    def play(self):
        self.sound.play()

class SoundEvents:
    ROCK_CRACK: SoundEvent = SoundEvent("rock_crack.wav")
    METAL_HIT: SoundEvent = SoundEvent("metal_hit.wav")
    DING: SoundEvent = SoundEvent("ding.ogg")

    @staticmethod
    def play_bgm():
        pygame.mixer.music.load("./sounds/bgm_cutted.mp3")
        pygame.mixer.music.play(-1, fade_ms=500)
