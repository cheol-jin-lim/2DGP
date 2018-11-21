from pico2d import *

class Player_life:
    def __init__(self):
        self.image = load_image('player_life.png')
        self.frame = 1
        self.x = 50
        self.y = 570
        self.my_life = 2


    def update(self):
        # self.frame = (self.frame + 1) % 2
        pass

    def draw(self):
        if self.my_life == 2:
            self.image.clip_draw(0, 0, 100, 50, self.x, self.y)

        if self.my_life == 1:
            self.image.clip_draw(0, 0, 50, 50, self.x, self.y)