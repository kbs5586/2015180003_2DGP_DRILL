import game_framework
import random
import Main_State.BabyBullet
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
        self.Bullet_Lst = []
        self.Bullet_Time = 0.0
        pass

    def Update(self):
        self.Bullet_Time += game_framework.frame_time
        if self.Bullet_Time > 3.0:
            Bullet = Main_State.BabyBullet.CBaby_Bullet(self.x, self.y)
            self.Bullet_Lst.append(Bullet)
            self.Bullet_Time = 0.0
        for i in self.Bullet_Lst:
            i.Update()

    def Render(self):
        self.Image.clip_draw(0, 0, self.ImgX, self.ImgY, self.x, self.y)
        for i in self.Bullet_Lst:
            i.Render()
        pass

    def Compute_Player_Pos(self, Player):
        if self.num == 0:
            self.x = Player.x - 100
            self.y = Player.y
        else:
            self.x = Player.x + 100
            self.y = Player.y
        pass
