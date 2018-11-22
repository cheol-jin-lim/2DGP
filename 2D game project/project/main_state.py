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


name = "MainState"


background = None
score_title = None
player_life = None
plane = None
my_bullet = None
# green_enemy = []
blue_enemy = []
blue_enemy2 = []
font = None
skill_bullet = None
enemies = []
death_green_enemy_stage1 = []

stage1_score = 0
handle_enemy_count = 0

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
    global background, score_title,player_life, plane, green_enemy,blue_enemy, blue_enemy2, my_bullet, stage1_score,death_green_enemy_stage1
    background = Background()
    score_title = Score_title()
    player_life = Player_life()
    plane = Plane()
    green_enemy = [Green_enemy(i) for i in range(14)]
    blue_enemy = [Blue_enemy(i) for i in range(14)]
    blue_enemy2 = [Blue_enemy2(i) for i in range(14)]
    death_green_enemy_stage1 = [Death_green_enemy_stage1(i) for i in range(14)]
    game_world.add_object(background, 0)
    game_world.add_object(score_title, 1)
    game_world.add_object(player_life, 1)
    game_world.add_object(plane, 1)
    for i in range(0, len(green_enemy)):
        game_world.add_object(green_enemy[i], 1)
        game_world.add_object(blue_enemy[i], 1)
        game_world.add_object(blue_enemy2[i], 1)
        game_world.add_object(death_green_enemy_stage1[i], 1)









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
    global stage1_score,handle_enemy_count
    for game_object in game_world.all_objects():
        game_object.update()




    """for enemy in green_enemy:
        for bullet in bullet_list:
            if enemy != None:
                if collide(enemy, bullet):
                    game_world.remove_object(enemy)
                    game_world.remove_object(bullet)
                    green_enemy.remove(enemy)
                    death_enemy.dead_enemy = True
                    bullet_list.remove(bullet)
                    # enemy.death_green_enemy = 1
                    # death_enemy.death_green = 1
                    stage1_score += 100
                    handle_enemy_count += 1
                    break"""

    for enemy in blue_enemy:
        for bullet in bullet_list:
            if enemy != None:
                if collide(enemy, bullet):
                    game_world.remove_object(enemy)
                    game_world.remove_object(bullet)
                    blue_enemy.remove(enemy)
                    bullet_list.remove(bullet)
                    # enemy.death_green_enemy = 1
                    stage1_score += 100
                    handle_enemy_count += 1
                    break

    for enemy in blue_enemy2:
        for bullet in bullet_list:
            if enemy != None:
                if collide(enemy, bullet):
                    game_world.remove_object(enemy)
                    game_world.remove_object(bullet)
                    blue_enemy2.remove(enemy)
                    bullet_list.remove(bullet)
                    # enemy.death_green_enemy = 1
                    stage1_score += 100
                    handle_enemy_count += 1
                    break


    for i in range(len(green_enemy)):
        for j in range(len(bullet_list)):
            if green_enemy[i] != 0:
                if collide(green_enemy[i], bullet_list[j]):
                    game_world.remove_object(green_enemy[i])
                    game_world.remove_object(bullet_list[j])
                    death_green_enemy_stage1[i].dead_enemy = True
                    green_enemy[i] = 0

                    # death_enemy.remove(death_enemy[i])
                    stage1_score += 100
                    handle_enemy_count += 1
                    break



    """for i in range(len(blue_enemy)):
        for bullet in bullet_list:
            if blue_enemy[i] != 0:
                if collide(blue_enemy[i], bullet):
                    blue_enemy[i].death_blue_enemy = 1
                    # game_world.remove_object(blue_enemy[i])
                    game_world.remove_object(bullet)
                    blue_enemy[i] = 0
                    stage1_score += 100
                    handle_enemy_count += 1
                    break


    for i in range(len(blue_enemy2)):
        for bullet in bullet_list:
            if blue_enemy2[i] != 0:
                if collide(blue_enemy2[i], bullet):
                    blue_enemy2[i].death_blue_enemy2 = 1
                    # game_world.remove_object(blue_enemy2[i])
                    game_world.remove_object(bullet)
                    blue_enemy2[i] = 0
                    stage1_score += 100
                    handle_enemy_count += 1
                    break"""


    if handle_enemy_count == 42:   # 42마리
        game_framework.push_state(stage1_clear_state)
        game_world.remove_object(plane)
        game_world.remove_object(background)
        game_world.remove_object(score_title)
        game_world.remove_object(player_life)
        for i in range(len(green_enemy)):
            """game_world.remove_object(green_enemy[i])
            # game_world.remove_object(blue_enemy[i])
             game_world.remove_object(blue_enemy2[i])"""
            # game_world.remove_object(death_enemy[i])









def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()




    update_canvas()



    pass





