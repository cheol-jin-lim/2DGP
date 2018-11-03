from pico2d import *


import game_world






class Blue_enemy:


    def __init__(self, i):
        Blue_enemy.image = load_image('Blue_enemy_clip.png')
        self.x = 50+50 * i
        self.y = 450
        self.frame = 0





    def update(self):
        self.frame = (self.frame + 1) % 2
        pass


    def draw(self):
        self.image.clip_draw(self.frame * 50, 0, 50, 100, self.x, self.y)

        pass



