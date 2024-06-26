import tkinter as tk

from .tile import *

class Map:
    def __init__(self, canvas: tk.Canvas, width, height):
        self.canvas = canvas
        self.void = []
        self.map = []
        self.width = int(width / 32)
        self.height = int(height / 32)
        self.allocate()
    
    def allocate(self):
        for y in range(0, self.height):
            self.void.append([])
            for x in range(0, self.width):
                self.void[y].append(Tile(self.canvas, "void"))
                self.void[y][x].draw(x, y)
        for y in range(0, self.height):
            self.map.append([])
            for x in range(0, self.width):
                self.map[y].append(None)

    def load(self):
        pass

    def save(self):
        pass

    def fill(self, tile: str):
        for y in range(0, self.height):
            for x in range(0, self.width):
                self.void[y][x] = Tile(self.canvas, tile)
                self.void[y][x].draw(x, y)

    def create(self, tile: str, x: int, y: int):
        self.map[y][x] = Tile(self.canvas, tile)
        self.map[y][x].draw(x, y)

    def safe_create(self, tile: str, x: int, y: int):
        if self.map[y][x] == None:
            self.map[y][x] = Tile(self.canvas, tile)
            self.map[y][x].draw(x, y)
            return True
        return False
    
    def delete(self, x: int, y: int):
        self.map[y][x] = None
        self.void[y][x].draw(x, y)
