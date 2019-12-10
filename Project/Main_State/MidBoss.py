import game_framework
import Main_State.Item
import random
import Main_State.MidBossBullet
import game_framework

from pico2d import *


class CMidBoss:
    def __init__(self):
        self.Image = load_image('Resource//Boss0.png')
        self.Hp = 50000
        self.x, self.y = 400, 600
        self.ImgX, self.ImgY = 300, 300
        self.Speed = 1
        self.Type = 'MidBoss'
        self.time = 0.0
        self.Bullet_Lst = []
        self.BulletTime = 0.0
        self.Sound = load_wav('Sound//Death.wav')
        self.Sound.set_volume(3)
        pass

    def Update(self):
        self.y -= self.Speed
        if self.y <= 450:
            self.y = 450

        self.time += game_framework.frame_time
        if self.time < 10:
            self.Pattern0()
        elif self.time <= 20:
            self.Pattern1()
        else:
            self.Pattern2()
        if self.time >= 50:
            self.time = 0.0

        for i in self.Bullet_Lst:
            i.Update()
        pass

    def Render(self):
        self.Image.clip_draw(0, 0, self.ImgX, self.ImgY, self.x, self.y)
        for i in self.Bullet_Lst:
            i.Render()
        pass

    def Pattern0(self):
        self.BulletTime += game_framework.frame_time
        if self.BulletTime > 2.0:
            for i in range(6):
                MidBossBullet = Main_State.MidBossBullet.CMidBossBullet(self.x, self.y, 0, i)
                self.Bullet_Lst.append(MidBossBullet)
            self.BulletTime = 0.0
        pass

    def Pattern1(self):
        self.BulletTime += game_framework.frame_time
        if self.BulletTime > 2.0:
            for i in range(6):
                MidBossBullet = Main_State.MidBossBullet.CMidBossBullet(self.x, self.y, 1, i)
                self.Bullet_Lst.append(MidBossBullet)
            self.BulletTime = 0.0
        pass

    def Pattern2(self):
        self.BulletTime += game_framework.frame_time
        if self.BulletTime > 2.0:
            for i in range(8):
                MidBossBullet = Main_State.MidBossBullet.CMidBossBullet(self.x, self.y, 2, i)
                self.Bullet_Lst.append(MidBossBullet)
            self.BulletTime = 0.0
        pass

    def Drop(self, Unit_Lst):
        pass
