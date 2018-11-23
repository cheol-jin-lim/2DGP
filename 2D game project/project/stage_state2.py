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
from death_red_enemy_stage2 import Death_red_enemy_stage2
from death_green_enemy_stage1 import Death_green_enemy_stage1
from death_blue_enemy4_stage2 import Death_blue_enemy4_stage2
from death_blue_enemy5_stage2 import Death_blue_enemy5_stage2
from death_blue_enemy_stage1 import Death_blue_enemy_stage1
from death_blue_enemy2_stage1 import Death_blue_enemy2_stage1
from death_green_enemy2 import Dead_effect
from death_boss_enemy import Dead_effect
from death_blue_enemy3 import Dead_effect
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
death_blue_enemy_stage1 = []
death_blue_enemy2_stage1 = []
death_red_enemy_stage2 = []
death_green_enemy_stage1 = []
death_blue_enemy4_stage2 = []
death_blue_enemy5_stage2 = []
player_life_number = 2
stage2_score = 0
test_dead = None
test_dead_boss = None
test_dead_blue_enemy3 = None
stage2_clear_wait_time = 0.0


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
        ,green_enemy2,middle_boss_enemy, blue_enemy4, blue_enemy5, death_red_enemy_stage2, death_green_enemy_stage1, \
        death_blue_enemy4_stage2, death_blue_enemy5_stage2,death_blue_enemy2_stage1,death_blue_enemy_stage1
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
    death_red_enemy_stage2 = [Death_red_enemy_stage2(i) for i in range(5)]
    death_green_enemy_stage1 = [Death_green_enemy_stage1(i) for i in range(5)]
    death_blue_enemy_stage1 = [Death_blue_enemy_stage1(i) for i in range(5)]
    death_blue_enemy2_stage1 = [Death_blue_enemy2_stage1(i) for i in range(5)]
    death_blue_enemy4_stage2 = [Death_blue_enemy4_stage2(i) for i in range(5)]
    death_blue_enemy5_stage2 = [Death_blue_enemy5_stage2(i) for i in range(5)]
    game_world.add_object(background, 0)
    game_world.add_object(score_title, 1)
    game_world.add_object(player_life, 1)
    game_world.add_object(plane, 1)
    game_world.add_objects(death_red_enemy_stage2, 1)
    game_world.add_objects(death_green_enemy_stage1, 1)
    game_world.add_objects(death_blue_enemy4_stage2, 1)
    game_world.add_objects(death_blue_enemy5_stage2, 1)
    game_world.add_objects(death_blue_enemy_stage1, 1)
    game_world.add_objects(death_blue_enemy2_stage1, 1)
    game_world.add_objects(green_enemy, 1)
    game_world.add_objects(blue_enemy, 1)
    game_world.add_objects(blue_enemy2, 1)
    game_world.add_objects(red_enemy, 1)
    game_world.add_objects(blue_enemy4, 1)
    game_world.add_objects(blue_enemy5, 1)
    game_world.add_objects(green_enemy2, 1)
    game_world.add_objects(middle_boss_enemy, 1)
    game_world.add_objects(blue_enemy3, 1)

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
    global handle_enemy_count, player_life_number, test_dead, test_dead_blue_enemy3, test_dead_boss, stage2_clear_wait_time
    for game_object in game_world.all_objects():
        game_object.update()

    for enemy in red_enemy:
        for bullet in bullet_list:
            if collide(enemy, bullet):
                red_enemy.remove(enemy)
                bullet_list.remove(bullet)
                game_world.remove_object(enemy)
                game_world.remove_object(bullet)
                death_red_enemy_stage2[enemy.count].dead_enemy = True
                death_red_enemy_stage2[enemy.count].explosion()
                main_state.stage1_score += 500
                handle_enemy_count += 1

    for enemy in blue_enemy4:
        for bullet in bullet_list:
            if collide(enemy, bullet):
                blue_enemy4.remove(enemy)
                bullet_list.remove(bullet)
                game_world.remove_object(enemy)
                game_world.remove_object(bullet)
                death_blue_enemy4_stage2[enemy.count].dead_enemy = True
                death_blue_enemy4_stage2[enemy.count].explosion()
                main_state.stage1_score += 500
                handle_enemy_count += 1

    for enemy in blue_enemy5:
        for bullet in bullet_list:
            if collide(enemy, bullet):
                blue_enemy5.remove(enemy)
                bullet_list.remove(bullet)
                game_world.remove_object(enemy)
                game_world.remove_object(bullet)
                death_blue_enemy5_stage2[enemy.count].dead_enemy = True
                death_blue_enemy5_stage2[enemy.count].explosion()
                main_state.stage1_score += 500
                handle_enemy_count += 1

    for enemy in green_enemy:
        for bullet in bullet_list:
            if collide(enemy, bullet):
                green_enemy.remove(enemy)
                bullet_list.remove(bullet)
                game_world.remove_object(enemy)
                game_world.remove_object(bullet)
                death_green_enemy_stage1[enemy.count].dead_enemy = True
                death_green_enemy_stage1[enemy.count].explosion()
                main_state.stage1_score += 500
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
                main_state.stage1_score += 500
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
                main_state.stage1_score += 500
                handle_enemy_count += 1


    for enemy in green_enemy2:
        for bullet in bullet_list:
            if collide(enemy, bullet):
                test_dead = Dead_effect(enemy.x, enemy.y)
                game_world.add_object(test_dead, 1)
                game_world.remove_object(enemy)
                game_world.remove_object(bullet)
                green_enemy2.remove(enemy)
                bullet_list.remove(bullet)
                handle_enemy_count += 1
                main_state.stage1_score += 1000





    for enemy in blue_enemy3:
        for bullet in bullet_list:
            if enemy != None:
                if collide(enemy, bullet):
                    test_dead_blue_enemy3 = Dead_effect(enemy.x, enemy.y)
                    game_world.add_object(test_dead_blue_enemy3, 1)
                    game_world.remove_object(enemy)
                    game_world.remove_object(bullet)
                    blue_enemy3.remove(enemy)
                    bullet_list.remove(bullet)
                    handle_enemy_count += 1
                    main_state.stage1_score += 1000
                    break

    for enemy in middle_boss_enemy:
        for bullet in bullet_list:
            if collide(enemy, bullet):
                test_dead_boss = Dead_effect(enemy.x, enemy.y)
                game_world.add_object(test_dead_boss, 1)
                game_world.remove_object(enemy)
                game_world.remove_object(bullet)
                middle_boss_enemy.remove(enemy)
                bullet_list.remove(bullet)
                handle_enemy_count += 1
                main_state.stage1_score += 1000


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

    if handle_enemy_count == 39:   # 39마리
        if stage2_clear_wait_time > 0.5:
            game_world.remove_object(plane)
            game_world.remove_object(background)
            game_world.remove_object(score_title)
            game_world.remove_object(player_life)
            game_world.remove_object(green_enemy)
            game_world.remove_object(blue_enemy)
            game_world.remove_object(blue_enemy2)
            game_world.remove_object(blue_enemy4)
            game_world.remove_object(blue_enemy5)
            game_world.remove_object(test_dead)
            game_world.remove_object(test_dead_boss)
            game_world.remove_object(test_dead_blue_enemy3)
            game_framework.push_state(stage_2_clear_state)
            stage2_clear_wait_time = 0
        delay(0.01)
        stage2_clear_wait_time += 0.01






def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()



    pass





