from pico2d import *
import game_world
import game_framework

class My_bullet:
    image = None # 클래스변수

    def __init__(self, x = 400, y = 300, velocity = 1):
        if My_bullet.image == None:
            My_bullet.image = load_image('images/my_bullet.png')
        self.x, self.y, self.velocity = x, y, velocity

        self.collide_sound = load_wav('sounds/pickup.wav')
        self.collide_sound.set_volume(32)



    def get_bb(self):
        return self.x-7, self.y -20, self.x+7, self.y + 20

    def collide_sound(self):
        self.collide_sound.play()




    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y += self.velocity * 5


        if self.y < 25 or self.y > 600 - 25:
            game_world.remove_object(self)


class Skill_bullet:
    image = None # 클래스변수

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Skill_bullet.image == None:
            Skill_bullet.image = load_image('images/skill_bullet.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.frame = 1

    def get_bb(self):
        return self.x-60, self.y -110, self.x+60, self.y + 110

    def draw(self):
        self.image.draw(self.x, self.y)


    def update(self):
        self.y += self.velocity * 5

        if self.y < 25 or self.y > 600 - 25:
            game_world.remove_object(self)



