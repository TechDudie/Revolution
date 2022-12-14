import tkinter as tk

from .tile import *

global items
global excpetions
items = {"log": 0}
EXCEPTIONS = ["leaves"]

global canvas
item_tiles = {}
canvas = None

def setupCanvas(tkCanvas: tk.Canvas):
    global canvas
    canvas = tkCanvas

def add_item(type: str, quantity: int) -> int:
    if type in EXCEPTIONS:
        return
    items[type] += quantity
    updateHUD(type)
    return items[type]

def remove_item(type: str, quantity: int) -> int:
    items[type] -= quantity
    updateHUD(type)
    return items[type]

def set_item(type: str, quantity: int) -> int:
    items[type] = quantity
    updateHUD(type)
    return items[type]

def get_item(type: str) -> int:
    return items[type]

def setupHUD():
    global canvas
    canvas.create_rectangle(0, 576 - len(items) * 32, 128, 608 + len(items) * 32, fill="#000000")
    for i in range(0, len(items)):
        item_tiles[str([items.keys()][i]).split("'")[1:2][0]] = Tile(canvas, str([items.keys()][i]).split("'")[1:2][0]) # used a dirty programming hack here, may lead to unexpected problems later
        item_tiles[str([items.keys()][i]).split("'")[1:2][0]].draw(1, 19 - len(items) + i)

def updateHUD(type):
    global canvas
    canvas.create_rectangle(0, 576 - len(items) * 32, 128, 608 + len(items) * 32, fill="#000000")
    for i in range(0, len(items)):
        item_tiles[str([items.keys()][i]).split("'")[1:2][0]].draw(1, 19 - len(items) + i)
    y = (19 - len(items) + list(items.keys()).index(type)) * 32
    canvas.create_text(80, y + 16, text=str(get_item(type)), fill="#ffffff", font=('Arial 16'))
    update() # type: ignore

from .craft import *