import game_framework
from pico2d import *


class CNormal_Monster0:
    Image = None

    def __init__(self, xPos=1):
        if CNormal_Monster0.Image is None:
            CNormal_Monster0.Image = load_image('Resource//Monster0.png')
        self.Hp = 1
        self.x, self.y = xPos * 100, 600
        self.ImgX, self.ImgY = 116, 120
        self.Bullet_Lst = []
        self.Monster_Bullet_Time = 0.0
        self.Speed = 1
        self.Type = "Monster"
        pass

    def Update(self):
        self.y -= self.Speed

        if self.Monster_Bullet_Time > 1.0:
            self.Monster_Bullet_Time = 0.0
        self.Monster_Bullet_Time += 0.01

        pass

    def Render(self):
        CNormal_Monster0.Image.clip_draw(0, 0, self.ImgX, self.ImgY, self.x, self.y)
        pass

    def Drop(self):
        pass
