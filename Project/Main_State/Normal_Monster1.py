import game_framework
import Main_State.Item
import random

from pico2d import *


class CNormal_Monster1:
    Image = None

    def __init__(self, xPos=1):
        if CNormal_Monster1.Image is None:
            CNormal_Monster1.Image = load_image('Resource//Monster1.png')
        self.Hp = 2000
        self.x, self.y = xPos * 100, 600
        self.ImgX, self.ImgY = 116, 120
        self.Bullet_Lst = []
        self.Monster_Bullet_Time = 0.0
        self.Speed = 1
        self.Type = "Monster"
        self.Sound = load_wav('Sound//Death.wav')
        self.Sound.set_volume(3)
        pass

    def Update(self):
        self.y -= self.Speed

        if self.Monster_Bullet_Time > 1.0:
            self.Monster_Bullet_Time = 0.0
        self.Monster_Bullet_Time += 0.01
        pass

    def Render(self):
        CNormal_Monster1.Image.clip_draw(0, 0, self.ImgX, self.ImgY, self.x, self.y)
        pass

    def Drop(self, Unit_Lst):
        Item_Lst = []

        tmp = random.randint(0, 2)
        print(tmp)
        if tmp == 0:
            Item = Main_State.Item.CItem(0, self.x, self.y)
        elif tmp == 1:
            Item = Main_State.Item.CItem(1, self.x, self.y)
        else:
            Item = Main_State.Item.CItem(2, self.x, self.y)
        Item_Lst.append(Item)
        Unit_Lst.append(Item_Lst)
        pass
