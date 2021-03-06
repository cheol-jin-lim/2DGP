import random
import math
import game_framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
from pico2d import *
import stage_state2
import death_green_enemy2

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 1


class Green_enemy2:
    DEATH_TIME_PER_ACTION = 1
    DEATH_ACTION_PER_TIME = 1.0 / DEATH_TIME_PER_ACTION
    DEATH_FRAMES_PER_ACTION = 4
    image = None
    death_image = None

    def load_image(self):
        if Green_enemy2.image == None:
            Green_enemy2.image = load_image('images/test_green_enemy2.png')


    def __init__(self, i):
        self.x, self.y = 450+ 50 * i, 500
        self.load_image()
        self.dir = random.random()*2*math.pi
        self.speed = 0
        self.timer = 1.0
        self.frame = 0
        self.build_behavior_tree()
        self.count = 0
        self.bgm = load_wav('sounds/enemy_accept_sound.wav')
        self.bgm.set_volume(32)


    def wander(self):
        self.speed = RUN_SPEED_PPS
        self.timer -= game_framework.frame_time
        if self.timer < 0:
            self.timer += 1.0
            self.dir = random.random() * 2 * math.pi

        return BehaviorTree.SUCCESS
        pass


    def find_player(self):
        plane = stage_state2.get_plane()
        distance = (plane.x - self.x)**2 + (plane.y - self.y) **2
        if distance < (PIXEL_PER_METER * 10)**2:
            self.dir = math.atan2(plane.y - self.y, plane.x - self.x)
            return BehaviorTree.SUCCESS
        else:
            self.speed = 0
            return BehaviorTree.FAIL
        pass


    def move_to_player(self):
        if self.count == 0:
            self.bgm.play()
        self.count += 1
        self.speed = RUN_SPEED_PPS
        return BehaviorTree.SUCCESS
        pass

    def build_behavior_tree(self):
        wander_node = LeafNode("Wander", self.wander)  # wander code


        find_player_node = LeafNode("Find Player", self.find_player)
        move_to_player_node = LeafNode("Move to Player", self.move_to_player)
        chase_node = SequenceNode("Chase")
        chase_node.add_children(find_player_node, move_to_player_node)
        wander_chase_node = SelectorNode("WanderChase")
        wander_chase_node.add_children(chase_node, wander_node)
        self.bt = BehaviorTree(wander_chase_node)
        pass


    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def update(self):
        self.bt.run()
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time

        if self.y < 350:
            self.x = clamp(50, self.x, 800 - 50)
            self.y = clamp(80, self.y, 500 - 50)
        else:
            self.x = clamp(300, self.x, 700 - 250)
            self.y = clamp(80, self.y, 500 - 50)

        pass


    def draw(self):
        self.image.draw(self.x, self.y)




    def handle_event(self, event):
        pass