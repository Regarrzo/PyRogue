import attributes

def EntityType(name, attributes):

    class Entity:

        attributes = set()

        def __init__(self, name=name):
            self.name = name

    for attribute in attributes:
        Entity = attribute(Entity)

    return Entity

Sword = EntityType("Sword", (attributes.render("/"), attributes.script(None)))

a = Sword()
print(a.attributes)
print(a.__dict__)
