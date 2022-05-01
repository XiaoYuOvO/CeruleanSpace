from tkinter import *


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title("CeruleanSpace")
        self.geometry("480x600")
        # todo 窗体的iron

        self.draw_mainmenu()

    def draw_mainmenu(self):
        frame_1 = Frame(self)  # 最顶上的窗格
        frame_1.pack()
        Label(frame_1, text="欢迎来到蔚蓝深空！").grid(row=0, column=0)

        frame_2 = Frame(self)
        frame_2.pack()
        Button(frame_2, text="开始游戏").grid(row=0, column=0)
        Button(frame_2, text="游戏设置").grid(row=0, column=1)
        Button(frame_2, text="查看记录").grid(row=0, column=2)

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


if __name__ == '__main__':
    w = Window()
    w.mainloop()
