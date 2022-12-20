import tkinter as tk

from .tile import *

global items
global canvas
items = {"log": 0}
item_tiles = {}
canvas = None

class Item: # I might use this class in the future, but atm, I'm not using it
    def __init__(self):
        pass

def add_item(type: str, quantity: int) -> int:
    items[type] += quantity
    return items[type]

def remove_item(type: str, quantity: int) -> int:
    items[type] -= quantity
    return items[type]

def setupCanvas(tkCanvas: tk.Canvas):
    global canvas
    canvas = tkCanvas

def setupHUD():
    global canvas
    canvas.create_rectangle(0, 576 - len(items) * 32, 128, 608 + len(items) * 32, fill="#000000")
    for i in range(0, len(items)):
        item_tiles[str([items.keys()][i]).split("'")[1:2][0]] = Tile(canvas, str([items.keys()][i]).split("'")[1:2][0]) # used a dirty programming hack here, may lead to unexpected problems later
        item_tiles[str([items.keys()][i]).split("'")[1:2][0]].draw(1, 19 - len(items) + i)