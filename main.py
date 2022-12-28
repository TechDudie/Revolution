import tkinter as tk

from src.tile import *
from src.map import *
from src.item import *
from src.event import *
from src.craft import *

import src.planets.earth as earth

root = tk.Tk()

width = 1280
height = 640
root.geometry(f"{width}x{height}+100+100")
root.title("Revolution")

canvas = tk.Canvas(root, width=width, height=height, highlightthickness=0)
canvas.place(x=0, y=0)
map = Map(canvas, width, height)
earth.generator(map, canvas)
craft = CraftFrame(root, int(width / 4), int(height / 4), int(width / 2), int(height / 2))

setupCanvas(canvas)
setupMap(map)
setupCraft(craft)
setupHUD()

canvas.bind("<Button-1>", lclick)
canvas.bind("<Button-3>", rclick)
root.bind("<KeyPress>", key)

root.mainloop()