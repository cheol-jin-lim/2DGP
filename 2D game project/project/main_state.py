import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state2


name = "MainState"

space = None
plane = None
life = None
score_title = None
font = None

green_enemy = None
blue_enemy = None
blue_enemy2 = None

green = None
blue = None
blue2 = None

class Space:
    def __init__(self):
        self.image = load_image('backgroundmap.png')

    def draw(self):
        self.image.draw(400, 300)

class Plane:
    #x = 0, y = 0
    def __init__(self):
        self.x, self.y = 400, 50
        self.image = load_image('player.png')
        self.dir = 0

    def update(self):
       self.x += self.dir
       # if self.x >= 800:
           # self.dir = -1
        #elif self.x <= 0:
            #self.dir = 1


    def draw(self):
        self.image.draw(self.x, self.y)


class Life:
    def __init__(self):
        self.image = load_image('life.png')

    def draw(self):
        self.image.draw(100,550)

class Score_title:
    def __init__(self):
        self.image = load_image('score.png')

    def draw(self):
        self.image.draw(400,580)


class Enemy1():
    def __init__(self, enemy1_x, enemy1_y):
        self.image = load_image('green_enemy_clip.png')
        self.frame = 0
        self.x, self.y = enemy1_x, enemy1_y



    # def update(self):
        #   self.frame = (self.frame + 1) % 7

    def draw(self):
        self.image.clip_draw(self.frame * 50, 0, 50, 100, self.x, self.y)



class Enemy2:
    def __init__(self, enemy2_x, enemy2_y):
        self.image = load_image('blue_enemy_clip.png')
        self.frame = 0
        self.x, self.y = enemy2_x, enemy2_y

    # def update(self):
       # self.y = self.y - 0.5
       # self.frame = (self.frame + 1) % 7

    def draw(self):
        self.image.clip_draw(self.frame * 50, 0, 50, 100, self.x, self.y)

class Enemy3:
    def __init__(self, enemy3_x, enemy3_y):
        self.image = load_image('blue_enemy_clip2.png')
        self.frame = 0
        self.x, self.y = enemy3_x, enemy3_y

    # def update(self):
       # self.y = self.y - 0.5
       # self.frame = (self.frame + 1) % 7

    def draw(self):
        self.image.clip_draw(self.frame * 50, 0, 50, 100, self.x, self.y)



class bullet:

    global plane
    bullet_y = 0

    def __init__(self):
        self.image = load_image('my_bullet.png')
        bullet_y = plane.y
    def update(self):

        pass

    def draw(self):
        self.image.draw(plane.x, plane.y)







def enter():
    global plane, space, life, score_title, green_enemy, blue_enemy, blue_enemy2
    global green, blue, blue2
    space = Space()
    plane = Plane()
    life = Life()




    green = [Enemy1(90 + 50 * i, 500) for i in range(13)]
    blue = [Enemy2(90 + 50 * i, 450) for i in range(13)]
    blue2 = [Enemy3(90 + 50 * i, 400) for i in range(13)]


    """green_enemy = Enemy1()
    blue_enemy = Enemy2()
    blue_enemy2 = Enemy3()"""
    score_title = Score_title()
    pass


def exit():
    global space, plane, life, score_title, green_enemy,blue_enemy, blue_enemy2
    global green, blue, blue2


    del(space)
    del(plane)
    del(life)
    del(score_title)
    del(green_enemy)
    del(blue_enemy)
    del(blue_enemy2)
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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state2)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            plane.dir = -10
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
            plane.dir = 0
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            plane.dir = 10
        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            plane.dir = 0



    pass

def update():
    global green_enemy,blue_enemy, blue_enemy2,green, blue, blue2
    plane.update()
    print(plane.x)
    # for green_enemy in green:
        # green_enemy.update()

    # for blue_enemy in blue:
        # blue_enemy.update()

    # for blue_enemy2 in blue2:
        # blue_enemy2.update()
    pass


def draw():
    global green_enemy, blue_enemy, blue_enemy2, green, blue, blue2
    clear_canvas()
    space.draw()
    life.draw()
    score_title.draw()
    plane.draw()
    for green_enemy in green:
        green_enemy.draw()

    for blue_enemy in blue:
       blue_enemy.draw()

    for blue_enemy2 in blue2:
        blue_enemy2.draw()
    update_canvas()
    handle_events()
    pass





