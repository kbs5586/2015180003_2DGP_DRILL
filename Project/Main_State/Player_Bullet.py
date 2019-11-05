import game_framework
from pico2d import *
import Main_State.Player
import Main_state


class CPlayer_Bullet:
    Image = None
    ImgX = None
    ImgY = None
    Speed = None
    Att = None

    def __init__(self, PosX, PosY, Player_Num):
        if CPlayer_Bullet.Image is None:
            if Player_Num == 0:
                CPlayer_Bullet.Image = load_image('Resource//Bullet_Ch0_0.png')
                CPlayer_Bullet.ImgX, CPlayer_Bullet.ImgY = 64, 64
                CPlayer_Bullet.Speed = 3
                CPlayer_Bullet.Att = 1
            if Player_Num == 1:
                CPlayer_Bullet.Image = load_image('Resource//Bullet_Ch1_0.png')
                CPlayer_Bullet.ImgX, CPlayer_Bullet.ImgY = 128, 128
                CPlayer_Bullet.Speed = 2
                CPlayer_Bullet.Att = 2
            if Player_Num == 2:
                CPlayer_Bullet.Image = load_image('Resource//Bullet_Ch2_0.png')
                CPlayer_Bullet.ImgX, CPlayer_Bullet.ImgY = 128, 128
                CPlayer_Bullet.Speed = 1
                CPlayer_Bullet.Att = 3
        self.x, self.y = PosX, PosY + 30

        pass

    def Chang_Bullet(self, Player_Bullet_Stack, Player_Num):
        if Player_Bullet_Stack >= 3:
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
        pass

    def Render(self):
        CPlayer_Bullet.Image.clip_draw(0, 0, CPlayer_Bullet.ImgX, CPlayer_Bullet.ImgY, self.x, self.y)
        pass

    def Collision(self, Unit_Lst):
        for i in Unit_Lst:
            if self.x - CPlayer_Bullet.ImgX/2 < i.x + i.ImgX / 2 \
                    and self.y + CPlayer_Bullet.ImgY/2 > i.y - i.ImgY / 2 \
                    and self.x + CPlayer_Bullet.ImgX/2 > i.x - i.ImgX / 2 \
                    and self.y - CPlayer_Bullet.ImgY/2 < i.y + i.ImgY / 2:
                i.Hp -= CPlayer_Bullet.Att
                if i.Hp <= 0:
                    i.Drop(Main_state.State_Lst)
                    del Unit_Lst[Unit_Lst.index(i)]

        pass
