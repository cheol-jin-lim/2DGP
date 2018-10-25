from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
running = True



hide_cursor()
size = 20
points = [(random.randint(0,1280-50), random.randint(0,1024-50))for i in range(size)]
n = 1
frame = 0

def draw_line(p1, p2,p3,p4):
        dir = p2[0]-p1[0]
        for i in range(0,50+1,20):
            t = i / 100

            x =(2*t**2-3*t+1)*p1[0]+(-4*t**2+4*t)*p2[0]+(2*t**2-t)*p3[0]
            y= (2*t**2-3*t+1)*p1[1]+(-4*t**2+4*t)*p2[1]+(2*t**2-t)*p3[1]
            global frame
            clear_canvas()
            kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
            if(dir < 0):
                character.clip_draw(frame * 100, 0,90, 90,x, y)
            else:
                character.clip_draw(frame * 100, 100, 90, 90, x, y)
        for i in range(0, 100 + 1, 2):
            t = i / 100
            x = ((-t**3+2*t**2-t)*p1[0]+(3*t**3 - 5*t**2 + 2)*p2[0]+(-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
            y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + ( -3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2
            clear_canvas()
            kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
            if (dir < 0):
                character.clip_draw(frame * 100, 0, 90, 90, x, y)
            else:
                character.clip_draw(frame * 100, 100, 90, 90, x, y)
        for i in range(50,100+1,2);


            update_canvas()
            delay(0.08)
            frame = ( frame + 1) % 8


cnt = 0;
while running:
     draw_line(points[n-1], points[n])
     print(points[n-1],points[n])
     n = (n + 1) % size


close_canvas()




