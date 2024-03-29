import random
from pico2d import *
import game_world
import game_framework


class Ball:
    image = None

    def __init__(self):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1280 - 1),random.randint(0, 1024 - 1), 0

    def get_bb(self):
        # fill here
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time

    # fill here for def stop
    def stop(self):
        self.fall_speed = 0

