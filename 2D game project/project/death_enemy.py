"""from pico2d import *
import main_state
import stage1_clear_state
import green_enemy
import game_framework


image = None
class Death_enemy:
    DEATH_TIME_PER_ACTION = 1
    DEATH_ACTION_PER_TIME = 1.0 / DEATH_TIME_PER_ACTION
    DEATH_FRAMES_PER_ACTION = 4
    def __init__(self):
        self.image = load_image('dead.png')
        self.death_frame = 0
        self.death_total_frame = 0.0
        self.death_green = 0


    def update(self):
        self.death_total_frame += Death_enemy.DEATH_FRAMES_PER_ACTION * Death_enemy.DEATH_ACTION_PER_TIME * game_framework.frame_time
        self.death_frame = int(self.death_total_frame) % 4
        pass

    def draw(self):
        if self.death_green == 1:
            self.image.clip_draw(self.death_frame * 70, 0, 70, 80, main_state.enemy.x, green_enemy.y)"""


