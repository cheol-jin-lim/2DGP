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
life = None
score_title = None
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


class Life:
    def __init__(self):
        self.image = load_image('player_life.png')

    def draw(self):
        self.image.draw(100,550)

class Score_title:
    def __init__(self):
        self.image = load_image('score_title.png')

    def draw(self):
        self.image.draw(400,580)




def enter():
    global plane, space, life, score_title
    space = Space()
    plane = Plane()
    life = Life()
    score_title = Score_title()
    pass


def exit():
    global space, plane, life, score_title
    del(space)
    del(plane)
    del(life)
    del(score_title)
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
    life.draw()
    score_title.draw()
    plane.draw()
    update_canvas()
    pass





