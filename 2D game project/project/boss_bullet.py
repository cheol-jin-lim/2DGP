from pico2d import *
import game_world
import game_framework
import final_boss
import random
import final_stage_state
class Boss_bullet:
    image = None # 클래스변수

    def __init__(self, i):
        if Boss_bullet.image == None:
            Boss_bullet.image = load_image('boss_bullet.png')
        self.x = 50 + 40 * i
        self.y = 500
        self.velocity = random.randint(1, 5)



    def get_bb(self):
        return self.x-7, self.y -20, self.x+7, self.y + 20

    def collide_sound(self):
        pass




    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.velocity
        self.x = clamp(50, self.x, 800 - 50)
        self.y = clamp(10, self.y, 600 - 50)
        if self.y < 25 or self.y > 600 - 25:
            final_stage_state.boss_bullet_count += 1

            game_world.remove_object(self)
            if final_stage_state.boss_bullet_count == 20:
                final_stage_state.boss_bullet.clear()
                final_stage_state.boss_bullet = [Boss_bullet(i) for i in range(20)]
                game_world.add_objects(final_stage_state.boss_bullet, 1)
                final_stage_state.boss_bullet_count = 0







