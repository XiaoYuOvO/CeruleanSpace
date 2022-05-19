import os.path
import re
import tkinter
from tkinter.ttk import *
from tkinter import *
from cerulean_space.settings.game_settings import *
from cerulean_space.game import *

settings = GameSettings()
name_of_save = "NewGame"


def scan_save():
    reg = re.compile(".*?\\.json")
    path = "../../"
    files = []
    for _, _, file_names in os.walk(path):
        for each in file_names:
            if reg.match(each) is not None:
                files.append(each)
    return files


def new_dialog():
    global name_of_save, settings
    d = Dialog(0)
    d.draw()
    d.mainloop()

    if not d.is_finished:
        return

    settings.set_save_path(name_of_save)
    CeruleanSpace(settings).start_game_loop()


def show_introduction():
    show_d = Dialog(2)
    show_d.draw()
    show_d.mainloop()


def continue_dialog():
    global name_of_save
    d = Dialog(1, scan_save())
    d.draw()
    d.mainloop()

    if not d.is_finished:
        return

    settings.world_file = "../{}".format(name_of_save)
    CeruleanSpace(settings).start_game_loop()


def setting_dialog():
    s = SettingWindows()
    s.setting()
    s.mainloop()


class Dialog(Tk):
    def __init__(self, code, save_names=None):
        super().__init__()
        self.type = code
        self.title("新游戏" if self.type == 0 else "继续游戏" if self.type == 1 else "游戏介绍")
        self.geometry("300x80" if self.type != 2 else "800x350")
        self.save_names = save_names

        self.save_name = StringVar()
        self.save_name.set(name_of_save)
        self.entry = Entry(self, textvariable=self.save_name)

        self.com = Combobox(self, values=self.save_names)

        self.is_finished = False

    def get_name(self):
        global name_of_save
        print(self.entry.get())
        if self.type == 0:
            name_of_save = self.entry.get()
        else:
            name_of_save = self.com.get()
        self.is_finished = True
        self.destroy()
        self.quit()

    def draw(self):
        if self.type == 0:
            self.entry.pack()
            Button(self, text="新游戏", command=self.get_name, font=("Calibri", 15)).pack()
            print(self.entry.get())
        elif self.type == 1:
            self.com.pack()
            Button(self, text="继续游戏", command=self.get_name, font=("Calibri", 15)).pack()
        else:
            t1 = "本游戏中，你将作为一名航天员，驾驶飞船从地面飞向太空，到太空中执行回收垃圾的任务。"
            t2 = "在飞向太空的途中，你需要用A，D操作飞船的旋转角度，躲避途中的飞机和陨石"
            t3 = "同时，你可以按下W来消耗右侧的推进燃料来提升飞行速度，或者按S来减速。"
            t4 = "你的推进燃料越少，惯性就越小，转向和加速速度就越快。"
            t5 = "你还需要注意风向对飞行的影响。"
            t6 = "当你成功进入太空后，你就需要迅速地将周围的太空垃圾收集到飞船上并送往空间站。"
            t7 = "需要注意的是，你一次收集的垃圾越多，飞得越慢。"
            t8 = "太空中还会散布一些油罐，可以收集他们来补充你的燃料。但这也将使你的飞船重量变大，惯性变大。"
            t9 = "你必须在有限时间内将不低于指定数量的垃圾收集到空间站中，否则任务将会失败。"
            t10 = "那么，你能完成任务吗？"

            Label(self, text=t1, font=("Calibri", 12)).pack()
            Label(self, text=t2, font=("Calibri", 12)).pack()
            Label(self, text=t3, font=("Calibri", 12)).pack()
            Label(self, text=t4, font=("Calibri", 12)).pack()
            Label(self, text=t5, font=("Calibri", 12)).pack()
            Label(self, text=t6, font=("Calibri", 12)).pack()
            Label(self, text=t7, font=("Calibri", 12)).pack()
            Label(self, text=t8, font=("Calibri", 12)).pack()
            Label(self, text=t9, font=("Calibri", 12)).pack()
            Label(self, text=t10, font=("Calibri", 15)).pack()


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title("CeruleanSpace")
        self.geometry("480x300")

        self.save_name = ''
        # todo 窗体的iron

    def draw_mainmenu(self):
        frame_1 = Frame(self)  # 最顶上的窗格
        frame_1.pack(fill=tkinter.X, side=tkinter.TOP)
        Label(frame_1, text="蔚蓝浩空", font=("Calibri", 25)).pack()

        frame_2 = Frame(self)
        frame_2.pack(fill=tkinter.Y, side=tkinter.LEFT)
        Button(frame_2, text="新建存档", font=("Calibri", 15), command=new_dialog).grid(row=0, column=0)
        Button(frame_2, text="继续游戏", font=("Calibri", 15), command=continue_dialog).grid(row=1, column=0)
        Button(frame_2, text="游戏介绍", font=("Calibri", 15), command=show_introduction).grid(row=2, column=0)
        Button(frame_2, text="游戏设置", font=("Calibri", 15), command=setting_dialog).grid(row=3, column=0)


class SettingWindows(Tk):
    def __init__(self):
        super().__init__()
        self.keys_list = {
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
        self.save = None
        self.right = None
        self.left = None
        self.reward = None
        self.weight_value = None
        self.forward = None
        self.title("设置")
        self.geometry("380x250")

    def _get_setting(self):
        global settings
        settings.key_forward = self.keys_list.get(self.forward.get())
        settings.key_reward = self.keys_list.get(self.reward.get())
        settings.key_left = self.keys_list.get(self.left.get())
        settings.key_right = self.keys_list.get(self.right.get())
        settings.key_save_world = self.keys_list.get(self.save.get())

        self.destroy()

    def setting(self):
        global settings

        Label(self, text="前进键").grid(row=0, column=0)
        Label(self, text="后退键").grid(row=1, column=0)
        Label(self, text="向左键").grid(row=2, column=0)
        Label(self, text="向右键").grid(row=3, column=0)
        Label(self, text="存档键").grid(row=4, column=0)

        self.forward = Combobox(self, values=list(self.keys_list.keys()))
        self.forward.current(list(self.keys_list.keys()).index("w"))
        self.forward.grid(row=0, column=1)

        self.reward = Combobox(self, values=list(self.keys_list.keys()))
        self.reward.current(list(self.keys_list.keys()).index("s"))
        self.reward.grid(row=1, column=1)

        self.left = Combobox(self, values=list(self.keys_list.keys()))
        self.left.current(list(self.keys_list.keys()).index("a"))
        self.left.grid(row=2, column=1)

        self.right = Combobox(self, values=list(self.keys_list.keys()))
        self.right.current(list(self.keys_list.keys()).index("d"))
        self.right.grid(row=3, column=1)

        self.save = Combobox(self, values=list(self.keys_list.keys()))
        self.save.current(list(self.keys_list.keys()).index("r"))
        self.save.grid(row=4, column=1)

        Button(self, text="确定",
               command=self._get_setting).grid(row=8, column=0)

        return settings


def run():
    w = Window()

    w.draw_mainmenu()
    w.mainloop()
    w.quit()
