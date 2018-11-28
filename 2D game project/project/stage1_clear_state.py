import game_framework
from pico2d import *
import stage_state2
import game_world
import death_green_enemy_stage1
import death_blue_enemy_stage1
import death_blue_enemy2_stage1
name = "stage1_clear_state"
image = None
logo_time = 0.0
bgm = None

def enter():
    global image, bgm
    image = load_image('images/stage_clear_image.png')
    bgm = load_wav('sounds/stage_clear_sound.wav')
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
        game_framework.change_state(stage_state2)
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




