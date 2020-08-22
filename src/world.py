from collections import deque
from itertools import chain




class SynchronizedDeque:
    def __init__(self, iterable=None, connections=None):
        self.data = deque()

        if iterable:
            for item in iterable:
                self.data.append(item)

        self.connections = connections
        
        if not connections:
            self.connections = []
    
    def __delitem__(self, index):
        del self.data[index]

    def __iter__(self):
        return iter(self.data)
    
    def remove(self, index):
        pass
    
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
        # These entities will be handled
        self.active_entities = deque()

        # These entities won't be handled
        self.inactive_entities = deque()

        self.handlers = None

    def handle_entity(self, entity): 
        
        
        pass

    def update(self):
        for entity in self.active_entities:
            self.handle_entity(entity)


game_world = World(None)

def script_handler_function(entity, world):
    entity.update(world)

script_handler = AttributeHandler("script", script_handler_function)
