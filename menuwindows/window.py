from tkinter import *

class Window(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.frame = None

    def switch_frame(self, frame):
        if self.frame is not None:
            self.frame.destroy()
        self.frame = frame(self)
        self.frame.pack()
