import pyxel
from classes.object import Object


class Button(Object):
    def __init__(self, x, y, image, u, v, w, h, action, col=None) -> None:
        super().__init__(x, y, image, u, v, w, h, col)
        self.action = action

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            x = self.x
            y = self.y
            w = self.w
            h = self.h
            if (
                pyxel.mouse_x >= x
                and pyxel.mouse_x < x + w
                and pyxel.mouse_y >= y
                and pyxel.mouse_y < y + h
            ):
                self.action()
