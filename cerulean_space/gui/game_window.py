from tkinter import *
from tkinter.ttk import *
import pygame


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title("CeruleanSpace")
        self.geometry("480x300")
        # todo 窗体的iron

    def draw_mainmenu(self, call_backs):
        frame_1 = Frame(self)  # 最顶上的窗格
        frame_1.pack()
        Label(frame_1, text="欢迎来到蔚蓝深空！").grid(row=0, column=0)

        frame_2 = Frame(self)
        frame_2.pack()
        Button(frame_2, text="新建存档", command=call_backs["NewGame"]).grid(row=0, column=0)
        Button(frame_2, text="继续游戏", command=call_backs["Continue"]).grid(row=0, column=1)
        Button(frame_2, text="查看记录", command=call_backs["CheckRecord"]).grid(row=1, column=1)
        Button(frame_2, text="游戏设置", command=call_backs["Setting"]).grid(row=1, column=0)

        frame_3 = Frame(self)
        frame_3.pack()
        value = IntVar()
        value.set(0)
        Radiobutton(frame_3, text="简单", variable=value, value=0).grid(row=0, column=0)
        Radiobutton(frame_3, text="普通", variable=value, value=1).grid(row=0, column=1)
        Radiobutton(frame_3, text="中等", variable=value, value=2).grid(row=1, column=0)
        Radiobutton(frame_3, text="困难", variable=value, value=3).grid(row=1, column=1)
        Radiobutton(frame_3, text="炼狱", variable=value, value=4).grid(row=2, column=0)
        Radiobutton(frame_3, text="疯狂", variable=value, value=5).grid(row=2, column=1)


