import game_framework
from pico2d import *
import time
import game_world

PIXEL_PER_METER = (10.0 / 0.4)
RUN_SPEED_KMPH = 40.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


class Bird:

    def __init__(self):
        self.x, self.y = 1600 // 2, 300
        self.image = load_image('bird_animation.png')
        # fill here
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = RUN_SPEED_PPS
        self.frameX = 0
        self.frameY = 0
        self.frameTime = 0
        self.current_time = time.time()

    def update(self):

        self.x += self.velocity * game_framework.frame_time
        if self.dir == 1:
            self.velocity = RUN_SPEED_PPS
            if self.x > 1480:
                self.dir = -1
        elif self.dir == -1:
            self.velocity = -RUN_SPEED_PPS
            if self.x <= 100:
                self.dir = 1

        self.frameTime += game_framework.frame_time
        if self.frameTime > 0.1:
            self.frameTime = 0
            self.frameX += 1

        if self.frameX == 5:
            self.frameX = 0
            self.frameY += 1
        if self.frameY == 3:
            self.frameY = 0

        pass

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frameX * 183, self.frameY * 168, 183, 168, self.x, self.y, 100, 100)

        if self.dir == -1:
            self.image.clip_composite_draw(self.frameX * 183, self.frameY * 168, 180, 166,
                                           0.0, 'h', self.x, self.y, 100, 100)

        pass
