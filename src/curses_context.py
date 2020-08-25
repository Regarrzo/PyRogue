import curses

from src.utility import Vec2
from src.context import RenderContext


class CursesRenderContext(RenderContext):
    def __init__(self):
        super(CursesRenderContext, self).__init__()
        self.screen = curses.initscr()

        curses.noecho()
        curses.cbreak()

        self.screen.keypad(True)
        self.screen.clear()

    def draw(self, character, pos):
        self.screen.addstr(pos.y, pos.x, character)

    def finish_draw(self):
        self.screen.move(0, 0)

    def clear(self):
        self.screen.refresh()

    def terminate(self):
        curses.nocbreak()
        self.screen.keypad(False)
        curses.echo()
        curses.endwin()
