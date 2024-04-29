from random import randint
from time import sleep

import pyxel
from classes.bird import Bird
from classes.instance import Instance
from classes.object import Object


class Game(Instance):
    def __init__(self) -> None:
        pyxel.mouse(False)
        self.ticks = 0
        self.lost = False
        super().__init__()
        self.up_pipes = []
        self.down_pipes = []
        for i in range(3):
            y = randint(-220, -12)
            y2 = y + 240 + randint(60, 122)
            up_pipe = Object(227 + 92 * i, y, 1, 2, 0, 44, 238, 7)
            down_pipe = Object(227 + 92 * i, y2, 1, 50, 0, 44, 238, 7)
            self.up_pipes.append(up_pipe)
            self.down_pipes.append(down_pipe)
        self.objects.append(Bird(16, 148, 1, 127, 8, 32, 24, 14))
        for pipe in self.up_pipes:
            self.objects.append(pipe)
        for pipe in self.down_pipes:
            self.objects.append(pipe)

    def update(self):
        if self.lost:
            return True
        for object in self.objects:
            if type(object) != Bird:
                object.x -= 1
            else:
                object.update()
        if self.up_pipes[0].x == -47:
            up_pipe = self.up_pipes[0]
            down_pipe = self.down_pipes[0]
            self.objects.remove(up_pipe)
            self.objects.remove(down_pipe)
            self.up_pipes.remove(up_pipe)
            self.down_pipes.remove(down_pipe)
            y = randint(-220, -12)
            y2 = y + 240 + randint(60, 122)
            self.up_pipes.append(Object(227, y, 1, 2, 0, 44, 238, 7))
            self.down_pipes.append(Object(227, y2, 1, 50, 0, 44, 238, 7))
            self.objects.append(self.up_pipes[2])
            self.objects.append(self.down_pipes[2])
        self.col()
        self.ticks += 1

    def col(self):
        bird = self.objects[0]
        flag = False
        if bird.y + bird.h > 320:
            flag = True
        if bird.y < 0:
            flag = True
        for object in self.objects:
            if type(object) != Bird:
                if (
                    bird.x + bird.w > object.x
                    and bird.x < object.x + object.w
                    and bird.y + bird.h > object.y
                    and bird.y < object.y + object.h
                ):
                    flag = True
        if flag:
            self.lost = flag
