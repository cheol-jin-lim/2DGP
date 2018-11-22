import random
import json
import os

from pico2d import *

import game_framework
import game_world
import game_over_state
import stage_2_clear_state
from background import Background
from score_title import Score_title
from my_bullet import My_bullet
from plane import *
from player_life import Player_life
from red_enemy import Red_enemy
from blue_enemy3 import Blue_enemy3
from green_enemy2 import Green_enemy2
from green_enemy import Green_enemy
from blue_enemy import Blue_enemy
from blue_enemy2 import Blue_enemy2
from middle_boss_enemy import Middle_boss_enemy
from blue_enemy4 import Blue_enemy4
from blue_enemy5 import Blue_enemy5
import main_state

name = "stage_state2"


background = None
score_title = None
player_life = None
plane = None
my_bullet = None
font = None
skill_bullet = None
red_enemy = []
green_enemy = []
blue_enemy = []
blue_enemy2 = []
blue_enemy3 = []
green_enemy2 = []
middle_boss_enemy = []
blue_enemy4 = []
blue_enemy5 = []
player_life_number = 2
stage2_score = 0


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
    pass



def get_plane():
    return plane


def enter():
    global background, score_title, player_life, plane, my_bullet, red_enemy, green_enemy, blue_enemy, blue_enemy2,blue_enemy3\
        ,green_enemy2,middle_boss_enemy, blue_enemy4, blue_enemy5
    background = Background()
    score_title = Score_title()
    player_life = Player_life()
    plane = Plane()
    red_enemy = [Red_enemy(i) for i in range(5)]
    green_enemy = [Green_enemy(i) for i in range(5)]
    blue_enemy = [Blue_enemy(i) for i in range(5)]
    blue_enemy2 = [Blue_enemy2(i) for i in range(5)]
    blue_enemy4 = [Blue_enemy4(i) for i in range(5)]
    blue_enemy5 = [Blue_enemy5(i) for i in range(5)]
    green_enemy2 = [Green_enemy2(i) for i in range(3)]
    middle_boss_enemy = [Middle_boss_enemy(i) for i in range(3)]
    blue_enemy3 = [Blue_enemy3(i) for i in range(3)]
    game_world.add_object(background, 0)
    game_world.add_object(score_title, 1)
    game_world.add_object(player_life, 1)
    game_world.add_object(plane, 1)
    # game_world.add_object(blue_enemy3, 1)
    # game_world.add_object(green_enemy2, 1)
    # game_world.add_object(middle_boss_enemy, 1)
    for i in range(5):
        game_world.add_object(green_enemy[i], 1)
        game_world.add_object(blue_enemy[i], 1)
        game_world.add_object(blue_enemy2[i], 1)
        game_world.add_object(red_enemy[i], 1)
        game_world.add_object(blue_enemy4[i], 1)
        game_world.add_object(blue_enemy5[i], 1)
    for i in range(3):
        game_world.add_object(green_enemy2[i], 1)
        game_world.add_object(middle_boss_enemy[i], 1)
        game_world.add_object(blue_enemy3[i], 1)

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

    if player_life_number == 0:
        game_framework.change_state(game_over_state)




    pass

