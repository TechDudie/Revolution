import tkinter as tk
import random
import threading

from ..map import *
from ..structure import *

from ..structures.tree import *

from ..threads.leaves import callback as leaves

PROBABILITY_TREE = 0.05

active_threads = {}

def generator(map: Map, canvas: tk.Canvas):
    map.fill("grass")
    place_structure(canvas, map, Tree, PROBABILITY_TREE)
    active_threads["leaf"] = threading.Thread(target=leaves, args=[map])
    active_threads["leaf"].start()
    
def place_structure(canvas: tk.Canvas, map: Map, structure: Structure, probability: float):
    struct = structure(canvas, map)
    width = map.width - struct.width
    height = map.height - struct.height
    for x in range(0, width):
        for y in range(0, height):
            if (random.random() < probability):
                struct.spawn(x, y)
                struct = structure(canvas, map)
                random.seed(random.random() + probability)