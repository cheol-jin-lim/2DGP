import game_framework
from pico2d import *
import main_state


image = None
name = "Pause_state"
time = 0
select = False


def enter():
    global image
    image = load_image('pause.png')
    pass


def exit():
    global image
    del (image)
    pass


def update():
    global time,select
    time += 0.1
    if time >= 1:
        if select == False:
            select = True
            time = 0
        elif select == True:
            select = False
            time = 0




    pass


def draw():
    clear_canvas()
    global select
    if select == True:
        image.draw(400, 300)
    main_state.space.draw()
    main_state.plane.draw()
    update_canvas()
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()

    pass

def pause():
    pass


def resume():
    pass