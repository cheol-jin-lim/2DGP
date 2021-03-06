from pico2d import *
from my_bullet import My_bullet
from my_bullet import Skill_bullet
import game_world
import game_framework
import main_state


RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP,BULLET_A,SKILL_S = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_a): BULLET_A,
    (SDL_KEYDOWN, SDLK_s): SKILL_S
}
PIXEL_PER_METER = (10.0/ 0.3) # 10PIXEL 30CM
RUN_SPEED_KMPH = 20.0 # KM / HOUR
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAME_PER_ACTION = 8


bullet_list = []
skill_bullet_list = []
class Runstate:

    @staticmethod
    def enter(plane, event):
        if event == RIGHT_DOWN:
            plane.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            plane.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            plane.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            plane.velocity += RUN_SPEED_PPS

    @staticmethod
    def exit(plane, event):
        if event == BULLET_A:
            plane.fire_bullet()
            plane.bullet_count += 1

        if plane.bullet_count == 20:
            plane.skill_bullet_count += 1
            plane.bullet_count = 0





        if (event == SKILL_S) and (plane.skill_bullet_count) > 0:
            plane.fire_skill_bullet()
            plane.skill_bullet_count -= 1

            pass

    @staticmethod
    def do(plane):
        plane.x += plane.velocity * game_framework.frame_time
        plane.x = clamp(25, plane.x, 800 - 25)

    @staticmethod
    def draw(plane):
        if plane.velocity == 1:
            plane.image.draw(plane.x, plane.y)
        else:
            plane.image.draw(plane.x, plane.y)


next_state_table = {
    Runstate: {RIGHT_UP: Runstate, LEFT_UP: Runstate, LEFT_DOWN: Runstate, RIGHT_DOWN: Runstate, BULLET_A: Runstate, SKILL_S: Runstate}

}


class Plane:

    def __init__(self):
        self.x, self.y =  400, 60
        self.image = load_image('images/player.png')
        self.dir = 1
        self.velocity = 0
        self.event_que = []
        self.cur_state = Runstate
        self.cur_state.enter(self, None)
        self.bullet_count = 0
        self.skill_bullet_count = 0
        self.font = load_font('ENCR10B.TTF', 16)

        self.shoot_sound = load_wav('sounds/player_shoot_sound.wav')
        self.shoot_sound.set_volume(32)

        self.skill_shoot_sound = load_wav('sounds/skill_bullet_sound.wav')
        self.skill_shoot_sound.set_volume(64)

    def shoot(self):
        self.shoot_sound.play()

    def skill_shoot(self):
        self.skill_shoot_sound.play()

    def fire_bullet(self):
        my_bullet =My_bullet(self.x, self.y, self.dir * 3)
        game_world.add_object(my_bullet, 1)
        bullet_list.append(my_bullet)
        Plane.shoot(self)

    def fire_skill_bullet(self):
        skill_bullet = Skill_bullet(self.x, self.y, self.dir * 3)
        game_world.add_object(skill_bullet, 1)
        skill_bullet_list.append(skill_bullet)
        Plane.skill_shoot(self)
        pass

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20





    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(620, 20,'[basic bullet: %d]' % self.bullet_count,(100, 255, 0))
        self.font.draw(620, 40, '[Skill bullet: %d]' % self.skill_bullet_count, (100, 255, 0))



    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)