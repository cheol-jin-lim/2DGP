import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state2


name = "MainState"

space = None
plane = None
font = None



class Space:
    def __init__(self):
        self.image = load_image('backgroundmap.png')

    def draw(self):
        self.image.draw(400, 300)

class Plane:
    def __init__(self):
        self.x, self.y = 400, 50
        self.image = load_image('Plane.png')
        self.dir = 1

    def update(self):
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.draw(self.x, self.y)




def enter():
    global plane, space
    space = Space()
    plane = Plane()
    pass


def exit():
    global space, plane
    del(space)
    del(plane)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state2)


    pass


def update():
    plane.update()
    pass


def draw():
    clear_canvas()
    space.draw()
    plane.draw()
    update_canvas()
    pass





