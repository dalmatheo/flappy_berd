import pyxel


class Object:
    def __init__(self, x, y, image, u, v, w, h, col=None) -> None:
        self.x = x
        self.y = y
        self.image = image
        self.u = u
        self.v = v
        self.w = w
        self.h = h
        self.col = col

    def update(self):
        pass

    def draw(self):
        if self.col == None:
            pyxel.blt(self.x, self.y, self.image, self.u, self.v, self.w, self.h)
        else:
            pyxel.blt(
                self.x, self.y, self.image, self.u, self.v, self.w, self.h, self.col
            )
