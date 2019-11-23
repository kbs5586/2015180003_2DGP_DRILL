import game_framework
import Main_State.Item
import random
import Main_State.MidBossBullet
import game_framework

from pico2d import *


class CMidBoss:
    def __init__(self):
        self.Image = load_image('Resource//Boss0.png');
        self.Hp = 100000
        self.x, self.y = 400, 600
        self.ImgX, self.ImgY = 300, 300
        self.Speed = 1
        self.Type = 'MidBoss'
        self.time = 0.0
        self.BulletLst = []
        self.BulletTime = 0.0
        pass

    def Update(self):
        self.y -= self.Speed
        if self.y <= 450:
            self.y = 450

        self.time += game_framework.frame_time
        if self.time < 5:
            self.Pattern0()
        elif self.time <= 10:
            self.Pattern1()
        elif self.time <= 20:
            self.Pattern2()

        for i in self.BulletLst:
            i.Update()
        pass

    def Render(self):
        self.Image.clip_draw(0, 0, self.ImgX, self.ImgY, self.x, self.y)
        for i in self.BulletLst:
            i.Render()
        pass

    def Pattern0(self):
        self.BulletTime += game_framework.frame_time
        if self.BulletTime > 2.0:
            for i in range(6):
                MidBossBullet = Main_State.MidBossBullet.CMidBossBullet(self.x, self.y, 0, i)
                self.BulletLst.append(MidBossBullet)
            self.BulletTime = 0.0
        pass

    def Pattern1(self):
        self.BulletTime += game_framework.frame_time
        if self.BulletTime > 2.0:
            for i in range(6):
                MidBossBullet = Main_State.MidBossBullet.CMidBossBullet(self.x, self.y, 1, i)
                self.BulletLst.append(MidBossBullet)
            self.BulletTime = 0.0
        pass

    def Pattern2(self):
        self.BulletTime += game_framework.frame_time
        if self.BulletTime > 2.0:
            for i in range(8):
                MidBossBullet = Main_State.MidBossBullet.CMidBossBullet(self.x, self.y, 2, i)
                self.BulletLst.append(MidBossBullet)
            self.BulletTime = 0.0
        pass
