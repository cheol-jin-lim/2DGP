import random
import json
import os

from pico2d import *

import game_framework
import game_world
from background import Background
from score_title import Score_title
from my_bullet import My_bullet
from plane import *
from player_life import Player_life
from red_enemy import Red_enemy
"""from blue_enemy3 import Blue_enemy3
from green_enemy2 import Green_enemy2"""




name = "stage_state2"


background = None
score_title = None
player_life = None
plane = None
my_bullet = None
font = None
skill_bullet = None
red_enemy = []



def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    # print(left_b,bottom_b,right_b,top_b)
    if left_a > right_b:  # 충돌이 없는경우
        return False
    if right_a < left_b:  # 충돌이 없는경우
        return False
    if top_a < bottom_b:  # 충돌이 없는경우
        return False
    if bottom_a > top_b:  # 충돌이 없는경우
        return False
    return True






def enter():
    global background, score_title, player_life, plane, my_bullet, red_enemy
    background = Background()
    score_title = Score_title()
    player_life = Player_life()
    plane = Plane()
    red_enemy = [Red_enemy(i) for i in range(3)]

    game_world.add_object(background, 0)
    game_world.add_object(score_title, 1)
    game_world.add_object(player_life, 1)
    game_world.add_object(plane, 1)
    for i in range(3):
        game_world.add_object(red_enemy[i], 1)










def exit():
    game_world.clear()
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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            """game_framework.push_state(main_state)"""
        else:
            plane.handle_event(event)



    pass

def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()



    pass





