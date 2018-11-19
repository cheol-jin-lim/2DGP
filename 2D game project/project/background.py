from pico2d import *
import main_state

class Background:
    def __init__(self):
        self.image = load_image('backgroundmap.png')
        self.font = load_font('ENCR10B.TTF', 40)


    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 300)

        if main_state.handle_enemy_count != 42:
            self.font.draw(400, 540, ' %d ' % main_state.stage1_score, (255, 255, 255))