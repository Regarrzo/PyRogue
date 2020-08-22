import abc

from itertools import chain


class RenderAdapter(abc.ABC):
    
    @abc.abstractmethod
    def render(self, world):
        pass


class ConsoleRenderAdapter(RenderAdapter):
    def __init__(self):
        pass

    def render(self, world):
        for entity in chain(world.active_entities, world.frozen_entities):
            if "consolerender" in entity.attributes:
