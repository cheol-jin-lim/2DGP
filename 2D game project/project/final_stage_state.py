import random
import json
import os
from pico2d import *
import game_framework
import game_world
import game_over_state
from background import Background
from score_title import Score_title
from my_bullet import My_bullet
from plane import *
from player_life import Player_life
from final_boss import Boss_enemy
import main_state
from boss_bullet import Boss_bullet
name = "final_stage_state"


background = None
score_title = None
player_life = None
plane = None
my_bullet = None
font = None
skill_bullet = None
final_boss = None
boss_bullet = None

player_life_number = 1
boss_bullet_count = 0


handle_enemy_count = 0
# i = random.randint(20, 70)


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
    global background, score_title, player_life, plane, my_bullet, final_boss, boss_bullet, my_bullet
    background = Background()
    score_title = Score_title()
    player_life = Player_life()
    plane = Plane()
    final_boss = Boss_enemy()
    my_bullet = bullet_list
    boss_bullet = [Boss_bullet(i) for i in range(20)]
    game_world.add_object(background, 0)
    game_world.add_object(score_title, 1)
    game_world.add_object(player_life, 1)
    game_world.add_object(plane, 1)
    game_world.add_object(final_boss, 1)
    game_world.add_objects(boss_bullet, 1)


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
    global boss_bullet_count, boss_bullet, final_boss
    for game_object in game_world.all_objects():
        game_object.update()

    for bullet in bullet_list:
        if collide(bullet, final_boss):
            game_world.remove_object(bullet)
            bullet_list.remove(bullet)
            final_boss.hp -= 1
            print(final_boss.hp)
            if final_boss.hp == 0:
                game_world.remove_object(final_boss)


    








def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()



    pass





