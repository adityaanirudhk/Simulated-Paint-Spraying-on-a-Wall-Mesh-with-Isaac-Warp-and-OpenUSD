
import numpy as np

class PaintSurface:

    def __init__(self, width=256, height=256): #defining the painting surface parameters

        self.width = width
        self.height = height
        self.paint = np.zeros((height,width))

    def add_paint(self, x, y, amount=0.05): #parameters for adding paint to the surface

        if 0 <= x < self.width and 0 <= y < self.height:

            current = self.paint[y,x]
            self.paint[y,x] = current + amount * (1-current)
