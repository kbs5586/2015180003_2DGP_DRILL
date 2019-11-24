import game_framework
import random
from pico2d import *


class CItem:
    def __init__(self, kind=0, PosX=400, PosY=300):
        self.kind = kind
        self.ImgX, self.ImgY = 0, 0
        self.Image = None
        if self.kind == 0:
            if self.Image is None:
                self.Image = load_image('Resource//Item0.png')
                self.ImgX = 46
                self.ImgY = 46
        elif self.kind == 1:
            if self.Image is None:
                self.Image = load_image('Resource//Item1.png')
                self.ImgX = 130
                self.ImgY = 80
        elif self.kind == 2:
            if self.Image is None:
                self.Image = load_image('Resource//Item2.png')
                self.ImgX = 80
                self.ImgY = 80
        self.x, self.y = PosX, PosY
        self.DirX, self.DirY = random.randint(0, 1), random.randint(0, 1)
        if self.DirX == 0:
            self.DirX = -1
        else:
            self.DirX = 1
        if self.DirY == 0:
            self.DirY = -1
        else:
            self.DirY = 1
        self.Speed = 1
        self.Type = "Item"
        self.LifeTime = 5.0

    def Update(self):
        if self.x <= 0:
            self.DirX *= -1
            self.x += self.Speed * self.DirX
        elif self.x >= 800:
            self.DirX *= -1
            self.x += self.Speed * self.DirX
        elif self.y <= 0:
            self.DirY *= -1
            self.y += self.Speed * self.DirY
        elif self.y >= 600:
            self.DirY *= -1
            self.y += self.Speed * self.DirY
            pass
        else:
            self.x += self.Speed * self.DirX
            self.y += self.Speed * self.DirY
            pass

        if self.LifeTime > 1.0:
            # 삭제코드

            logo_time = 0
        self.LifeTime -= 0.01
        pass

    def Render(self):
        self.Image.clip_draw(0, 0, self.ImgX, self.ImgY, self.x, self.y)

    def Delete(self):
        pass
