import game_framework
import Select_state
from pico2d import *
import Main_State.Player_Bullet


class CPlayer:
    Image = None

    def __init__(self, Player_Num):
        if CPlayer.Image is None:
            CPlayer.Image = load_image('Resource//Player0.png')
        self.Player_Num = Player_Num
        self.x, self.y = 0, 0
        self.ImgX, self.ImgY = 155, 110
        self.Hp = 100
        self.MouseX, self.MouseY = 0, 0
        self.Bullet_Stack = 0
        self.Bullet_Time = 0.0
        self.Bullet_Lst = []
        self.Type = "Player"
        pass

    def Mouse_Move(self, x, y):
        self.MouseX = x
        self.MouseY = y
        pass

    def Update(self):
        self.x = self.MouseX
        self.y = self.MouseY

        if self.Bullet_Time > 1:
            Bullet = Main_State.Player_Bullet.CPlayer_Bullet(self.x, self.y, self.Player_Num)
            self.Bullet_Lst.append(Bullet)
            self.Bullet_Time = 0
        self.Bullet_Time += 0.01

        for i in self.Bullet_Lst:
            i.Update()
        pass

    def Render(self):
        CPlayer.Image.clip_draw(0, 0, self.ImgX, self.ImgY, self.x, self.y)
        for i in self.Bullet_Lst:
            i.Render()
        pass
