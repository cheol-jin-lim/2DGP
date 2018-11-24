import random
import json
import os
from pico2d import *
import game_framework
import game_world
import pause_state2
import game_over_state
import all_stage_clear_state
from background import Background
from score_title import Score_title
from my_bullet import My_bullet
from plane import *
from player_life import Player_life
from final_boss import Boss_enemy
import main_state
from boss_bullet import Boss_bullet
from boss_hp_bar import Boss_hp_bar
from death_final_boss_enemy import Dead_effect
from death_plane import Death_plane
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
boss_hp_bar = None
test_dead_boss = None
player_life_number = 1
boss_bullet_count = 0
death_plane_final_boss = None

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
    global background, score_title, player_life, plane, my_bullet, final_boss, boss_bullet, my_bullet,boss_hp_bar,death_plane_final_boss
    background = Background()
    score_title = Score_title()
    player_life = Player_life()
    plane = Plane()
    final_boss = Boss_enemy()
    boss_hp_bar = Boss_hp_bar()
    my_bullet = bullet_list
    boss_bullet = [Boss_bullet(i) for i in range(20)]
    game_world.add_object(background, 0)
    game_world.add_object(score_title, 1)
    game_world.add_object(player_life, 1)
    game_world.add_object(boss_hp_bar, 1)
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
            game_framework.push_state(pause_state2)
        else:
            plane.handle_event(event)

    if player_life_number == 0:
        game_framework.change_state(game_over_state)






    pass

def update():
    global boss_bullet_count, boss_bullet, final_boss, test_dead_boss
    for game_object in game_world.all_objects():
        game_object.update()

    for bullet in bullet_list:
        if collide(bullet, final_boss):
            game_world.remove_object(bullet)
            bullet_list.remove(bullet)
            if bullet == Skill_bullet():
                final_boss.hp -= 3
            final_boss.hp -= 1
            print(final_boss.hp)
            if final_boss.hp == 0:
                game_world.remove_object(final_boss)
                test_dead_boss = Dead_effect(final_boss.x, final_boss.y)
                game_world.add_object(test_dead_boss, 1)
                test_dead_boss.explosion()
                main_state.stage1_score += 10000

    for bullet in boss_bullet:
        if collide(bullet, plane):
            game_world.remove_object(plane)
            death_plane_final_boss = Death_plane(plane.x, plane.y)
            game_world.add_object(death_plane_final_boss, 1)
            death_plane_final_boss.dead_plane = True
            death_plane_final_boss.explosion()
            game_framework.change_state(game_over_state)

    if final_boss.hp == 0:
        game_framework.change_state(all_stage_clear_state)



















def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()



    pass





