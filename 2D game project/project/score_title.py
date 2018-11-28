

from pico2d import *

class Score_title:
    def __init__(self):
        self.image = load_image('images/score.png')


    def update(self):
        pass

    def draw(self):
        self.image.draw(400,570)