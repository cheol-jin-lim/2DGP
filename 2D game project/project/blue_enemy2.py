from pico2d import *


import game_world






class Blue_enemy2:


    def __init__(self, i):
        Blue_enemy2.image = load_image('Blue_enemy_clip2.png')
        self.x = 70+50 * i
        self.y = 400
        self.frame = 0





    def update(self):
        self.frame = (self.frame + 1) % 8
        pass


    def draw(self):
        self.image.clip_draw(self.frame * 50, 0, 50, 100, self.x, self.y)

        pass



