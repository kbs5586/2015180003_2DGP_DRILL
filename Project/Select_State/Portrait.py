import game_framework
from pico2d import *


class CPortrait:
    def __init__(self, charNum):
        self.x, self.y = 0, 0
        self.ImgX, self.ImgY = 266, 600
        self.charNum=charNum
        if self.charNum == 0:
            self.Image = load_image('Resource//Char0.png')
            pass
        if self.charNum == 1:
            self.Image = load_image('Resource//Char1.png')
            pass
        if self.charNum == 2:
            self.Image = load_image('Resource//Char2.png')
            pass
        pass

    def Update(self):
        pass

    def Render(self):
        if self.charNum == 0:
            self.Image.clip_draw(0, 0, self.ImgX, self.ImgY, 133, 300)
            pass
        if self.charNum == 1:
            self.Image.clip_draw(0, 0, self.ImgX, self.ImgY, 400, 300)
            pass
        if self.charNum == 2:
            self.Image.clip_draw(0, 0, self.ImgX, self.ImgY, 666, 300)
            pass
        pass
