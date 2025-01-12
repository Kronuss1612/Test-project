from tkinter import Tk

class Window(Tk): # Window erbt von Tk

    def __init__(self): # __init__ ist ein Konstruktor in Python
        super().__init__() # super ist der Parent

        self.wm_title('Snake') # self ist Window UND Tk

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        window_width = screen_width // 3
        window_height = screen_height // 3

        startx = screen_width // 2 - window_width // 2
        starty = screen_height // 2 - window_height // 2

        self.wm_geometry(f'{window_width}x{window_height}+{startx}+{starty}')
