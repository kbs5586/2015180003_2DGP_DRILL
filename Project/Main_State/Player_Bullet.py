import game_framework
from pico2d import *
import Main_State.Player
import Main_state
import random


class CPlayer_Bullet:
    Image = None
    ImgX = None
    ImgY = None
    Speed = None
    Att = None

    def __init__(self, PosX, PosY, Player_Num):
        self.PreNum =Player_Num
        self. PlayerNum=0
        if CPlayer_Bullet.Image is None:
            if Player_Num == 0:
                CPlayer_Bullet.Image = load_image('Resource//Bullet_Ch0_0.png')
                CPlayer_Bullet.ImgX, CPlayer_Bullet.ImgY = 64, 64
                CPlayer_Bullet.Speed = 3
                CPlayer_Bullet.Att = 1
                self.PlayerNum = Player_Num
            if Player_Num == 1:
                CPlayer_Bullet.Image = load_image('Resource//Bullet_Ch1_0.png')
                CPlayer_Bullet.ImgX, CPlayer_Bullet.ImgY = 128, 128
                CPlayer_Bullet.Speed = 2
                CPlayer_Bullet.Att = 2
                self.PlayerNum = Player_Num
            if Player_Num == 2:
                CPlayer_Bullet.Image = load_image('Resource//Bullet_Ch2_0.png')
                CPlayer_Bullet.ImgX, CPlayer_Bullet.ImgY = 128, 128
                CPlayer_Bullet.Speed = 1
                CPlayer_Bullet.Att = 3
                self.PlayerNum = Player_Num

        if self.PreNum != self.PlayerNum:
            if self.PreNum == 0:
                CPlayer_Bullet.Image = load_image('Resource//Bullet_Ch0_0.png')
                CPlayer_Bullet.ImgX, CPlayer_Bullet.ImgY = 64, 64
                CPlayer_Bullet.Speed = 3
                CPlayer_Bullet.Att = 1
                self.PlayerNum = Player_Num
            if self.PreNum == 1:
                CPlayer_Bullet.Image = load_image('Resource//Bullet_Ch1_0.png')
                CPlayer_Bullet.ImgX, CPlayer_Bullet.ImgY = 128, 128
                CPlayer_Bullet.Speed = 2
                CPlayer_Bullet.Att = 2
                self.PlayerNum = Player_Num
            if self.PreNum == 2:
                CPlayer_Bullet.Image = load_image('Resource//Bullet_Ch2_0.png')
                CPlayer_Bullet.ImgX, CPlayer_Bullet.ImgY = 128, 128
                CPlayer_Bullet.Speed = 1
                CPlayer_Bullet.Att = 3
                self.PlayerNum = Player_Num

        self.x, self.y = PosX, PosY + 30
        self.BulletSound=load_wav('Sound//PlayerAtt.wav')
        self.BulletSound.set_volume(1)
        pass

    def Change_Bullet(self, Player_Num):
        if Player_Num == 0:
            CPlayer_Bullet.Image = load_image('Resource//Bullet_Ch0_1.png')
            CPlayer_Bullet.ImgX = 64
            CPlayer_Bullet.ImgY = 128
            CPlayer_Bullet.Att = 2
        if Player_Num == 1:
            CPlayer_Bullet.Image = load_image('Resource//Bullet_Ch1_1.png')
            CPlayer_Bullet.ImgX = 96
            CPlayer_Bullet.ImgY = 127
            CPlayer_Bullet.Att = 4
        if Player_Num == 2:
            CPlayer_Bullet.Image = load_image('Resource//Bullet_Ch2_1.png')
            CPlayer_Bullet.ImgX = 89
            CPlayer_Bullet.ImgY = 89
            CPlayer_Bullet.Att = 6

    def Update(self):
        self.y += CPlayer_Bullet.Speed;
        self.BulletSound.play()
        pass

    def Render(self):
        CPlayer_Bullet.Image.clip_draw(0, 0, CPlayer_Bullet.ImgX, CPlayer_Bullet.ImgY, self.x, self.y)
        pass

    def Collision(self, Unit_Lst):
        for i in Unit_Lst:
            if self.x - CPlayer_Bullet.ImgX / 2 < i.x + i.ImgX / 2 \
                    and self.y + CPlayer_Bullet.ImgY / 2 > i.y - i.ImgY / 2 \
                    and self.x + CPlayer_Bullet.ImgX / 2 > i.x - i.ImgX / 2 \
                    and self.y - CPlayer_Bullet.ImgY / 2 < i.y + i.ImgY / 2:
                i.Sound.play()
                i.Hp -= CPlayer_Bullet.Att
                if i.Hp <= 0:

                    j = random.randint(0, 10)
                    if i.Type == "MidBoss":
                        Main_state.IsStage1_End =True
                        pass
                    if i.Type == "Boss":
                        Main_state.IsStage2_End = True
                    if j <= 4:
                        i.Drop(Main_state.State_Lst)
                    del Unit_Lst[Unit_Lst.index(i)]
        pass
