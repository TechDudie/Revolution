import tkinter as tk

from .window import *
from .tile import *

def draggable(widget):
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)
    widget.bind("<ButtonRelease-1>", on_drag_release)

def draggable_component(widget):
    widget.bind("<Button-1>", on_component_drag_start)
    widget.bind("<B1-Motion>", on_component_drag_motion)
    widget.bind("<ButtonRelease-1>", on_component_drag_release)

def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

def on_drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)

def on_drag_release(event):
    widget = event.widget
    x = round((widget.winfo_x() - widget._drag_start_x + event.x) / 64) * 64
    if x < 0: x = 0
    if x > 512: x = 512
    widget.place(x=x, y=0)

def on_component_drag_start(event):
    widget = event.widget
    container = widget.nametowidget(widget.winfo_parent())
    container._drag_start_x = event.x
    container._drag_start_y = event.y

def on_component_drag_motion(event):
    widget = event.widget
    container = widget.nametowidget(widget.winfo_parent())
    x = container.winfo_x() - container._drag_start_x + event.x
    y = container.winfo_y() - container._drag_start_y + event.y
    container.place(x=x, y=y)

def on_component_drag_release(event):
    widget = event.widget
    container = widget.nametowidget(widget.winfo_parent())
    x = round((container.winfo_x() - container._drag_start_x + event.x) / 64) * 64
    if x < 0: x = 0
    if x > 512: x = 512
    container.place(x=x, y=0)

item_canvases = []

class ItemCanvas():
    def __init__(self, frame: tk.Frame, type: str, x: int, y: int):
        quantity = get_item(type) # type: ignore
        self.canvas = tk.Canvas(frame, width=64, height=32, highlightthickness=0, background="#777777")
        self.canvas.place(x=x, y=y)
        self.type = type
        self.icon = Tile(self.canvas, type)
        self.icon.draw(0, 0)
        self.canvas.create_text(48, 16, text=str(quantity), fill="#ffffff", font=('Arial 16'))
        draggable(self.canvas)
    
    def update(self):
        self.canvas.create_rectangle(28, -1, 64, 33, fill="#777777")
        self.canvas.create_text(48, 16, text=str(get_item(self.type)), fill="#ffffff", font=('Arial 16')) # type: ignore
        print("updated")

class CraftFrame(Window):
    def setup(self):
        self.hotbar = tk.Frame(self.frame, width=576, height=32, highlightbackground="#000000", highlightthickness=2, background="#cccccc")
        self.hotbar.place(x=32, y=256)
        item_canvases.append(ItemCanvas(self.hotbar, "log", 0, 0))

def update():
    for canvas in item_canvases:
        canvas.update()

from .item import *