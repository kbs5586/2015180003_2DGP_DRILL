import game_framework
from pico2d import *
import Main_State.Player
import Main_state


class CBaby_Bullet:
    Image = None
    ImgX = 20
    ImgY = 44
    Att = 1

    def __init__(self, xPos, yPos):
        if CBaby_Bullet.Image is None:
            CBaby_Bullet.Image = load_image('Resource//BabyBullet0.png')
        self.x = xPos
        self.y = yPos
        self.Speed = 2

        pass

    def Update(self):
        self.y += self.Speed
        pass

    def Render(self):
        CBaby_Bullet.Image.clip_draw(0, 0, self.ImgX, self.ImgY, self.x, self.y)
        pass

    def Collision(self, Unit_Lst):
        for i in Unit_Lst:
            if self.x - CBaby_Bullet.ImgX / 2 < i.x + i.ImgX / 2 \
                    and self.y + CBaby_Bullet.ImgY / 2 > i.y - i.ImgY / 2 \
                    and self.x + CBaby_Bullet.ImgX / 2 > i.x - i.ImgX / 2 \
                    and self.y - CBaby_Bullet.ImgY / 2 < i.y + i.ImgY / 2:
                i.Hp -= CBaby_Bullet.Att
                if i.Hp <= 0:
                    del Unit_Lst[Unit_Lst.index(i)]
        pass
