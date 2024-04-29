import pyxel

from classes.game import Game
from classes.instance import Instance
from classes.main_menu import MainMenu


class App:
    def __init__(self):
        pyxel.init(180, 320)
        pyxel.load("assets.pyxres")
        self.instance = MainMenu()
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.instance.update():
            self.instance = Game()

    def draw(self):
        pyxel.cls(3)
        self.instance.draw()


App()
