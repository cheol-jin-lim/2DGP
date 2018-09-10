from pico2d import *
import math
open_canvas()

# fill here
while(True):
    grass = load_image('grass.png')
    character = load_image('character.png')

    x=0
    y=0
    while(x<750):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x=x+10
        delay(0.01)
    while(y<550):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(750,y)
        y=y+10
        delay(0.01)

    while(x>0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,550)
        x=x-10
        delay(0.01)
    while(y>90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(0,y)
        y=y-10
        delay(0.01)
    character.draw_now(300,90)



    cx,cy = 400,300
    degree=360
    while(degree > 0):
        clear_canvas_now()
        grass.draw_now(400,30)
        x = cx + 200 * math.cos(2*math.pi * degree/360)
        y = cy + 200 * math.sin(2*math.pi * degree/360)
        character.draw_now(x,y)
        degree = degree-5
        delay(0.01)
    degree = 0
    

close_canvas()
