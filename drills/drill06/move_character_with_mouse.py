from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global mouse_x, mouse_y
    global click_x, click_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            click_x, click_y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')



running = True
mouse_x, mouse_y = 0, 0
click_x,click_y = 0, 0
frame = 0
hide_cursor()
my_x, my_y = 500, 500
t = 0

def move(x, y):
        global my_x, my_y, click_x, click_y, frame, t

        def moveright():
            my_x = my_x + 1
            pass

        def moveleft():
            global my_x
            my_x = my_x - 1
            pass

        def moveup():
            global my_y
            my_y = my_y + 1
            pass

        def movedown():
            global my_y
            my_y = my_y - 1
            pass

        if (click_x-my_x < 0):
            t = 1
        elif(click_x-my_x>0):
            t = 2

        if (click_y - my_y <0):
            t = 1
        elif(click_y-my_y>0):
            t = 2

        if (t==1):
            moveleft()
        elif(t==2):
            moveright()

        if(t==1):
            movedown()
        elif(t==2):
            moveup()


while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if(t == 1):
        character.clip_draw(frame * 100, 0, 100, 100, my_x, my_y)
    elif(t==2):
        character.clip_draw(frame * 100, 100 * 1, 100, 100, my_x, my_y)
    mouse.draw(mouse_x, mouse_y)
    update_canvas()
    frame = (frame + 1) % 8
    move(my_x, my_y)


    handle_events()

close_canvas()




