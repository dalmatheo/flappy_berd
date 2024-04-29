from classes.object import Object


class Instance:
    def __init__(self) -> None:
        self.objects: list[Object] = []

    def update(self):
        for object in self.objects:
            object.update()
        return False

    def draw(self):
        for object in self.objects:
            object.draw()
