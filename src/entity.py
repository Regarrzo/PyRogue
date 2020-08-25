"""
This module defines types representing entities
and objects in the game.
"""

from src.utility import Vec2


class Sprite:
    def __init__(self, resource):
        self.resource = resource

    def draw(self, entity, context):
        pass


class AsciiSprite(Sprite):
    def __init__(self, resource):
        super(AsciiSprite, self).__init__(resource)

    def draw(self, entity, context):
        context.draw(self.resource, entity.pos)


class Entity:
    """Base entity class for all entities in the game."""

    def __init__(self, name, pos=None):
        self.name = name
        self.pos = pos

        if not pos:
            self.pos = Vec2()

    def update(self, world):
        """
        Called every tick if the entity is in the update set.

        Args:
            world(World): The game world calling the update function.
        """

    def on_event(self, event):
        """
        Callback for recieving events.

        Args:
            event(Event): Information about the event.
        """


class GraphicEntity(Entity):
    """
    Base graphical entity class for all graphical entities
    in the game.
    """

    def __init__(self, name, sprite=None, pos=None):
        super(GraphicEntity, self).__init__(name, pos)
        self.sprite = sprite

    def draw(self, context):
        """
        Called every frame if the entity is in the render set. By default this
        method calls the sprite object's draw function.

        Args:
            context(RenderContext): The render context calling the draw method.
        """
        self.sprite.draw(self, context)
