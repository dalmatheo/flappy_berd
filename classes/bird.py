import pyxel
from classes.object import Object


class Bird(Object):
    def __init__(self, x, y, image, u, v, w, h, col=None) -> None:
        super().__init__(x, y, image, u, v, w, h, col)
        self.vel = [0, 0]
        self.ticks = 0

    def update(self):
        self.falling()
        self.jump()
        self.move()
        self.ticks += 1

    def falling(self):
        if self.ticks % 2 == 0:
            self.vel[1] += 1

    def jump(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.vel[1] = -6

    def move(self):
        self.x += self.vel[0]
        self.y += self.vel[1]
