import random
import json
import os

from pico2d import *

import game_framework
import game_world
import title_state
import pause_state2
from background import Background
from score_title import Score_title
from my_bullet import My_bullet
from plane import Plane
from player_life import Player_life
from green_enemy import Green_enemy
from blue_enemy import Blue_enemy
from blue_enemy2 import Blue_enemy2



name = "MainState"


background = None
score_title = None
player_life = None
plane = None
my_bullet = None
green_enemy = []
blue_enemy = []
font = None
skill_bullet = None


def enter():
    global background, score_title,player_life, plane, green_enemy,blue_enemy, blue_enemy2
    background = Background()
    score_title = Score_title()
    player_life = Player_life()
    plane = Plane()
    green_enemy = [Green_enemy(i) for i in range(14)]
    blue_enemy = [Blue_enemy(i) for i in range(14)]
    blue_enemy2 = [Blue_enemy2(i) for i in range(14)]
    game_world.add_object(background, 0)
    game_world.add_object(score_title, 1)
    game_world.add_object(player_life, 1)
    game_world.add_object(plane, 1)
    for i in range(0, 14):
        game_world.add_object(green_enemy[i], 1)
    for i in range(0, 14):
        game_world.add_object(blue_enemy[i], 1)
    for i in range(0, 14):
        game_world.add_object(blue_enemy2[i], 1)




    """green = [Enemy1(90 + 50 * i, 500) for i in range(13)]
    blue = [Enemy2(90 + 50 * i, 450) for i in range(13)]
    blue2 = [Enemy3(90 + 50 * i, 400) for i in range(13)]
    """



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
            game_framework.push_state(pause_state2)
        else:
            plane.handle_event(event)



    pass

def update():
    for game_object in game_world.all_objects():
        game_object.update()
        pass


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()
    pass





