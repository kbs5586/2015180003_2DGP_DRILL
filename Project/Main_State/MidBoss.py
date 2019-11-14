import game_framework
import Main_State.Item
import random

from pico2d import *


class CMidBoss:
    def __init__(self):
        self.Image = load_image('Resource//Boss0.png');
        self.Hp = 100000
        self.x, self.y = 400, 600
        self.ImgX, self.ImgY = 300, 300
        self.Speed = 1
        self.Type = 'MidBoss'
        pass

    def Update(self):
        self.y -= self.Speed
        if self.y <= 450:
            self.y = 450
        pass

    def Render(self):
        self.Image.clip_draw(0, 0, self.ImgX, self.ImgY, self.x, self.y)
        pass

    def Pattern0(self):
        pass

    def Pattern1(self):
        pass

    def Pattern2(self):
        pass
