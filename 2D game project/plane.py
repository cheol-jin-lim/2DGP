from pico2d import *
from background import *
from score_title import *
from player_life import *
from green_enemy import *

import game_world


RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP = range(4)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
}

class Runstate:

    @staticmethod
    def enter(plane, event):
        if event == RIGHT_DOWN:
            plane.velocity += 1
        elif event == LEFT_DOWN:
            plane.velocity -= 1
        elif event == RIGHT_UP:
            plane.velocity -= 1
        elif event == LEFT_UP:
            plane.velocity += 1

    @staticmethod
    def exit(plane, event):
            pass

    @staticmethod
    def do(plane):
        plane.x += plane.velocity
        plane.x = clamp(25, plane.x, 800 - 25)

    @staticmethod
    def draw(plane):
        if plane.velocity == 1:
            plane.image.draw(plane.x, plane.y)
        else:
            plane.image.draw(plane.x, plane.y)


next_state_table = {
    Runstate: {RIGHT_UP: Runstate, LEFT_UP: Runstate, LEFT_DOWN: Runstate, RIGHT_DOWN: Runstate}

}


class Plane:

    def __init__(self):
        self.x, self.y =  400, 60
        self.image = load_image('player.png')
        self.dir = 1
        self.velocity = 0
        self.event_que = []
        # self.cur_state = IdleState
        # self.cur_state.enter(self, None)

    def fire_ball(self):
        my_bullet =My_bullet(self.x, self.y, self.dir * 3)
        game_world.add_object(my_bullet, 1)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)