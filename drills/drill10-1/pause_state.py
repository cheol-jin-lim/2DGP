import game_framework
from pico2d import *


image = None
name = "Pause_state"

def enter():
    global image
    image = load_image('pause.png')
    pass

def exit():
    global image
    del (image)
    pass
import main_state
def update():

    pass

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()

    pass

def pause():
    pass


def resume():
    pass