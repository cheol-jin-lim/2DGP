import game_framework
from pico2d import *
import main_state

name = "all_state_clear_state"
image = None
logo_time = 0.0
font = None
bgm = None
def enter():
    global image, font, bgm
    image = load_image('images/all_state_clear.png')
    font = load_font('ENCR10B.TTF', 30)
    bgm = load_wav('sounds/all_stage_clear_bgm.wav')
    bgm.set_volume(256)
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
        game_framework.quit()
    delay(0.01)
    logo_time += 0.0025

    pass


def draw():
    global image, font
    clear_canvas()
    main_state.background.draw()
    image.draw(400, 300)
    font.draw(400, 450, '[Final Score:%d]' % main_state.stage1_score, (255, 255, 255))
    font.draw(400, 350, 'Made by Cheol jin Lim' , (255, 255, 255))
    update_canvas()
    pass




def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




