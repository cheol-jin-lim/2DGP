from pico2d import *

import game_framework
import game_world
import stage_state2







class Dead_effect:
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



    def __init__(self, x, y):
        self.image = load_image('dead.png')
        self.x = x
        self.y = y
        self.frame = 0
        self.total_frame = 0.0
        self.dead_enemy = False
        self.explosion_sound = load_wav('explosion_sound.wav')
        self.explosion_sound.set_volume(32)

    def explosion(self):
        self.explosion_sound.play()

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20


    def update(self):
        self.total_frame += 5 * Dead_effect.FRAMES_PER_ACTION * Dead_effect.ACTION_PER_TIME * game_framework.frame_time
        self.frame = int(self.total_frame) % 4


        pass


    def draw(self):
        if self.dead_enemy == False:
            self.image.clip_draw(self.frame * 65, 0, 65, 80, self.x, self.y)
        if self.frame == 3:
            self.dead_enemy = True