class SettingWindows(Tk):
    def __init__(self):
        super().__init__()
        self.title("设置")
        self.geometry("380x250")

    def setting(self, call_back):
        keys_list = {
            "K_0": pygame.K_0,
            "K_1": pygame.K_1,
            "K_2": pygame.K_2,
            "K_3": pygame.K_3,
            "K_4": pygame.K_4,
            "K_5": pygame.K_5,
            "K_6": pygame.K_6,
            "K_7": pygame.K_7,
            "K_8": pygame.K_8,
            "K_9": pygame.K_9,
            "K_a": pygame.K_a,
            "K_AC_BACK": pygame.K_AC_BACK,
            "K_AMPERSAND": pygame.K_AMPERSAND,
            "K_ASTERISK": pygame.K_ASTERISK,
            "K_AT": pygame.K_AT,
            "K_b": pygame.K_b,
            "K_BACKQUOTE": pygame.K_BACKQUOTE,
            "K_BACKSLASH": pygame.K_BACKSLASH,
            "K_BACKSPACE": pygame.K_BACKSPACE,
            "K_BREAK": pygame.K_BREAK,
            "K_c": pygame.K_c,
            "K_CAPSLOCK": pygame.K_CAPSLOCK,
            "K_CARET": pygame.K_CARET,
            "K_CLEAR": pygame.K_CLEAR,
            "K_COLON": pygame.K_COLON,
            "K_COMMA": pygame.K_COMMA,
            "K_CURRENCYSUBUNIT": pygame.K_CURRENCYSUBUNIT,
            "K_CURRENCYUNIT": pygame.K_CURRENCYUNIT,
            "K_d": pygame.K_d,
            "K_DELETE": pygame.K_DELETE,
            "K_DOLLAR": pygame.K_DOLLAR,
            "K_DOWN": pygame.K_DOWN,
            "K_e": pygame.K_e,
            "K_END": pygame.K_END,
            "K_EQUALS": pygame.K_EQUALS,
            "K_ESCAPE": pygame.K_ESCAPE,
            "K_EURO": pygame.K_EURO,
            "K_EXCLAIM": pygame.K_EXCLAIM,
            "K_f": pygame.K_f,
            "K_F1": pygame.K_F1,
            "K_F10": pygame.K_F10,
            "K_F11": pygame.K_F11,
            "K_F12": pygame.K_F12,
            "K_F13": pygame.K_F13,
            "K_F14": pygame.K_F14,
            "K_F15": pygame.K_F15,
            "K_F2": pygame.K_F2,
            "K_F3": pygame.K_F3,
            "K_F4": pygame.K_F4,
            "K_F5": pygame.K_F5,
            "K_F6": pygame.K_F6,
            "K_F7": pygame.K_F7,
            "K_F8": pygame.K_F8,
            "K_F9": pygame.K_F9,
            "K_g": pygame.K_g,
            "K_GREATER": pygame.K_GREATER,
            "K_h": pygame.K_h,
            "K_HASH": pygame.K_HASH,
            "K_HELP": pygame.K_HELP,
            "K_HOME": pygame.K_HOME,
            "K_i": pygame.K_i,
            "K_INSERT": pygame.K_INSERT,
            "K_j": pygame.K_j,
            "K_k": pygame.K_k,
            "K_KP0": pygame.K_KP0,
            "K_KP1": pygame.K_KP1,
            "K_KP2": pygame.K_KP2,
            "K_KP3": pygame.K_KP3,
            "K_KP4": pygame.K_KP4,
            "K_KP5": pygame.K_KP5,
            "K_KP6": pygame.K_KP6,
            "K_KP7": pygame.K_KP7,
            "K_KP8": pygame.K_KP8,
            "K_KP9": pygame.K_KP9,
            "K_KP_0": pygame.K_KP_0,
            "K_KP_1": pygame.K_KP_1,
            "K_KP_2": pygame.K_KP_2,
            "K_KP_3": pygame.K_KP_3,
            "K_KP_4": pygame.K_KP_4,
            "K_KP_5": pygame.K_KP_5,
            "K_KP_6": pygame.K_KP_6,
            "K_KP_7": pygame.K_KP_7,
            "K_KP_8": pygame.K_KP_8,
            "K_KP_9": pygame.K_KP_9,
            "K_KP_DIVIDE": pygame.K_KP_DIVIDE,
            "K_KP_ENTER": pygame.K_KP_ENTER,
            "K_KP_EQUALS": pygame.K_KP_EQUALS,
            "K_KP_MINUS": pygame.K_KP_MINUS,
            "K_KP_MULTIPLY": pygame.K_KP_MULTIPLY,
            "K_KP_PERIOD": pygame.K_KP_PERIOD,
            "K_KP_PLUS": pygame.K_KP_PLUS,
            "K_l": pygame.K_l,
            "K_LALT": pygame.K_LALT,
            "K_LCTRL": pygame.K_LCTRL,
            "K_LEFT": pygame.K_LEFT,
            "K_LEFTBRACKET": pygame.K_LEFTBRACKET,
            "K_LEFTPAREN": pygame.K_LEFTPAREN,
            "K_LESS": pygame.K_LESS,
            "K_LGUI": pygame.K_LGUI,
            "K_LMETA": pygame.K_LMETA,
            "K_LSHIFT": pygame.K_LSHIFT,
            "K_LSUPER": pygame.K_LSUPER,
            "K_m": pygame.K_m,
            "K_MENU": pygame.K_MENU,
            "K_MINUS": pygame.K_MINUS,
            "K_MODE": pygame.K_MODE,
            "K_n": pygame.K_n,
            "K_NUMLOCK": pygame.K_NUMLOCK,
            "K_NUMLOCKCLEAR": pygame.K_NUMLOCKCLEAR,
            "K_o": pygame.K_o,
            "K_p": pygame.K_p,
            "K_PAGEDOWN": pygame.K_PAGEDOWN,
            "K_PAGEUP": pygame.K_PAGEUP,
            "K_PAUSE": pygame.K_PAUSE,
            "K_PERCENT": pygame.K_PERCENT,
            "K_PERIOD": pygame.K_PERIOD,
            "K_PLUS": pygame.K_PLUS,
            "K_POWER": pygame.K_POWER,
            "K_PRINT": pygame.K_PRINT,
            "K_PRINTSCREEN": pygame.K_PRINTSCREEN,
            "K_q": pygame.K_q,
            "K_QUESTION": pygame.K_QUESTION,
            "K_QUOTE": pygame.K_QUOTE,
            "K_QUOTEDBL": pygame.K_QUOTEDBL,
            "K_r": pygame.K_r,
            "K_RALT": pygame.K_RALT,
            "K_RCTRL": pygame.K_RCTRL,
            "K_RETURN": pygame.K_RETURN,
            "K_RGUI": pygame.K_RGUI,
            "K_RIGHT": pygame.K_RIGHT,
            "K_RIGHTBRACKET": pygame.K_RIGHTBRACKET,
            "K_RIGHTPAREN": pygame.K_RIGHTPAREN,
            "K_RMETA": pygame.K_RMETA,
            "K_RSHIFT": pygame.K_RSHIFT,
            "K_RSUPER": pygame.K_RSUPER,
            "K_s": pygame.K_s,
            "K_SCROLLLOCK": pygame.K_SCROLLLOCK,
            "K_SCROLLOCK": pygame.K_SCROLLOCK,
            "K_SEMICOLON": pygame.K_SEMICOLON,
            "K_SLASH": pygame.K_SLASH,
            "K_SPACE": pygame.K_SPACE,
            "K_SYSREQ": pygame.K_SYSREQ,
            "K_t": pygame.K_t,
            "K_TAB": pygame.K_TAB,
            "K_u": pygame.K_u,
            "K_UNDERSCORE": pygame.K_UNDERSCORE,
            "K_UNKNOWN": pygame.K_UNKNOWN,
            "K_UP": pygame.K_UP,
            "K_v": pygame.K_v,
            "K_w": pygame.K_w,
            "K_x": pygame.K_x,
            "K_y": pygame.K_y,
            "K_z": pygame.K_z}  # 未来做成一个字典来储存对应的中文名称更好

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
               command=call_back(keys_list.get(forward.get()), keys_list.get(reward.get()), keys_list.get(left.get()),
                                 keys_list.get(right.get()), keys_list.get(save.get()), int(fps.get()),
                                 int(weight.get()), int(height.get())))


if __name__ == '__main__':
    w = SettingWindows()
    w.setting()
    w.mainloop()
