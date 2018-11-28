import final_stage_state

from pico2d import *

class Boss_hp_bar:
    def __init__(self):
        self.image = load_image('images/hp_bar.png')


    def update(self):
        pass

    def draw(self):
        if final_stage_state.final_boss.hp <= 50 and final_stage_state.final_boss.hp > 40:
            self.image.clip_draw(0, 150, 100, 50, 700, 550)
        if final_stage_state.final_boss.hp <= 40 and final_stage_state.final_boss.hp > 25 :
            self.image.clip_draw(0, 100, 100, 50, 700, 550)
        if final_stage_state.final_boss.hp <= 25 and final_stage_state.final_boss.hp > 10:
            self.image.clip_draw(0, 50, 100, 50, 700, 550)
        if final_stage_state.final_boss.hp <= 10 and final_stage_state.final_boss.hp > 0:
            self.image.clip_draw(0, 0, 100, 50, 700, 550)