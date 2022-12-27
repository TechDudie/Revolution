import time
import random

from ..map import *

def callback(map: Map):
    while True:
        current_time = time.time()
        for y in range(0, map.height):
            for x in range(0, map.width):
                try:
                    if map.map[y][x].name == "leaves":
                        if current_time - map.map[y][x].metadata["time"] > 10 and random.random() > 0.9:
                            map.delete(x, y)
                except:
                    pass
        time.sleep(1)