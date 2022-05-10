from cerulean_space.game import CeruleanSpace
from cerulean_space.settings.game_settings import GameSettings

if __name__ == '__main__':
    game = CeruleanSpace(GameSettings())
    game.start_game_loop()
