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


class Skill_bullet:
    image = None # 클래스변수

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Skill_bullet.image == None:
            Skill_bullet.image = load_image('skill_bullet.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.frame = 1

    def draw(self):
        self.image.draw(self.x, self.y) # (self.frame * 27, 0, 400, 75, self.x ,self.y)

    def update(self):
        self.y += self.velocity * 5
        # self.frame = (self.frame + 1 ) % 11

        if self.y < 25 or self.y > 600 - 25:
            game_world.remove_object(self)



