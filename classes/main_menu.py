import pyxel
from classes.button import Button
from classes.instance import Instance
from classes.object import Object


class MainMenu(Instance):
    def __init__(self) -> None:
        super().__init__()
        self.is_starting = False
        pyxel.mouse(True)
        self.objects.append(Button(0, 0, 0, 0, 0, 136, 32, self.start))

    def start(self):
        self.is_starting = True

    def update(self):
        if self.is_starting == True:
            return True
        return super().update()
