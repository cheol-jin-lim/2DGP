import game_framework
from pico2d import *
import stage_state2
# from green_enemy import Green_enemy
import game_world
import death_green_enemy_stage1
import death_blue_enemy_stage1
import death_blue_enemy2_stage1
name = "stage1_clear_state"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('stage_clear_image.png')
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




