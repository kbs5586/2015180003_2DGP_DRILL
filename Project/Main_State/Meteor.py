import game_framework
import random
import Main_state
from pico2d import *


class CMeteor:
    Image = None

    def __init__(self, xPos=1):
        if CMeteor.Image is None:
            CMeteor.Image = load_image('Resource//Meteor.png')
        self.x = xPos * 100
        self.y = 600
        self.Speed = 1
        self.Type = "Meteor"
        self.ImgX = 76
        self.ImgY = 120
        pass

    def Update(self):
        if Main_state.IsStage1_End:
            self.Speed=3
        self.y -= self.Speed
        pass

    def Render(self):
        CMeteor.Image.clip_draw(0, 0, self.ImgX, self.ImgY, self.x, self.y)
        pass

    def Collision(self, Unit):
        if self.x - self.ImgX / 2 < Unit.x + Unit.ImgX / 2 \
                and self.y + self.ImgY / 2 > Unit.y - Unit.ImgY / 2 \
                and self.x + self.ImgX / 2 > Unit.x - Unit.ImgX / 2 \
                and self.y - self.ImgY / 2 < Unit.y + Unit.ImgY / 2:
            del Unit
