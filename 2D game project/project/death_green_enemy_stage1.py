from pico2d import *

import game_framework
import game_world
import main_state





class Death_green_enemy_stage1:



    TIME_PER_ACTION = 1.0
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 1

    DEATH_TIME_PER_ACTION = 1.0
    DEATH_ACTION_PER_TIME = 1.0 / DEATH_TIME_PER_ACTION
    DEATH_FRAMES_PER_ACTION = 4

    image = None



    def __init__(self, i):
        self.image = load_image('dead.png')
        self.dead_enemy = False
        self.dead_enemy2 = False
        self.x = 50+50 * i
        self.y = 500
        self.frame = 0
        self.total_frame = 0.0

        self.explosion_sound = load_wav('explosion_sound.wav')
        self.explosion_sound.set_volume(32)

    def explosion(self):
        self.explosion_sound.play()

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
    def set_poistion(self, x, y):
        self.x = x , self.y = y


    def update(self):
        if self.dead_enemy==True:
            self.total_frame += 15 * Death_green_enemy_stage1.FRAMES_PER_ACTION * Death_green_enemy_stage1.ACTION_PER_TIME * game_framework.frame_time
            self.frame = int(self.total_frame) % 4


        pass


    def draw(self):
        if self.dead_enemy==True:
            self.image.clip_draw(self.frame * 65, 0, 65 ,80, self.x, self.y)
            if self.frame == 3:
                self.dead_enemy = False












