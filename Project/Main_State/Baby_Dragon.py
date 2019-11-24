import game_framework
import random
from pico2d import *


class CBaby_Dragon:

    def __init__(self, num):
        self.Image = load_image('Resource//Baby_Dragon.png')
        self.x = 400
        self.y = 300
        self.Bullet_Lst = []
        self.ImgX, self.ImgY = 39, 28
        self.Type = "Baby_Dragon"
        self.num = num
        pass

    def Update(self):
        pass

    def Render(self):
        self.Image.clip_draw(0, 0, self.ImgX, self.ImgY, self.x, self.y)
        pass

    def Compute_Player_Pos(self, Player):
        if self.num == 0:
            self.x = Player.x - 100
            self.y = Player.y
        else:
            self.x = Player.x + 100
            self.y = Player.y
        pass
