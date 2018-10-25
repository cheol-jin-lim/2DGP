from pico2d import *

class Player_life:
    def __init__(self):
        self.image = load_image('life.png')


    def update(self):
        pass

    def draw(self):
        self.image.draw(50,570)