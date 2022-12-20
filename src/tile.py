import tkinter as tk
import os

tile_path = os.path.join("assets", "tiles") + os.sep

class Tile:
    def __init__(self, canvas: tk.Canvas, name: str):
        self.canvas = canvas
        self.name = name
        self.image = tk.PhotoImage(file=f"{tile_path}{name}.png")
    
    def draw(self, x: int, y: int):
        self.canvas.create_image(x * 32, y * 32, image=self.image, anchor=tk.NW)