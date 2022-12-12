import tkinter as tk
import os

structure_path = os.path.join("assets", "structures") + os.sep

class Structure:
    def __init__(self, canvas: tk.Canvas, name: str):
        self.canvas = canvas
        self.name = name
        self.image = tk.PhotoImage(file=f"{structure_path}{name}.png")
    
    def spawn(self, x: int, y: int):
        self.canvas.create_image(x * 32, y * 32, image=self.image, anchor=tk.NW)

    def click(self):
        pass