

class World:
    def __init__(self):
        self.active_entities = []
        self.frozen_entities = []
    
    def update(self):
        for entity in self.active_entities:
            entity.update()
