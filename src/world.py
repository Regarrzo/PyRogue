from collections import deque
from itertools import chain


class AttributeHandler:
    def __init__(self, name, function):
        self.name = name
        self.function = function
    
    def __hash__(self):
        return hash(self.name)
    
    def handle(self, entity, world):
        self.function(entity, world)


class World:
    def __init__(self, render_adapter):
        self.active_entities = deque()
        self.frozen_entities = deque()
        self.dormant_entities = deque()

        self.handlers = {}

        self.render_adapter = render_adapter
    
    def render(self):
        self.render_adapter.render(self)
    
    def update(self):
        for entity in self.active_entities:
            for attribute in entity.attributes:
                if attribute in self.handlers:
                    self.handlers[attribute].handle(entity, self)


game_world = World(None)

def script_handler_function(entity, world):
    entity.update(world)

script_handler = AttributeHandler("script", script_handler_function)
