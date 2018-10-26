from pico2d import *
"""from background import Background
from score_title import Score_title
from player_life import Player_life
from green_enemy import Green_enemy """
from my_bullet import My_bullet
from my_bullet import Skill_bullet
import game_world


RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP,BULLET_A,SKILL_S = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_a): BULLET_A,
    (SDL_KEYDOWN, SDLK_s): SKILL_S
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
        if event == BULLET_A:
            plane.fire_bullet()
            plane.bullet_count += 1
            print(plane.bullet_count)
        if plane.bullet_count == 20:
            plane.skill_bullet_count += 1
            plane.bullet_count = 0
            print("------------------------")
            print(plane.skill_bullet_count)
            print("------------------------")




        if (event == SKILL_S) and (plane.skill_bullet_count) > 0:
            plane.fire_skill_bullet()
            plane.skill_bullet_count -= 1

            pass

    @staticmethod
    def do(plane):
        plane.x += plane.velocity * 3
        plane.x = clamp(25, plane.x, 800 - 25)

    @staticmethod
    def draw(plane):
        if plane.velocity == 1:
            plane.image.draw(plane.x, plane.y)
        else:
            plane.image.draw(plane.x, plane.y)


next_state_table = {
    Runstate: {RIGHT_UP: Runstate, LEFT_UP: Runstate, LEFT_DOWN: Runstate, RIGHT_DOWN: Runstate, BULLET_A: Runstate, SKILL_S: Runstate}

}


class Plane:

    def __init__(self):
        self.x, self.y =  400, 60
        self.image = load_image('player.png')
        self.dir = 1
        self.velocity = 0
        self.event_que = []
        self.cur_state = Runstate
        self.cur_state.enter(self, None)
        self.bullet_count = 0
        self.skill_bullet_count = 0

    def fire_bullet(self):
        my_bullet =My_bullet(self.x, self.y, self.dir * 3)
        game_world.add_object(my_bullet, 1)
        pass

    def fire_skill_bullet(self):
        skill_bullet = Skill_bullet(self.x, self.y, self.dir * 3)
        game_world.add_object(skill_bullet, 1)
        pass

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