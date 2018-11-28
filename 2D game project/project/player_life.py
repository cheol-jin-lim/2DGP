from pico2d import *

class Player_life:
    def __init__(self):
        self.image = load_image('images/player_life.png')
        self.frame = 1
        self.x = 50
        self.y = 570
        self.my_life = 1


    def update(self):
        pass

    def draw(self):
        if self.my_life == 1:
            self.image.clip_draw(0, 0, 50, 50, self.x, self.y)
        elif self.my_life == 0:
            self.my_life = None
