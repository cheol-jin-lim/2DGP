from pico2d import *

import game_framework
import game_world
import main_state





class Death_plane:



    TIME_PER_ACTION = 1.0
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 1

    DEATH_TIME_PER_ACTION = 1.0
    DEATH_ACTION_PER_TIME = 1.0 / DEATH_TIME_PER_ACTION
    DEATH_FRAMES_PER_ACTION = 4

    image = None



    def __init__(self, x, y):
        self.image = load_image('images/test_plane_explosion.png')
        self.dead_plane = False
        self.x = x
        self.y = y
        self.frame = 0
        self.total_frame = 0.0

        self.explosion_sound = load_wav('sounds/explosion_sound.wav')
        self.explosion_sound.set_volume(32)

    def explosion(self):
        self.explosion_sound.play()

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20


    def update(self):
        if self.dead_plane==True:
            self.total_frame += 10 * Death_plane.FRAMES_PER_ACTION * Death_plane.ACTION_PER_TIME * game_framework.frame_time
            self.frame = int(self.total_frame) % 4


        pass


    def draw(self):
        if self.dead_plane==True:
            self.image.clip_draw(self.frame * 80, 0, 80 ,100, self.x, self.y)
            if self.frame == 3:
                self.dead_plane = False












