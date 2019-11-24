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
        self.Angle = 0.0
        self.Pattern1Time = 0.0
        self.Pattern2Time = 0.0
        self.Type = "MidBossBullet"
        self.LifeTime = 0.0
        pass

    def Update(self):
        self.LifeTime += game_framework.frame_time
        if self.Pattern == 0:
            if self.Cnt == 0:
                self.x -= 2.5
            elif self.Cnt == 1:
                self.x -= 1.5
            elif self.Cnt == 2:
                self.x -= 0.5
            elif self.Cnt == 3:
                self.x += 0.5
            elif self.Cnt == 4:
                self.x += 1.5
            elif self.Cnt == 5:
                self.x += 2.5
            self.y -= 1

            pass
        elif self.Pattern == 1:
            self.Pattern1Time += game_framework.frame_time
            if self.Cnt % 2 == 0:
                self.x = self.x * math.cos(math.radians(self.Angle)) - self.y * math.sin(math.radians(self.Angle))
                self.y = self.x * math.sin(math.radians(self.Angle)) + self.y * math.cos(math.radians(self.Angle))
                self.Angle += 0.0001
            else:
                self.x = self.x * math.cos(math.radians(self.Angle)) - self.y * math.sin(math.radians(self.Angle))
                self.y = self.x * math.sin(math.radians(self.Angle)) + self.y * math.cos(math.radians(self.Angle))
                self.Angle -= 0.0001
            pass
        elif self.Pattern == 2:
            self.Pattern2Time += game_framework.frame_time
            if self.Pattern2Time <= 0.7:
                if self.Cnt == 0:
                    self.x -= 2.5
                elif self.Cnt == 1:
                    self.x -= 1.5
                elif self.Cnt == 2:
                    self.x -= 0.5
                elif self.Cnt == 3:
                    self.x -= 0.1
                elif self.Cnt == 4:
                    self.x += 0.1
                elif self.Cnt == 5:
                    self.x += 0.5
                elif self.Cnt == 6:
                    self.x += 1.5
                elif self.Cnt == 7:
                    self.x += 2.5
            else:
                self.y -= 1
            pass
        pass

    def Render(self):
        CMidBossBullet.Image.clip_draw(0, 0, self.ImgX, self.ImgY, self.x, self.y)
        pass

    def Collision(self, Unit):
        pass
