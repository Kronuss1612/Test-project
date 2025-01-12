from tkinter import Tk

class Map:
    size: int # attribute / Eigenschaft

    def __init__(self, size, window: Tk): # __init__ ist ein Konstruktor in Python
        self.size = size # wir geben der Eigenschaft den Wert des Parameters

    def draw(self):
        pass
    #open a window and show the map
