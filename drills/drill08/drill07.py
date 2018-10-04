from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
running = True



hide_cursor()
size = 20
points = [(random.randint(0,1280), random.randint(0,1024))for i in range(size)]
n = 1
frame = 0

def draw_line(p1, p2):
        dir = p2[0]-p1[0]
        for i in range(0,100+1,20):
            t = i / 100

            x = (1-t)*p1[0]+t*p2[0]
            y= (1-t)*p1[1]+t*p2[1]
            global frame
            clear_canvas()
            kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
            if(dir < 0):
                character.clip_draw(frame * 100, 0,90, 90,x, y)
            else:
                character.clip_draw(frame * 100, 100, 90, 90, x, y)


            update_canvas()
            delay(0.08)
            frame = ( frame + 1) % 8


cnt = 0;
while running:
     draw_line(points[n-1], points[n])
     print(points[n-1],points[n])
     n = (n + 1) % size


close_canvas()




