from util import Vec2


class Entity:
    def __init__(self, name, pos=Vec2()):
        self.name = name
        self.pos = pos

    def update(self, world):
        pass

    def on_event(self, event):
        pass
