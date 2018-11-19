from pico2d import *
import main_state
import stage1_clear_state

class Background:
    def __init__(self):
        self.image = load_image('backgroundmap.png')
        self.font = load_font('ENCR10B.TTF', 40)


    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 300)

        if stage1_clear_state.logo_time <= 0:
            self.font.draw(400, 540, ' %d ' % main_state.stage1_score, (255, 255, 255))