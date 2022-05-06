import os.path
import re
import tkinter
from tkinter.ttk import *
from tkinter import *
import pygame
# from ..world.generation.world_generator import *
from cerulean_space.settings.game_settings import *

settings = GameSettings()


def new_game():
    if os.path.exists(settings.world_file):
        pass


def scan_save():
    reg = re.compile(".*?\\.json")
    path = "../../"
    files = []
    for _, _, file_names in os.walk(path):
        for each in file_names:
            if reg.match(each) is not None:
                files.append(each)

    return files


class Dialog(Tk):
    new_code = 0
    continue_code = 1
    save_name = "NewGame"

    def __init__(self, code, save_names=None):
        super().__init__()
        self.type = code
        self.title("新游戏" if self.type == 0 else "选择存档")
        self.geometry("300x80")
        self.save_names = save_names

    def get_name(self, name):
        self.save_name = name
        print(name)
        return ""

    def draw(self):
        if self.type == 0:
            save_name = StringVar()
            save_name.set(self.save_name)
            entry = Entry(self, textvariable=save_name)
            entry.pack()

            Button(self, text="新游戏", command=self.get_name(save_name.get()), font=("Calibri", 15)).pack()
        else:
            com = Combobox(self, textvariable=self.save_names)
            com.pack()

            Button(self, text="继续游戏", command=self.get_name(com.get()), font=("Calibri", 15)).pack()


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title("CeruleanSpace")
        self.geometry("480x300")
        # todo 窗体的iron

    def draw_mainmenu(self, call_backs):
        saves = scan_save()
        frame_1 = Frame(self)  # 最顶上的窗格
        frame_1.pack(fill=tkinter.X, side=tkinter.TOP)
        Label(frame_1, text="蔚蓝浩空", font=("Calibri", 25)).pack()

        frame_2 = Frame(self)
        frame_2.pack(fill=tkinter.Y, side=tkinter.LEFT)
        Button(frame_2, text="新建存档", font=("Calibri", 15), command=call_backs["NewGame"]).grid(row=0, column=0)
        Button(frame_2, text="继续游戏", font=("Calibri", 15), command=call_backs["Continue"]).grid(row=1, column=0)
        Button(frame_2, text="查看记录", font=("Calibri", 15), command=call_backs["CheckRecord"]).grid(row=2, column=0)
        Button(frame_2, text="游戏设置", font=("Calibri", 15), command=call_backs["Setting"]).grid(row=3, column=0)

        # frame_3 = Frame(self)
        # frame_3.pack()
        # value = IntVar()
        # value.set(0)
        # Radiobutton(frame_3, text="简单", variable=value, value=0).grid(row=0, column=0)
        # Radiobutton(frame_3, text="普通", variable=value, value=1).grid(row=0, column=1)
        # Radiobutton(frame_3, text="中等", variable=value, value=2).grid(row=1, column=0)
        # Radiobutton(frame_3, text="困难", variable=value, value=3).grid(row=1, column=1)
        # Radiobutton(frame_3, text="炼狱", variable=value, value=4).grid(row=2, column=0)
        # Radiobutton(frame_3, text="疯狂", variable=value, value=5).grid(row=2, column=1)


