import random
import math
import game_framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
from pico2d import *
import stage_state2

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 1


class Middle_boss_enemy:
    image = None

    def load_image(self):
        if Middle_boss_enemy.image == None:
            Middle_boss_enemy.image = load_image('middle_boss_enemy.png')

    def __init__(self, i):
        self.x, self.y = 400+50 * i, 500
        self.load_image()
        self.dir = random.random()*2*math.pi
        self.speed = 0
        self.timer = 1.0
        self.frame = 0
        self.build_behavior_tree()
        self.count = 0
        self.bgm = load_wav('enemy_accept_sound.wav')
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
        # fill here
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
        # fill here
        wander_node = LeafNode("Wander", self.wander)  # wander code
        # self.bt = BehaviorTree(wander_node)

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
        # fill here
        self.bt.run()

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time

        self.x = clamp(50, self.x, 700 - 50)
        self.y = clamp(80, self.y, 500 - 50)
        pass


    def draw(self):
        """if math.cos(self.dir) < 0:
            self.image.composite_draw(0, 'h', self.x, self.y)
        else:"""
        self.image.draw(self.x, self.y)

        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        pass