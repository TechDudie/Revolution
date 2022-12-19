from ..structure import *
from ..update import *

class Tree(Structure):
    def setup(self):
        self.name = "tree"
        self.height = 5
        self.width = 7
        self.hitbox = (5, 5)
        self.hp = 3
        self.status = 0

    def click(self, event):
        if self.location[0] < event.x / 32 < self.location[0] + self.hitbox[0] and self.location[1] < event.y / 32 < self.location[1] + self.hitbox[1]:
            self.hp -= 1
            if self.hp == 0:
                map = self.map
                for i in range(0, 5):
                    for j in range(0, 5):
                        if map.map[self.location[1] + j][self.location[0] + i] == None:
                            map.void[self.location[1] + j][self.location[0] + i].draw(self.location[0] + i, self.location[1] + j)
                        else:
                            map.map[self.location[1] + j][self.location[0] + i].draw(self.location[0] + i, self.location[1] + j)
                map.create("log", self.location[0] + 2, self.location[1] + 2)
                map.create("log", self.location[0] + 3, self.location[1] + 2)
                map.create("log", self.location[0] + 4, self.location[1] + 2)
                for i in range(0, 5):
                    map.safe_create("leaves", self.location[0] + 5, self.location[1] + i)
                for i in range(0, 5):
                    map.safe_create("leaves", self.location[0] + 6, self.location[1] + i)
                for i in range(1, 4):
                    map.safe_create("leaves", self.location[0] + 7, self.location[1] + i)
                update()