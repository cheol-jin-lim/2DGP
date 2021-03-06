import game_framework
from pico2d import *


name = "TitleState"
image = None


bgm = None

def enter():
    global image, bgm
    image = load_image('images/main.png')
    bgm = load_wav('sounds/01StageIntro.wav')
    bgm.set_volume(64)
    bgm.play()
    pass


def exit():
    global image
    del(image)
    pass

import main_state

def handle_events():
    global bgm
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.push_state(main_state)
                bgm.set_volume(0)
    pass


def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
    pass







def update():
    pass


def pause():
    pass


def resume():
    pass






