from pico2d import *


import game_world






class Green_enemy:


    def __init__(self, i):
        Green_enemy.image = load_image('green_enemy_clip.png')
        self.x = 70+50 * i
        self.y = 500
        self.frame = 0





    def update(self):
        self.frame = (self.frame + 1) % 8
        pass


    def draw(self):
        self.image.clip_draw(self.frame * 50, 0, 50 ,100, self.x, self.y)

        pass



