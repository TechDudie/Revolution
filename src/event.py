import tkinter as tk
import math

from .item import *
from .map import *
from .craft import *

global map
global craft_frame
global registered_structures
map = None
craft_frame = None
registered_structures = []

def setupMap(target_map: Map):
    global map
    map = target_map

def setupCraft(target_frame: CraftFrame):
    global craft_frame
    craft_frame = target_frame

def lclick(event: tk.Event):
    global map
    for structure in registered_structures:
        if structure.click(event) == True:
            return
    x = math.floor(event.x / 32)
    y = math.floor(event.y / 32)
    try:
        tile = map.map[y][x].name
        add_item(tile, 1)
        map.delete(x, y)
    except AttributeError:
        pass

def rclick(event: tk.Event):
    global map
    for structure in registered_structures:
        if structure.click(event) == True:
            return
    x = math.floor(event.x / 32)
    y = math.floor(event.y / 32)
    try:
        # if map.safe_create("log", x, y):
        #     remove_item("log", 1)
        if remove_item("log", 1) != -1:
            map.create("log", x, y)
    except AttributeError:
        pass

def key(event: tk.Event):
    if event.char == "c":
        craft_frame.toggle()