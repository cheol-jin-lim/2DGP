from pico2d import *
import random

import game_world
import game_framework





class Boss_enemy:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 1
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 1

    DEATH_TIME_PER_ACTION = 1
    DEATH_ACTION_PER_TIME = 1.0 / DEATH_TIME_PER_ACTION
    DEATH_FRAMES_PER_ACTION = 4


    image = None
    death_image = None


    def __init__(self):
        Boss_enemy.image = load_image('final_boss_enemy.png')
        self.death_image = load_image('dead.png')
        self.x = random.randint(200, 600)
        self.y = random.randint(200, 500)
        self.frame = 0
        self.total_frame = 0.0
        self.death_frame = 0
        self.death_total_frame = 0.0
        self.death_boss_enemy = 0

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20





    def update(self):
        self.total_frame += Boss_enemy.FRAMES_PER_ACTION * Boss_enemy.ACTION_PER_TIME * game_framework.frame_time
        self.frame = int(self.total_frame) % 2
        self.death_total_frame += Boss_enemy.DEATH_FRAMES_PER_ACTION * Boss_enemy.DEATH_ACTION_PER_TIME * game_framework.\
            frame_time
        self.death_frame = int(self.death_total_frame) % 4

        pass


    def draw(self):
        if self.death_boss_enemy == 0:
            self.image.draw(self.x, self.y)# self.image.clip_draw(self.frame * 50, 0, 50, 100, self.x, self.y)

        """elif self.death_boss_enemy == 1:
            self.death_image.clip_draw(self.death_frame * 70, 0, 70, 80, self.x, self.y)
            if self.death_frame == 3:
                self.death_boss_enemy = 3

        elif self.death_boss_enemy == 3:
            self.death_boss_enemy = 3"""
        draw_rectangle(*self.get_bb())





