import tkinter as tk

class Window:
    def __init__(self, root, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.metadata = {}
        self.visible = False
        self.root = root
        self.frame = tk.Frame(root, width=width, height=height, highlightthickness=0)
        self.setup()

    def setup(self):
        pass

    def show(self) -> bool:
        if not self.visible:
            self.frame.place(x=self.x, y=self.y)
            self.visble = True
            return True
        return False

    def hide(self) -> bool:
        if self.visible:
            self.frame.place_forget()
            self.visble = False
            return True
        return False
    
    def toggle(self):
        if self.visible:
            self.frame.place_forget()
            self.visible = False
        else:
            self.frame.place(x=self.x, y=self.y)
            self.visible = True