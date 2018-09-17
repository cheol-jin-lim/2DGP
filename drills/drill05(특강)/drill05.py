from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


def move_from_center_to_right():
    x,y = 800 // 2,90
    while x < 800 - 25:
        clear_canvas_now()
        grass.draw(400,30)
        character.draw_now(x,y)
        x = x + 10
        delay(0.01)
    pass
def move_up():
    x,y = 800 - 25, 90
    while y < 600 - 50:
        clear_canvas_now()
        grass.draw(400,30)
        character.draw_now(x,y)
        y = y + 10
        delay(0.01)
    pass
def move_left():
    x, y = 800 - 25, 600 - 50
    while x > 0 + 25:
        clear_canvas_now()
        grass.draw(400, 30)
        character.draw_now(x, y)
        x = x - 10
        delay(0.01)
    pass
def move_down():
    x, y = 0+25, 600 - 50
    while y > 0 + 50:
        clear_canvas_now()
        grass.draw(400, 30)
        character.draw_now(x, y)
        y = y- 10
        delay(0.01)
    pass
def move_from_left_to_center():
    x, y = 0+25, 90
    while x < 800 // 2:
        clear_canvas_now()
        grass.draw(400, 30)
        character.draw_now(x, y)
        x = x + 10
        delay(0.01)
    pass




def make_rectangle():
    move_from_center_to_right()
    move_up()
    move_left()
    move_down()
    move_from_left_to_center()
    pass

import math

def make_circle():
    cx, cy, r = 800 // 2, 600 // 2, (600-180) // 2
    degree = -90
    while degree < 270:
        radian = math.radians(degree)
        x = cx + r * math.cos(radian)
        y = cy + r * math.sin(radian)
        degree = degree + 1
        clear_canvas_now()
        grass.draw(400, 30)
        character.draw_now(x, y)
        degree = degree + 1
        delay(0.01)

    pass



while True:
    # make_rectangle()
    make_circle()


close_canvas()
