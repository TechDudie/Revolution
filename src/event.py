import tkinter as tk

registered_structures = []

def lclick(event: tk.Event):
    for structure in registered_structures:
        structure.click(event)

def rclick(event: tk.Event):
    pass

def key(event: tk.Event):
    pass