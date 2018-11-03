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


    def __init__(self, i):
        Blue_enemy2.image = load_image('Blue_enemy_clip2.png')
        self.x = 50+50 * i
        self.y = 400
        self.frame = 0
        self.total_frame = 0.0





    def update(self):

        pass


    def draw(self):
        self.image.clip_draw(self.frame * 50, 0, 50, 100, self.x, self.y)

        pass



