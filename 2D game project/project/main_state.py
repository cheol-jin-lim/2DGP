import random
import json
import os

from pico2d import *

import game_framework
import game_world
import title_state
import pause_state2
import stage1_clear_state
from background import Background
from score_title import Score_title
from my_bullet import My_bullet
from plane import *
from player_life import Player_life
from green_enemy import Green_enemy
from blue_enemy import Blue_enemy
from blue_enemy2 import Blue_enemy2
from death_green_enemy_stage1 import Death_green_enemy_stage1
from death_blue_enemy_stage1 import Death_blue_enemy_stage1
from death_blue_enemy2_stage1 import Death_blue_enemy2_stage1

name = "MainState"


background = None
score_title = None
player_life = None
plane = None
my_bullet = None
green_enemy = []
blue_enemy = []
blue_enemy2 = []
font = None
skill_bullet = None
death_green_enemy_stage1 = None
death_blue_enemy_stage1 = []
death_blue_enemy2_stage1 = []
stage1_score = 0
handle_enemy_count = 0
stage1_clear_wait_time = 0.0


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
    global background, score_title,player_life, plane, green_enemy,blue_enemy, blue_enemy2, my_bullet, stage1_score,death_green_enemy_stage1\
        ,death_blue_enemy_stage1,death_blue_enemy2_stage1
    background = Background()
    score_title = Score_title()
    player_life = Player_life()
    plane = Plane()
    green_enemy = [Green_enemy(i) for i in range(14)]
    blue_enemy = [Blue_enemy(i) for i in range(14)]
    blue_enemy2 = [Blue_enemy2(i) for i in range(14)]
    death_green_enemy_stage1 = [Death_green_enemy_stage1(i) for i in range(14)]
    death_blue_enemy_stage1 = [Death_blue_enemy_stage1(i) for i in range(14)]
    death_blue_enemy2_stage1 = [Death_blue_enemy2_stage1(i) for i in range(14)]
    game_world.add_object(background, 0)
    game_world.add_object(score_title, 1)
    game_world.add_object(player_life, 1)
    game_world.add_object(plane, 1)
    game_world.add_objects(green_enemy, 1)
    game_world.add_objects(blue_enemy, 1)
    game_world.add_objects(blue_enemy2, 1)
    game_world.add_objects(death_green_enemy_stage1, 1)
    game_world.add_objects(death_blue_enemy_stage1, 1)
    game_world.add_objects(death_blue_enemy2_stage1, 1)









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
            game_framework.push_state(pause_state2)
        else:
            plane.handle_event(event)












    pass

def update():
    global stage1_score,handle_enemy_count,stage1_clear_wait_time
    for game_object in game_world.all_objects():
        game_object.update()

    for enemy in green_enemy:
        for bullet in bullet_list:
            if collide(enemy, bullet):
                green_enemy.remove(enemy)
                bullet_list.remove(bullet)
                game_world.remove_object(enemy)
                game_world.remove_object(bullet)
                death_green_enemy_stage1[enemy.count].dead_enemy = True
                death_green_enemy_stage1[enemy.count].explosion()
                stage1_score += 100
                handle_enemy_count += 1

    for enemy in blue_enemy:
        for bullet in bullet_list:
            if collide(enemy, bullet):
                blue_enemy.remove(enemy)
                bullet_list.remove(bullet)
                game_world.remove_object(enemy)
                game_world.remove_object(bullet)
                death_blue_enemy_stage1[enemy.count].dead_enemy = True
                death_blue_enemy_stage1[enemy.count].explosion()
                stage1_score += 100
                handle_enemy_count += 1

    for enemy in blue_enemy2:
        for bullet in bullet_list:
            if collide(enemy, bullet):
                blue_enemy2.remove(enemy)
                bullet_list.remove(bullet)
                game_world.remove_object(enemy)
                game_world.remove_object(bullet)
                death_blue_enemy2_stage1[enemy.count].dead_enemy = True
                death_blue_enemy2_stage1[enemy.count].explosion()
                stage1_score += 100
                handle_enemy_count += 1




    if handle_enemy_count == 42:   # 42마리
        if stage1_clear_wait_time > 0.5:
            stage1_clear_wait_time = 0
            game_world.remove_object(plane)
            game_world.remove_object(background)
            game_world.remove_object(score_title)
            game_world.remove_object(player_life)
            game_world.remove_object(death_green_enemy_stage1)
            game_world.remove_object(death_blue_enemy_stage1)
            game_world.remove_object(death_blue_enemy2_stage1)
            game_world.remove_object(death_green_enemy_stage1)
            game_world.remove_object(death_blue_enemy_stage1)
            game_world.remove_object(death_blue_enemy2_stage1)
            game_framework.change_state(stage1_clear_state)
            bullet_list.clear()
        delay(0.01)
        stage1_clear_wait_time += 0.01










def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()




    update_canvas()



    pass