class SettingWindows(Tk):
    def __init__(self):
        super().__init__()
        self.title("设置")
        self.geometry("380x250")

    def setting(self):
        global settings

        def _get_setting(forward_key, reward_key, left_key, right_key, save_key, fps_max, weight_max, height_max):
            global settings
            settings.key_forward = forward_key
            settings.key_reward = reward_key
            settings.key_left = left_key
            settings.key_right = right_key
            settings.key_save_world = save_key
            settings.game_tick_fps = fps_max
            settings.game_window_width = weight_max
            settings.game_window_height = height_max

        keys_list = {
            "0": pygame.K_0,
            "1": pygame.K_1,
            "2": pygame.K_2,
            "3": pygame.K_3,
            "4": pygame.K_4,
            "5": pygame.K_5,
            "6": pygame.K_6,
            "7": pygame.K_7,
            "8": pygame.K_8,
            "9": pygame.K_9,
            "a": pygame.K_a,
            "b": pygame.K_b,
            "c": pygame.K_c,
            "d": pygame.K_d,
            "e": pygame.K_e,
            "g": pygame.K_g,
            "h": pygame.K_h,
            "i": pygame.K_i,
            "j": pygame.K_j,
            "k": pygame.K_k,
            "l": pygame.K_l,
            "m": pygame.K_m,
            "n": pygame.K_n,
            "o": pygame.K_o,
            "p": pygame.K_p,
            "q": pygame.K_q,
            "r": pygame.K_r,
            "s": pygame.K_s,
            "t": pygame.K_t,
            "u": pygame.K_u,
            "z": pygame.K_z,
            "v": pygame.K_v,
            "w": pygame.K_w,
            "x": pygame.K_x,
            "y": pygame.K_y,
            "AC_BACK": pygame.K_AC_BACK,
            "AMPERSAND": pygame.K_AMPERSAND,
            "ASTERISK": pygame.K_ASTERISK,
            "AT": pygame.K_AT,
            "BACKQUOTE": pygame.K_BACKQUOTE,
            "BACKSLASH": pygame.K_BACKSLASH,
            "BACKSPACE": pygame.K_BACKSPACE,
            "BREAK": pygame.K_BREAK,
            "CAPSLOCK": pygame.K_CAPSLOCK,
            "CARET": pygame.K_CARET,
            "CLEAR": pygame.K_CLEAR,
            "COLON": pygame.K_COLON,
            "COMMA": pygame.K_COMMA,
            "CURRENCYSUBUNIT": pygame.K_CURRENCYSUBUNIT,
            "CURRENCYUNIT": pygame.K_CURRENCYUNIT,
            "DELETE": pygame.K_DELETE,
            "DOLLAR": pygame.K_DOLLAR,
            "DOWN": pygame.K_DOWN,
            "END": pygame.K_END,
            "EQUALS": pygame.K_EQUALS,
            "ESCAPE": pygame.K_ESCAPE,
            "EURO": pygame.K_EURO,
            "EXCLAIM": pygame.K_EXCLAIM,
            "f": pygame.K_f,
            "F1": pygame.K_F1,
            "F10": pygame.K_F10,
            "F11": pygame.K_F11,
            "F12": pygame.K_F12,
            "F13": pygame.K_F13,
            "F14": pygame.K_F14,
            "F15": pygame.K_F15,
            "F2": pygame.K_F2,
            "F3": pygame.K_F3,
            "F4": pygame.K_F4,
            "F5": pygame.K_F5,
            "F6": pygame.K_F6,
            "F7": pygame.K_F7,
            "F8": pygame.K_F8,
            "F9": pygame.K_F9,
            "GREATER": pygame.K_GREATER,
            "HASH": pygame.K_HASH,
            "HELP": pygame.K_HELP,
            "HOME": pygame.K_HOME,
            "INSERT": pygame.K_INSERT,
            "KP0": pygame.K_KP0,
            "KP1": pygame.K_KP1,
            "KP2": pygame.K_KP2,
            "KP3": pygame.K_KP3,
            "KP4": pygame.K_KP4,
            "KP5": pygame.K_KP5,
            "KP6": pygame.K_KP6,
            "KP7": pygame.K_KP7,
            "KP8": pygame.K_KP8,
            "KP9": pygame.K_KP9,
            "KP_0": pygame.K_KP_0,
            "KP_1": pygame.K_KP_1,
            "KP_2": pygame.K_KP_2,
            "KP_3": pygame.K_KP_3,
            "KP_4": pygame.K_KP_4,
            "KP_5": pygame.K_KP_5,
            "KP_6": pygame.K_KP_6,
            "KP_7": pygame.K_KP_7,
            "KP_8": pygame.K_KP_8,
            "KP_9": pygame.K_KP_9,
            "KP_DIVIDE": pygame.K_KP_DIVIDE,
            "KP_ENTER": pygame.K_KP_ENTER,
            "KP_EQUALS": pygame.K_KP_EQUALS,
            "KP_MINUS": pygame.K_KP_MINUS,
            "KP_MULTIPLY": pygame.K_KP_MULTIPLY,
            "KP_PERIOD": pygame.K_KP_PERIOD,
            "KP_PLUS": pygame.K_KP_PLUS,
            "LALT": pygame.K_LALT,
            "LCTRL": pygame.K_LCTRL,
            "LEFT": pygame.K_LEFT,
            "LEFTBRACKET": pygame.K_LEFTBRACKET,
            "LEFTPAREN": pygame.K_LEFTPAREN,
            "LESS": pygame.K_LESS,
            "LGUI": pygame.K_LGUI,
            "LMETA": pygame.K_LMETA,
            "LSHIFT": pygame.K_LSHIFT,
            "LSUPER": pygame.K_LSUPER,
            "MENU": pygame.K_MENU,
            "MINUS": pygame.K_MINUS,
            "MODE": pygame.K_MODE,
            "NUMLOCK": pygame.K_NUMLOCK,
            "NUMLOCKCLEAR": pygame.K_NUMLOCKCLEAR,
            "PAGEDOWN": pygame.K_PAGEDOWN,
            "PAGEUP": pygame.K_PAGEUP,
            "PAUSE": pygame.K_PAUSE,
            "PERCENT": pygame.K_PERCENT,
            "PERIOD": pygame.K_PERIOD,
            "PLUS": pygame.K_PLUS,
            "POWER": pygame.K_POWER,
            "PRINT": pygame.K_PRINT,
            "PRINTSCREEN": pygame.K_PRINTSCREEN,
            "QUESTION": pygame.K_QUESTION,
            "QUOTE": pygame.K_QUOTE,
            "QUOTEDBL": pygame.K_QUOTEDBL,
            "RALT": pygame.K_RALT,
            "RCTRL": pygame.K_RCTRL,
            "RETURN": pygame.K_RETURN,
            "RGUI": pygame.K_RGUI,
            "RIGHT": pygame.K_RIGHT,
            "RIGHTBRACKET": pygame.K_RIGHTBRACKET,
            "RIGHTPAREN": pygame.K_RIGHTPAREN,
            "RMETA": pygame.K_RMETA,
            "RSHIFT": pygame.K_RSHIFT,
            "RSUPER": pygame.K_RSUPER,
            "SCROLLLOCK": pygame.K_SCROLLLOCK,
            "SCROLLOCK": pygame.K_SCROLLOCK,
            "SEMICOLON": pygame.K_SEMICOLON,
            "SLASH": pygame.K_SLASH,
            "SPACE": pygame.K_SPACE,
            "SYSREQ": pygame.K_SYSREQ,
            "TAB": pygame.K_TAB,
            "UNDERSCORE": pygame.K_UNDERSCORE,
            "UNKNOWN": pygame.K_UNKNOWN,
            "UP": pygame.K_UP
        }  # 未来做成一个字典来储存对应的中文名称更好

        Label(self, text="前进键").grid(row=0, column=0)
        Label(self, text="后退键").grid(row=1, column=0)
        Label(self, text="向左键").grid(row=2, column=0)
        Label(self, text="向右键").grid(row=3, column=0)
        Label(self, text="存档键").grid(row=4, column=0)
        Label(self, text="最高帧数").grid(row=5, column=0)
        Label(self, text="窗口宽度").grid(row=6, column=0)
        Label(self, text="窗口长度").grid(row=7, column=0)

        forward = Combobox(self, values=list(keys_list.keys()))
        forward.current(list(keys_list.keys()).index("K_w"))
        forward.grid(row=0, column=1)

        reward = Combobox(self, values=list(keys_list.keys()))
        reward.current(list(keys_list.keys()).index("K_s"))
        reward.grid(row=1, column=1)

        left = Combobox(self, values=list(keys_list.keys()))
        left.current(list(keys_list.keys()).index("K_a"))
        left.grid(row=2, column=1)

        right = Combobox(self, values=list(keys_list.keys()))
        right.current(list(keys_list.keys()).index("K_d"))
        right.grid(row=3, column=1)

        save = Combobox(self, values=list(keys_list.keys()))
        save.current(list(keys_list.keys()).index("K_r"))
        save.grid(row=4, column=1)

        fps_value = StringVar()
        fps_value.set("120")
        fps = Entry(self, textvariable=fps_value)
        fps.grid(row=5, column=1)

        weight_value = StringVar()
        weight_value.set("1920")
        weight = Entry(self, textvariable=fps_value)
        weight.grid(row=6, column=1)

        height_value = StringVar()
        height_value.set("1080")
        height = Entry(self, textvariable=fps_value)
        height.grid(row=7, column=1)

        Button(self, text="确定",
               command=_get_setting(keys_list.get(forward.get()), keys_list.get(reward.get()),
                                    keys_list.get(left.get()),
                                    keys_list.get(right.get()), keys_list.get(save.get()), int(fps.get()),
                                    int(weight.get()), int(height.get()))).grid(row=8, column=0)

        return settings


if __name__ == '__main__':
    w = Dialog(0)

    def none():
        pass
    dic = dict()
    dic["NewGame"] = none
    dic["Continue"] = none
    dic["CheckRecord"] = none
    dic["Setting"] = none

    w.draw()
    w.mainloop()
