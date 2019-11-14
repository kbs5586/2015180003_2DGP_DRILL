from pico2d import *
import game_framework


class Brick:
    def __init__(self):
        self.image = load_image('brick180x40.png')
        self.x, self.y = 1600 // 2, 170
        self.speed = 450
        self.velocity = 1

    def update(self):
        self.x+=self.velocity
        if self.x < 0:
            self.velocity = 1
        elif self.x >= 1600:
            self.velocity = -1

    def draw(self):
        self.image.draw(self.x, self.y, 180, 40)
        draw_rectangle(*self.get_bb())

    # fill here
    def get_bb(self):
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20
