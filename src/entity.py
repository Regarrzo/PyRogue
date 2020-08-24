
def EntityType(name, attributes):
    """
    Create a new EntityType class with the specified name and 
    attributes.

    Parameters:

    name: Default name of instances of the EntityType class
    attributes: Iterable containing class decorators
    """

    class Entity:

        attributes = set()

        def __init__(self, name=name):
            self.name = name

    for attribute in attributes:
        Entity = attribute(Entity)

    return Entity
