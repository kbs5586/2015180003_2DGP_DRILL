import game_framework
import Select_state
from pico2d import *
import Main_State.Player_Bullet
import Main_State.Baby_Dragon


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
        self.Bullet_Stack_Num = 0
        self.Bullet_Stack_Shape = 0
        self.Bullet_Stack_Speed = 0
        self.Bullet_Time = 0.0
        self.Bullet_Lst = []
        self.Type = "Player"
        self.BulletSpeed = 0.1
        self.IsCheck_Bullet_Stack_Shape = False
        self.Baby_Dragon0 = Main_State.Baby_Dragon.CBaby_Dragon(0)
        self.Baby_Dragon1 = Main_State.Baby_Dragon.CBaby_Dragon(1)
        self.font = load_font('ENCR10B.TTF', 50)

        self.Game_time = 0.0
        pass

    def Mouse_Move(self, x, y):
        self.MouseX = x
        self.MouseY = y
        pass

    def Update(self):
        self.x = self.MouseX
        self.y = self.MouseY
        self.Bullet_Time += game_framework.frame_time
        self.Game_time += game_framework.frame_time
        if self.BulletSpeed <= 0.2:
            self.BulletSpeed = 0.2
        if self.Bullet_Time > self.BulletSpeed:
            if self.Bullet_Stack_Num >= 10:
                Bullet = Main_State.Player_Bullet.CPlayer_Bullet(self.x - 10, self.y, self.Player_Num)
                self.Bullet_Lst.append(Bullet)
                Bullet = Main_State.Player_Bullet.CPlayer_Bullet(self.x + 10, self.y, self.Player_Num)
                self.Bullet_Lst.append(Bullet)
            else:
                Bullet = Main_State.Player_Bullet.CPlayer_Bullet(self.x, self.y, self.Player_Num)
                self.Bullet_Lst.append(Bullet)
            self.Bullet_Time = 0

        for i in self.Bullet_Lst:
            i.Update()
            if not self.IsCheck_Bullet_Stack_Shape:
                if self.Bullet_Stack_Shape >= 3:
                    i.Change_Bullet(self.Player_Num)
                    self.IsCheck_Bullet_Stack_Shape = True

        self.Baby_Dragon0.Update()
        self.Baby_Dragon0.Compute_Player_Pos(self)

        self.Baby_Dragon1.Update()
        self.Baby_Dragon1.Compute_Player_Pos(self)
        pass

    def Render(self):
        CPlayer.Image.clip_draw(0, 0, self.ImgX, self.ImgY, self.x, self.y)
        for i in self.Bullet_Lst:
            i.Render()
        self.font.draw(700, 300, '%d' % self.Game_time, (255, 255, 255))
        self.Baby_Dragon0.Render()
        self.Baby_Dragon1.Render()
        pass

    def Change_Player(self, num):
        self.Player_Num=num

        pass

    def Collision(self, Unit_Lst):
        for i in Unit_Lst:
            if self.x - self.ImgX / 2 < i.x + i.ImgX / 2 \
                    and self.y + self.ImgY / 2 > i.y - i.ImgY / 2 \
                    and self.x + self.ImgX / 2 > i.x - i.ImgX / 2 \
                    and self.y - self.ImgY / 2 < i.y + i.ImgY / 2:
                if i.kind == 0:
                    self.Bullet_Stack_Num += 2
                    pass
                elif i.kind == 1:
                    self.Bullet_Stack_Shape += 2
                    pass
                elif i.kind == 2:
                    self.Bullet_Stack_Speed += 2
                    if self.Bullet_Stack_Speed >= 2:
                        self.Bullet_Stack_Speed = 0
                        self.BulletSpeed -= 0.3
                del Unit_Lst[Unit_Lst.index(i)]
                pass
        pass
