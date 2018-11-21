import game_framework
from pico2d import *
import main_state
import stage_state2
import title_state

name = "game_over_state"
image = None
logo_time = 0.0
font = None

def enter():
    global image, font
    image = load_image('end.png')
    font = load_font('ENCR10B.TTF', 40)
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
    global image, font
    clear_canvas()
    main_state.background.draw()
    image.draw(400, 300)
    font.draw(170, 400, '[Final Score:%d]' % main_state.stage1_score, (255, 255, 255))
    update_canvas()
    pass




def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass



