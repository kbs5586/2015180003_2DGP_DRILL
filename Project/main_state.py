import random
import json
import os
import Select_state

from pico2d import *

import game_framework

logo_time = 0.0

name = "MainState"
x, y = 0, 0
Player = None
Bullet_Lst = []
Monster_Lst = []
Back_Ground_Img = None


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
        if logo_time > 0.05:
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
    image = None

    def __init__(self):
        self.x, self.y = Player.x, Player.y + 10
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
        self.y += 60

    def Draw(self):
        self.image.clip_draw(0, 0, 64, 64, self.x, self.y)


class CMonster:
    def __init__(self):
        self.x, self.y = 400, 300
        self.image = load_image('Monster0.png')

    def Update(self):
        self.y -= 1
        pass

    def Draw(self):
        self.image.clip_draw(0, 0, 116, 120, self.x, self.y)


def enter():
    global Player
    global Back_Ground_Img
    Back_Ground_Img = load_image('BackGround.png')
    Player = CPlayer()
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
    global logo_time
    global Monster_Lst
    if logo_time > 1.0:
        Monster = CMonster()
        Monster_Lst.append(Monster)
        logo_time = 0
    delay(0.01)
    logo_time += 0.01


def draw():
    global Back_Ground_Img
    global Player
    global Monster_Lst
    global Bullet_Lst
    clear_canvas()
    Back_Ground_Img.draw(400, 300)
    if Player is not None:
        Player.Update()
        Player.Draw()
    # if Monster_Lst is not None:
    # for i in Monster_Lst:
    # i.Update()
    # i.Draw()
    if Bullet_Lst is not None:
        for i in Bullet_Lst:
            i.Update()
            i.Draw()
            if i.y >= 600:
                del Bullet_Lst[Bullet_Lst.index(i)]

    update_canvas()
