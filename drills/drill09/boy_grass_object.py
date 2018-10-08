from pico2d import *
import random


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)

class Smallball:
    def __init__(self):
        self.speed = random.randint(5, 15)
        self.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(100, 700), 500

    def update(self):
        self.y = self.y - self.speed
        if self.y <= 50:
            self.speed = 0

    def draw(self):
        self.image.draw(self.x, self.y)


class Bigball:
    def __init__(self):
        self.speed = random.randint(1, 10)
        self.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(100, 700), 500


    def update(self):
        self.y = self.y - self.speed
        if self.y <= 50:
            self.speed = 0

    def draw(self):
        self.image.draw(self.x, self.y)





class Boy:
    def __init__(self):
        self.x, self.y =random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x = self.x + 1

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()


grass = Grass()


team = [Boy() for i in range(11)]
running = True
n = random.randint(1,15)
ball_1 = [Bigball() for i in range(n)]
ball_2 = [Smallball() for i in range(20- n)]

while running:
    handle_events()

    for boy in team:
        boy.update()
    for bigball in ball_1:
        bigball.update()
    for Smallball in ball_2:
        Smallball.update()
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for bigball in ball_1:
        bigball.draw()
    for Smallball in ball_2:
        Smallball.draw()
    update_canvas()

    delay(0.05)

close_canvas()