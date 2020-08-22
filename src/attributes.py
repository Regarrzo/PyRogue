

def _extend_init(**extend_attributes):
    def extender(func):
        def __init__(self, *args, **kwargs):
            func(self, *args, **kwargs)

            for name, value in extend_attributes.items():
                setattr(self, name, value)
        
        return __init__
    return extender


def render(char):
    def attribute(EntityType):
        EntityType.__init__ = _extend_init(char=char)(EntityType.__init__)
        EntityType.attributes.add("consolerender")

        return EntityType

    return attribute


def script(script):
    def attribute(EntityType):
        EntityType.__init__ = _extend_init(script=script)(EntityType.__init__)
        EntityType.attributes.add("script")

        def update(self, world):
            self.script(self, world)

        EntityType.update = update

        return EntityType

    return attribute