from pico2d import *

import game_framework
import game_world






class Green_enemy:
    PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
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
    enemy = None

    def __init__(self, i):
        self.image = load_image('images/green_enemy_clip.png')
        self.x = 50+50 * i
        self.y = 500
        self.frame = 0
        self.total_frame = 0.0
        self.count = i

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20



    def setEnemy(self,enemy):
        self.enemy = enemy



    def update(self):
        self.total_frame += Green_enemy.FRAMES_PER_ACTION * Green_enemy.ACTION_PER_TIME * game_framework.frame_time
        self.frame = int(self.total_frame) % 2


        pass


    def draw(self):
        self.image.clip_draw(self.frame * 50, 0, 50, 100, self.x, self.y)











