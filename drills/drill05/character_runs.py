from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def one_position():

    x,y = 203,535
    clear_canvas()
    grass.draw(400, 30)
    character.clip.draw(0,300,100,100,203,535)

    update_canvas()
    get_events()


    pass
def two_position():
    pass
def three_position():
    pass
def four_position():
    pass
def five_position():
    pass
def six_position():
    pass
def seven_position():
    pass
def eight_position():
    pass
def nine_position():
    pass
def ten_position():
    pass

def make_running():
    while True:
        one_position()
        two_position()
        three_position()
        four_position()
        five_position()
        six_position()
        seven_position()
        eight_position()
        nine_position()
        ten_position()
    pass






close_canvas()

