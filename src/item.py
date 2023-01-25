import tkinter as tk
from collections import OrderedDict

from .tile import *

global inventory
global hotbar
global EXCEPTIONS
global canvas
inventory = [
    ["", 0],
    ["", 0],
    ["", 0],
    ["", 0],
    ["", 0],
    ["", 0],
    ["", 0],
    ["", 0],
    ["", 0]
]
hotbar: Tile = None
EXCEPTIONS = ["leaves"]
canvas: tk.Canvas = None

def setupCanvas(tkCanvas: tk.Canvas):
    global canvas
    canvas = tkCanvas

def index_item(type: str) -> int:
    hotbar_types = []
    x = 0
    for i in range(0, len(inventory)):
        hotbar_types.append(inventory[i][0])
    for i in hotbar_types:
        if i == type:
            return x
        x += 1
    x = 0
    for i in hotbar_types:
        if i == "":
            inventory[x][0] = type
            return x
        x += 1
    print("Wow, your inventory is full!") # To be fixed
    return None

def add_item(type: str, quantity: int) -> int:
    if type in EXCEPTIONS:
        return
    inventory[index_item(type)][1] += quantity
    updateHUD(type)
    return inventory[index_item(type)][1]

def remove_item(type: str, quantity: int) -> int:
    inventory[index_item(type)][1] -= quantity
    updateHUD(type)
    return inventory[index_item(type)][1]

def set_item(type: str, quantity: int) -> int:
    inventory[index_item(type)][1] = quantity
    updateHUD(type)
    return inventory[index_item(type)][1]

def get_item(type: str) -> int:
    return inventory[index_item(type)][1]

def swap_item(index_a: int, index_b: int):
    buffer = inventory[index_a]
    inventory[index_a] = inventory[index_b]
    inventory[index_b] = buffer
    print(inventory)

def setupHUD():
    global canvas
    canvas.create_rectangle(0, 544, 128, 640, fill="#000000")

def updateHUD(type):
    global canvas
    global hotbar
    canvas.create_rectangle(0, 544, 128, 640, outline="", fill="#000000")
    hotbar = Tile(canvas, inventory[0][0])
    hotbar.draw(1, 18)
    canvas.create_text(80, 592, text=str(get_item(type)), fill="#ffffff", font=('Arial 16'))
    update() # type: ignore

from .craft import *