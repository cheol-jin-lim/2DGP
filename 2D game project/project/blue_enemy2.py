from pico2d import *


import game_world
import game_framework






class Blue_enemy2:
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

    image =None
    death_image = None


    def __init__(self, i):
        Blue_enemy2.image = load_image('Blue_enemy_clip2.png')
        self.death_image = load_image('dead.png')
        self.x = 50+50 * i
        self.y = 400
        self.frame = 0
        self.total_frame = 0.0
        self.death_total_frame = 0.0
        self.death_frame = 0
        self.death_blue_enemy2 = 0


    def get_bb(self):
        # fill here
        return self.x - 20, self.y - 20, self.x+20, self.y + 20




    def update(self):
        self.total_frame += Blue_enemy2.FRAMES_PER_ACTION * Blue_enemy2.ACTION_PER_TIME * game_framework.frame_time
        self.death_total_frame += Blue_enemy2.DEATH_FRAMES_PER_ACTION * Blue_enemy2.DEATH_ACTION_PER_TIME * game_framework. \
            frame_time
        self.frame = int(self.total_frame) % 2
        self.death_frame = int(self.death_total_frame) % 4

        pass


    def draw(self):
        if self.death_blue_enemy2 == 0:
            self.image.clip_draw(self.frame * 50, 0, 50, 100, self.x, self.y)
        elif self.death_blue_enemy2 == 1:
            self.death_image.clip_draw(self.death_frame * 70, 0, 70, 80, self.x, self.y)
            if self.death_frame == 3:
                self.death_blue_enemy2 = 3
        elif self.death_blue_enemy2 == 3:
            self.death_blue_enemy2 = 3
        draw_rectangle(*self.get_bb())





