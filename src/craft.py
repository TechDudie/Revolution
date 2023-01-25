import tkinter as tk
import math
import os

from .window import *
from .tile import *

item_canvases = []
hotbar_path = os.path.join("assets", "gui") + os.sep

def draggable(widget):
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)
    widget.bind("<ButtonRelease-1>", on_drag_release)

def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x

def on_drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    if x < 0: x = 0
    if x > 512: x = 512
    widget.place(x=x+1, y=1)

def on_drag_release(event):
    widget = event.widget
    x = round((widget.winfo_x() - widget._drag_start_x + event.x) / 64) * 64
    if x < 0: x = 0
    if x > 512: x = 512
    widget.place(x=x+1, y=1)
    swap_item(widget.invslot, math.floor((x - 1) / 64) + 1) # type: ignore
    widget.invslot = math.floor((x - 1) / 64) + 1
    print(x)
    print(widget.invslot)

class ItemCanvas:
    def __init__(self, frame: tk.Frame, type: str):
        quantity = get_item(type) # type: ignore
        self.canvas = tk.Canvas(frame, width=64, height=32, highlightthickness=0, background="#777777")
        self.canvas.place(x=1, y=1)
        self.canvas.invslot = 0
        self.type = type
        self.icon = Tile(self.canvas, type)
        self.icon.draw(0, 0)
        self.canvas.create_text(48, 16, text=str(quantity), fill="#ffffff", font=('Arial 16'))
        draggable(self.canvas)
    
    def update(self):
        self.canvas.create_rectangle(32, 0, 64, 32, outline="", fill="#777777")
        self.canvas.create_text(48, 16, text=str(get_item(self.type)), fill="#ffffff", font=('Arial 16')) # type: ignore

class CraftFrame(Window):
    def setup(self):
        self.hotbar = tk.Frame(self.frame, width=578, height=34, highlightthickness=0, background="#ff0000")
        self.hotbar.place(x=32, y=256)
        self.hotbar_background_image = tk.PhotoImage(file=f"{hotbar_path}hotbar.png")
        self.hotbar_background = tk.Label(self.hotbar, width=578, height=34, image=self.hotbar_background_image)
        self.hotbar_background.place(x=-2, y=-2)
        item_canvases.append(ItemCanvas(self.hotbar, "log"))

def update():
    for canvas in item_canvases:
        canvas.update()

from .item import *