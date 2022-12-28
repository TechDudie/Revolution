from .event import *

def update():
    for structure in registered_structures:
        if structure.location != (-1, -1):
            structure.spawn(structure.location[0], structure.location[1])