from pico2d import *

class Player_life:
    def __init__(self):
        self.image = load_image('player_life.png')
        self.frame = 1
        self.x = 50
        self.y = 570


    def update(self):
        # self.frame = (self.frame + 1) % 2
        pass

    def draw(self):
        self.image.draw(self.x, self.y) # clip_draw(self.frame * 50, 0, 50, 50, self.x, self.y)