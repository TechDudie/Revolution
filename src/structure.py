from PIL import ImageTk, Image
import tkinter as tk
import os

from .event import *
from .map import *

structure_path = os.path.join("assets", "structures") + os.sep

class Structure:
    def __init__(self, canvas: tk.Canvas, map: Map):
        self.canvas = canvas
        self.map = map
        self.name = ""
        self.height = 0
        self.width = 0
        self.hp = 1
        self.setup()
        self.image = ImageTk.PhotoImage(Image.open(f"{structure_path}{self.name}.png"))
        self.location = (-1, -1)
        self.click_register()
    
    def spawn(self, x: int, y: int):
        if self.hp > 0:
            self.canvas.create_image(x * 32, y * 32, image=self.image, anchor=tk.NW)
            self.location = (x, y)

    def setup(self):
        pass

    def click(self, event):
        pass

    def click_register(self):
        registered_structures.append(self)