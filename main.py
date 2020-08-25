import traceback
from time import sleep


from src.entity import GraphicEntity, AsciiSprite
from src.curses_context import CursesRenderContext
from src.world import World
from src.utility import Vec2

render_context = CursesRenderContext()


def main():
    player_sprite = AsciiSprite("@")
    player_entity = GraphicEntity("Player", player_sprite, Vec2(2, 2))

    game_world = World(render_context)
    game_world.objects.add(player_entity, (game_world.render_objects,))

    while True:
        game_world.draw()
        sleep(1/30)

    render_context.terminate()


print("bla")
try:
    main()
except Exception as e:
    render_context.terminate()
    traceback.print_exc()
