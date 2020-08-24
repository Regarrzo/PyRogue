from src.utility import Vec2


class Entity:
    def __init__(self, name, pos=None):
        self.name = name
        self.pos = pos

        if not pos:
            self.pos = Vec2()

    def update(self, world):
        pass

    def on_event(self, event):
        pass
