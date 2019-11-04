import game_framework
from pico2d import *


class CCursor:
    Image = None

    def __init__(self):
        self.x, self.y = 400, 300
        self.MouseX, self.MouseY = 0, 0
        self.ImgX, self.ImgY = 47, 42
        if CCursor.Image is None:
            CCursor.Image = load_image('Resource//Cursor.png')
        pass

    def Mouse_Move(self, x, y):
        self.MouseX = x
        self.MouseY = y

    def Update(self):
        self.x=self.MouseX
        self.y=self.MouseY
        pass

    def Render(self):
        CCursor.Image.clip_draw(0, 0, self.ImgX, self.ImgY, self.x, self.y)
        pass
