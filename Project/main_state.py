import random
import json
import os
import random
import Select_state

from pico2d import *

import game_framework

logo_time = 0.0
Monster_time = 0.0
Total_time = 0.0

name = "MainState"
x, y = 0, 0
Player = None
Bullet_Lst = []
Monster_Lst = []
Back_Ground_Img = None

Item = None


class CPlayer:
    def __init__(self):
        self.x, self.y = x, y
        self.Bullet_Stack = 0
        if Select_state.CharNum == 1:
            self.image = load_image('Player0.png')
        elif Select_state.CharNum == 2:
            self.image = load_image('Player1.png')
        elif Select_state.CharNum == 3:
            self.image = load_image('Player2.png')

    def Update(self):
        global x, y
        global logo_time
        global Bullet_Lst
        if logo_time > 0.1:
            Bullet = CBullet()
            Bullet_Lst.append(Bullet)
            logo_time = 0
        delay(0.01)
        logo_time += 0.01
        self.x, self.y = x, y

    def Draw(self):
        global Bullet_Lst
        self.image.clip_draw(0, 0, 155, 110, self.x, self.y)


class CBullet:
    global Player
    global Monster_Lst
    global Bullet_Lst
    image = None

    def __init__(self):
        self.x, self.y = Player.x, Player.y + 30
        self.lifeTime = 0
        if Player is not None:
            if Select_state.CharNum == 1:
                if Player.Bullet_Stack == 0:
                    if CBullet.image is None:
                        CBullet.image = load_image('Bullet_Ch0_0.png')
                elif Player.Bullet_Stack == 1:
                    if CBullet.image is None:
                        CBullet.image = load_image('Bullet_Ch0_1.png')

    def Update(self):
        self.y += 30

    def Draw(self):
        CBullet.image.clip_draw(0, 0, 64, 64, self.x, self.y)

    def Collision(self, Unit):
        for i in Unit:
            if self.x - 34 < i.x + i.ImgX/2 \
                    and self.y + 34 > i.y - i.ImgY/2 \
                    and self.x + 34 > i.x - i.ImgX/2 \
                    and self.y - 34 < i.y + i.ImgY/2:
                del Unit[Unit.index(i)]
                return True


class CItem:
    image = None

    def __init__(self, xPos=400):
        self.x = xPos
        self.y = 600
        if CItem.image is None:
            CItem.image = load_image('Item0.png')

    def Update(self):
        self.y -= 6
        pass

    def Draw(self):
        CItem.image.clip_draw(0, 0, 46, 46, self.x, self.y)
        pass


class CMonster:
    def __init__(self, xPos=400):
        self.x = xPos * 100
        self.y = 600
        self.image = load_image('Monster0.png')
        self.ImgX = 116
        self.ImgY = 120

    def Update(self):
        self.y -= 1
        pass

    def Draw(self):
        self.image.clip_draw(0, 0, self.ImgX, self.ImgY, self.x, self.y)


def enter():
    global Player, Item
    global Back_Ground_Img
    Back_Ground_Img = load_image('BackGround.png')
    Player = CPlayer()
    Item = CItem()
    pass


def exit():
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    global Player, x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 600 - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            pass


def update():
    global Monster_time, Total_time
    global Monster_Lst, Bullet_Lst

    if Monster_time > 1.0:
        Monster_lineLst = []
        for i in range(6):
            Monster_lineLst.append(random.randint(1, 7))
        for i in Monster_lineLst:
            Monster = CMonster(int(i))
            Monster_Lst.append(Monster)
        Monster_time = 0
    delay(0.01)

    Monster_time += 0.01
    Total_time += 0.01
    if Total_time >= 30:
        i = 0

    for j in Bullet_Lst:
        if j.Collision(Monster_Lst):
            del Bullet_Lst[Bullet_Lst.index(j)]


def draw():
    global Back_Ground_Img
    global Player, Item
    global Monster_Lst
    global Bullet_Lst
    clear_canvas()
    Back_Ground_Img.draw(400, 300)

    if Player is not None:
        Player.Update()
        Player.Draw()
    if Monster_Lst is not None:
        for i in Monster_Lst:
            i.Update()
            i.Draw()
            if i.y <= 0:
                del Monster_Lst[Monster_Lst.index(i)]
    if Bullet_Lst is not None:
        for i in Bullet_Lst:
            i.Update()
            i.Draw()
            if i.y >= 600:
                del Bullet_Lst[Bullet_Lst.index(i)]

    update_canvas()
