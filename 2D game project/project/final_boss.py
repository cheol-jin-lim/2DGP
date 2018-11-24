from pico2d import *
import random
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
import game_world
import game_framework
import final_stage_state
from boss_bullet import *
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

boss_bullet = None


class Boss_enemy:

    TIME_PER_ACTION = 1
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 1

    image = None
    death_image = None


    def __init__(self):
        Boss_enemy.image = load_image('final_boss_enemy.png')
        self.death_image = load_image('dead.png')
        self.x = random.randint(200, 600)
        self.y = random.randint(200, 500)
        self.frame = 0
        self.timer = 1.0
        self.total_frame = 0.0
        self.build_behavior_tree()
        self.death_frame = 0
        self.death_total_frame = 0.0
        self.death_boss_enemy = 0
        self.speed = 0
        self.dir = random.random() * 2 * math.pi
        self.hp = 50

    def get_bb(self):
        return self.x - 140, self.y - 50, self.x + 140, self.y + 50

    def wander(self):
        self.speed = RUN_SPEED_PPS
        self.timer -= game_framework.frame_time
        if self.timer < 0:
            self.timer += 1.0
            self.dir = random.random() * 2 * math.pi

        return BehaviorTree.SUCCESS
        pass

    def find_player(self):
        plane = final_stage_state.get_plane()
        distance = (plane.x - self.x) ** 2 + (plane.y - self.y) ** 2
        if distance < (PIXEL_PER_METER * 10) ** 2:
            self.dir = math.atan2(plane.y - self.y, plane.x - self.x)
            return BehaviorTree.SUCCESS
        else:
            self.speed = 0
            return BehaviorTree.FAIL
        pass

    def move_to_player(self):
        self.speed = RUN_SPEED_PPS
        return BehaviorTree.SUCCESS
        pass

    def shoot_bullet(self):
        pass





    def build_behavior_tree(self):
        wander_node = LeafNode("Wander", self.wander)  # wander code
        # self.bt = BehaviorTree(wander_node)

        find_player_node = LeafNode("Find Player", self.find_player)
        # move_to_player_node = LeafNode("Move to Player", self.move_to_player)
        chase_node = SequenceNode("Chase")
        shoot_bullet_node =LeafNode("shoot bullet", self.shoot_bullet)
        # chase_node.add_children(shoot_bullet_node) # chase_node에 미사일 발사 추가하기
        wander_chase_node = SelectorNode("WanderChase")
        wander_chase_node.add_children(wander_node)
        self.bt = BehaviorTree(wander_chase_node)
        pass





    def update(self):
        self.bt.run()
        self.total_frame += Boss_enemy.FRAMES_PER_ACTION * Boss_enemy.ACTION_PER_TIME * game_framework.frame_time
        self.frame = int(self.total_frame) % 2
        self.speed = RUN_SPEED_PPS

        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time

        self.x = clamp(100, self.x, 700 - 50)
        self.y = clamp(200, self.y, 500 - 50)


        pass


    def draw(self):
        if self.death_boss_enemy == 0:
            self.image.draw(self.x, self.y)# self.image.clip_draw(self.frame * 50, 0, 50, 100, self.x, self.y)
        draw_rectangle(*self.get_bb())





