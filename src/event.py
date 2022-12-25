import tkinter as tk
import math

from .item import *
from .map import *

global map
global registered_structures
map = None
registered_structures = []

def setupMap(target_map: Map):
    global map
    map = target_map

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
    except:
        pass

def rclick(event: tk.Event):
    pass

def key(event: tk.Event):
    pass