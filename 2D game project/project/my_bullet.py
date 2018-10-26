from pico2d import *
import game_world

class My_bullet:
    image = None # 클래스변수

    def __init__(self, x = 400, y = 300, velocity = 1):
        if My_bullet.image == None:
            My_bullet.image = load_image('my_bullet.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y += self.velocity * 5

        if self.y < 25 or self.y > 600 - 25:
            game_world.remove_object(self)