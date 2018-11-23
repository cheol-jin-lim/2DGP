import game_framework
from pico2d import *
import stage_state2
import final_stage_state
# from green_enemy import Green_enemy

name = "stage1_clear_state"
image = None
logo_time = 0.0
bgm = None

def enter():
    global image
    image = load_image('stage_clear_image.png')
    bgm = load_wav('stage_clear_sound.wav')
    bgm.set_volume(64)
    bgm.play()
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
        game_framework.change_state(final_stage_state)
    delay(0.01)
    logo_time += 0.0025

    pass


def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
    pass




def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




