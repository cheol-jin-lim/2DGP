from pico2d import *
open_canvas(800,600)
grass = load_image('grass.png')
character = load_image('animation_sheet.png')




def one_position():
    x,y = 203,535
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(0,200,100,100,x,y)
    update_canvas()
    get_events()
pass

def two_position():
    x, y = 203, 535
    frame = 0
    while x > 132 and y > 243:

        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame*100,0,100,100,x,y)

        update_canvas()
        frame = (frame + 1) % 8
        x = x - 2
        y = y - 10 # x축이 이동하는 거리보다 y축이 이동하는 거리를 크게해줌.

        get_events()

    pass
def three_position():
    x,y = 132,243
    frame = 0
    while x < 535 and y < 470:

        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)

        update_canvas()
        frame = (frame % 8) + 1
        x = x + 10
        y = y + 5

        get_events()


    pass
def four_position():
    x,y = 535,470
    frame = 0
    while x > 477 and y > 203:

        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)

        update_canvas()
        frame = (frame % 8) + 1
        x = x - 2
        y = y - 8

        get_events()
    pass
def five_position():
    x,y = 477,203
    frame = 0
    while x < 715 and y > 136:

        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)

        update_canvas()
        frame = (frame % 8) + 1
        x = x + 8
        y = y - 2

        get_events()
    pass
def six_position():
    x,y = 715,136
    frame = 0
    while x > 316 and y < 225:

        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)

        update_canvas()
        frame = (frame % 8) + 1
        x = x - 15
        y = y + 3

        get_events()
    pass
def seven_position():
    x,y = 316,225
    frame = 0
    while x < 510 and y > 92:

        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)

        update_canvas()
        frame = (frame % 8) + 1
        x = x + 10
        y = y - 10

        get_events()
    pass
def eight_position():
    x,y = 510,92
    frame = 0
    while x < 692 and y < 518:

        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)

        update_canvas()
        frame = (frame % 8) + 1
        x = x + 5
        y = y + 10

        get_events()
    pass
def nine_position():
    x,y = 692,518
    frame = 0
    while x > 682 and y > 336:

        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)

        update_canvas()
        frame = (frame % 8) + 1
        x = x - 1
        y = y - 20

        get_events()
    pass
def ten_position():
    x,y = 682,336
    frame = 0
    while x < 712 and y < 349:

        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)

        update_canvas()
        frame = (frame % 8) + 1
        x = x + 9
        y = y + 3

        get_events()
    pass


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







close_canvas()

