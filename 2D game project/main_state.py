import random
import json
import os

from pico2d import *

import game_framework
import game_world
import title_state
import pause_state2
from background import *
from score_title import *
from plane import *
from player_life import *



name = "MainState"


background = None
score_title = None
player_life = None
plane = None
font = None


def enter():
    global background, score_title, player_life, my_bullet, plane
    background = Background()
    score_title = Score_title()
    player_life = Player_life()
    # my_bullet = My_bullet()
    plane = Plane
    game_world.add_object(background, 0)
    game_world.add_object(score_title, 0)
    game_world.add_object(player_life, 0)
    game_world.add_object(plane, 1)
    # game_world.add_object(my_bullet, 1)





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
        else:
            plane.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
    pass





