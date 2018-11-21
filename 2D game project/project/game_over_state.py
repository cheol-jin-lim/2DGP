import game_framework
from pico2d import *
import main_state
import stage_state2
import title_state

name = "game_over_state"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('end.png')
    pass


def exit():
    global image
    del(image)
    pass

def update():
    global logo_time

    if(logo_time > 0.5):
        logo_time = 0
        # game_framework.quit()
        game_framework.quit()
    delay(0.01)
    logo_time += 0.0025

    pass


def draw():
    global image
    clear_canvas()
    main_state.background.draw()
    image.draw(400, 300)
    update_canvas()
    pass




def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




