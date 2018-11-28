from pico2d import *
import main_state
import stage1_clear_state
import stage_state2


class Background:
    def __init__(self):
        self.image = load_image('images/backgroundmap.png')
        self.font = load_font('ENCR10B.TTF', 40)
        self.bgm = load_wav('sounds/start_intro.wav')
        self.bgm.set_volume(64)
        self.bgm.play()




    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 300)
        self.font.draw(400, 540, ' %d ' % main_state.stage1_score, (255, 255, 255))