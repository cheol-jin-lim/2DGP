from pico2d import *
open_canvas(800,600)
grass = load_image('grass.png')
character = load_image('animation_sheet.png')
frame = 0



def one_position():
    x,y = 203,535
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame,200,100,100,x,y)
    update_canvas()
    get_events()
pass

def two_position():
    x, y = 203, 535
    while x > 132 and y > 243:
        frame = 0
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame*100,0,100,100,x,y)

        update_canvas()
        frame = (frame + 1) % 8
        x = x - 2
        y = y - 10 # x축이 이동하는 거리보다 y축이 이동하는 거리를 크게해줌.
        delay(0.05)
        get_events()

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


# while True:
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







close_canvas()

