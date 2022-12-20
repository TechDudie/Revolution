import tkinter as tk

from src.tile import *
from src.map import *
from src.item import *
from src.event import *

import src.planets.earth as earth

import src.structures.tree as tree

root = tk.Tk()

root.geometry("1280x640+100+100")
root.title("Revolution")

canvas = tk.Canvas(root, width=1280, height=640)
canvas.pack()

canvas.bind("<Button-1>", lclick)
canvas.bind("<Button-3>", rclick)
canvas.bind("<Key>", key)

map = Map(canvas)
earth.generator(map, canvas)

setupCanvas(canvas)
setupHUD()

root.mainloop()
