import tkinter as tk
import os

structure_path = os.path.join("assets", "structures") + os.sep

class Structure:
    def __init__(self, canvas: tk.Canvas, name="", height=1, width=1):
        self.setup()
        self.canvas = canvas
        self.name = name
        self.image = tk.PhotoImage(file=f"{structure_path}{name}.png")
        self.location = (-1, -1)
    
    def spawn(self, x: int, y: int):
        self.canvas.create_image(x * 32, y * 32, image=self.image, anchor=tk.NW)
        self.location = (x, y)

    def setup(self):
        pass

    def click(self):
        pass