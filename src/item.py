import tkinter as tk

from .tile import *

global canvas
canvas = None

def setupCanvas(tkCanvas: tk.Canvas):
    global canvas
    canvas = tkCanvas

def setupHUD():
    pass