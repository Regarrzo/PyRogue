from src.sharedset import Sharedset


class World:
    def __init__(self, render_context=None):
        self.objects = Sharedset()

        self.update_objects = Sharedset(master=self.objects)
        self.render_objects = Sharedset(master=self.objects)

        self.render_context = render_context

    def draw(self):
        self.render_context.clear()

        for entity in self.render_objects:
            entity.draw(self.render_context)

        self.render_context.finish_draw()
