import pyxel

from classes.game import Game
from classes.instance import Instance
from classes.main_menu import MainMenu


class App:
    def __init__(self):
        pyxel.init(180, 320)
        pyxel.load("assets.pyxres")
        self.instances: list[Instance] = [MainMenu(), Game()]
        self.instance = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        flag = self.instances[self.instance].update()
        if flag and self.instance == 0:
            self.instances[0] = MainMenu()
            self.instance = (self.instance + 1) % 2
        if flag and self.instance == 1:
            self.instances[1] = Game()
            pyxel.text(0, 0, "test", 0)

    def draw(self):
        pyxel.cls(3)
        self.instances[self.instance].draw()


App()
