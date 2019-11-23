import game_framework
from pico2d import *
import Main_State.Player
import Main_state
import random
import Main_State.MidBossBullet


class CMidBossBullet:
    Image = None

    def __init__(self, PosX, PosY, Pattern, Cnt):
        if CMidBossBullet.Image is None:
            CMidBossBullet.Image = load_image('Resource//MidBossBullet0.png');
        self.ImgX = 23
        self.ImgY = 23
        self.x = PosX
        self.y = PosY
        self.Speed = 0.0
        self.Pattern = Pattern
        self.Cnt = Cnt

        pass

    def Update(self):
        if self.Pattern == 0:
            pass
        elif self.Pattern == 1:
            pass
        elif self.Pattern == 2:
            pass
        pass

    def Render(self):
        CMidBossBullet.Image.clip_draw(0, 0, self.ImgX, self.ImgY, self.x, self.y)
        pass

    def Collision(self, Unit):
        pass
