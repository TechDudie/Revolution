from ..structure import *

class Tree(Structure):
    def setup(self):
        self.name = "tree"
        self.height = 5
        self.width = 5

    def click(self, event):
        if self.location[0] < event.x / 32 < self.location[0] + self.width and self.location[1] < event.y / 32 < self.location[1] + self.height:
            pass