def update():
    global green_enemy2,plane,player_life_number,blue_enemy3,middle_boss_enemy,handle_enemy_count,stage2_score
    for game_object in game_world.all_objects():
        game_object.update()




    for i in range(len(red_enemy)):
        for bullet in bullet_list:
            if red_enemy[i] != None:
                if collide(red_enemy[i], bullet):
                    # red_enemy[i].death_red_enemy = 1
                    # game_world.remove_object(red_enemy[i])
                    game_world.remove_object(bullet)
                    red_enemy[i] = None
                    handle_enemy_count += 1
                    main_state.stage1_score += 500
                    break


    for i in range(len(green_enemy)):
        for bullet in bullet_list:
            if green_enemy[i] != None:
                if collide(green_enemy[i], bullet):
                    # green_enemy[i].death_green_enemy = 1
                    # game_world.remove_object(red_enemy[i])
                    game_world.remove_object(bullet)
                    green_enemy[i] = None
                    handle_enemy_count += 1
                    main_state.stage1_score += 500
                    break


    for i in range(len(blue_enemy)):
        for bullet in bullet_list:
            if blue_enemy[i] != None:
                if collide(blue_enemy[i], bullet):
                    # blue_enemy[i].death_blue_enemy = 1
                    # game_world.remove_object(red_enemy[i])
                    game_world.remove_object(bullet)
                    blue_enemy[i] = None
                    handle_enemy_count += 1
                    main_state.stage1_score += 500
                    break


    for i in range(len(blue_enemy2)):
        for bullet in bullet_list:
            if blue_enemy2[i] != None:
                if collide(blue_enemy2[i], bullet):
                    # blue_enemy2[i].death_blue_enemy2 = 1
                    # game_world.remove_object(red_enemy[i])
                    game_world.remove_object(bullet)
                    blue_enemy2[i] = None
                    handle_enemy_count += 1
                    main_state.stage1_score += 500
                    break

    for i in range(len(blue_enemy4)):
        for bullet in bullet_list:
            if blue_enemy4[i] != None:
                if collide(blue_enemy4[i], bullet):
                    # blue_enemy4[i].death_blue_enemy4 = 1
                    # game_world.remove_object(red_enemy[i])
                    game_world.remove_object(bullet)
                    blue_enemy4[i] = None
                    handle_enemy_count += 1
                    main_state.stage1_score += 500
                    break

    for i in range(len(blue_enemy5)):
        for bullet in bullet_list:
            if blue_enemy5[i] != None:
                if collide(blue_enemy5[i], bullet):
                    # blue_enemy5[i].death_blue_enemy5 = 1
                    # game_world.remove_object(red_enemy[i])
                    game_world.remove_object(bullet)
                    blue_enemy5[i] = None
                    handle_enemy_count += 1
                    main_state.stage1_score += 500
                    break


    for enemy in green_enemy2:
        for bullet in bullet_list:
            if enemy != None:
                if collide(enemy, bullet):
                    # green_enemy2[i].death_green_enemy2 = 1
                    game_world.remove_object(enemy)
                    game_world.remove_object(bullet)
                    green_enemy2.remove(enemy)
                    bullet_list.remove(bullet)
                    handle_enemy_count += 1
                    main_state.stage1_score += 500
                    break


    for enemy in blue_enemy3:
        for bullet in bullet_list:
            if enemy != None:
                if collide(enemy, bullet):
                    game_world.remove_object(enemy)
                    game_world.remove_object(bullet)
                    blue_enemy3.remove(enemy)
                    bullet_list.remove(bullet)
                    handle_enemy_count += 1
                    main_state.stage1_score += 500
                    break

    for enemy in middle_boss_enemy:
        for bullet in bullet_list:
            if enemy != None:
                if collide(enemy, bullet):
                    game_world.remove_object(enemy)
                    game_world.remove_object(bullet)
                    middle_boss_enemy.remove(enemy)
                    bullet_list.remove(bullet)
                    handle_enemy_count += 1
                    main_state.stage1_score += 500
                    break

    for enemy in middle_boss_enemy:
        if collide(enemy, plane):
            player_life_number -= 1

    for enemy in blue_enemy3:
        if collide(enemy, plane):
            player_life_number -= 1

    for enemy in green_enemy2:
        if collide(enemy, plane):
            player_life_number -= 1


    if player_life_number == 1:
        player_life.my_life = 1

    if handle_enemy_count == 2:   # 39마리
        game_framework.push_state(stage_2_clear_state)
        game_world.remove_object(plane)
        game_world.remove_object(background)
        game_world.remove_object(score_title)
        game_world.remove_object(player_life)
        for i in range(len(green_enemy)):
            print(len(green_enemy))
            game_world.remove_object(green_enemy[i])
            game_world.remove_object(blue_enemy[i])
            game_world.remove_object(blue_enemy2[i])
            game_world.remove_object(blue_enemy4[i])
            game_world.remove_object(blue_enemy5[i])
            game_world.remove_object(red_enemy[i])



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()



    pass





