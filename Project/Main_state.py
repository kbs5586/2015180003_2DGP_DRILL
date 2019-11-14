import random
import json
import os
import random

from pico2d import *
import game_framework

import Select_state
import Main_State.Player
import Main_State.Normal_Monster0
import Main_State.Normal_Monster1
import Main_State.MidBoss

Back_Ground_Img = None

State_Lst = []
Player_Lst = []

Normal_Monster_Time = 0.0
Mid_Boss_Time = 0.0


def Create_Normal_Monster():
    global State_Lst
    global Normal_Monster_Time
    Normal_Monster_Lst = []
    if Normal_Monster_Time > 5.0:
        for i in range(6):
            rnd = random.randint(0, 10)
            if rnd <= 7:
                Monster = Main_State.Normal_Monster0.CNormal_Monster0(int(random.randint(1, 7)))
            else:
                Monster = Main_State.Normal_Monster1.CNormal_Monster1(int(random.randint(1, 7)))
            Normal_Monster_Lst.append(Monster)
        State_Lst.append(Normal_Monster_Lst)
        Normal_Monster_Time = 0.0
    Normal_Monster_Time += 0.01


def Create_MidBoss():
    global State_Lst
    global Mid_Boss_Time
    Mid_Monster_Lst = []
    if Mid_Boss_Time > 30.0:
        MidBoss = Main_State.MidBoss.CMidBoss()
        Mid_Monster_Lst.append(MidBoss)
        State_Lst.append(Mid_Monster_Lst)
        Mid_Boss_Time = 0.0
    Mid_Boss_Time += 0.01
    pass


def enter():
    global Back_Ground_Img
    global Player_Lst
    global State_Lst
    Back_Ground_Img = load_image('Resource//BackGround.png')
    player = Main_State.Player.CPlayer(Select_state.CharNum)
    Player_Lst.append(player)

    State_Lst.append(Player_Lst)
    pass


def exit():
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    global Player_Lst
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 600 - 1 - event.y
            for i in Player_Lst:
                i.Mouse_Move(x, y)
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            pass


def update():
    Create_Normal_Monster()
    Create_MidBoss()
    for i in State_Lst:
        for j in i:
            j.Update()

    Delete()
    Collision()
    pass


def draw():
    global Back_Ground_Img
    global State_Lst
    clear_canvas()
    Back_Ground_Img.draw(400, 300)

    for i in State_Lst:
        for j in i:
            j.Render()

    update_canvas()


def Delete():
    global Player_Lst
    global State_Lst

    for i in State_Lst:
        for j in i:
            if j.Type == "Monster":
                if j.y <= 0:
                    del i[i.index(j)]
            if j.Type == "Player":
                for k in j.Bullet_Lst:
                    if k.y >= 600:
                        del j.Bullet_Lst[j.Bullet_Lst.index(k)]


def Collision():
    global State_Lst

    for i in State_Lst:
        for j in i:
            if j.Type == "Player":
                for k in State_Lst:
                    for l in k:
                        if l.Type == "Item":
                            j.Collision(k)
                for k in j.Bullet_Lst:
                    for l in State_Lst:
                        for h in l:
                            if h.Type == "Monster":
                                k.Collision(l)
        pass

    pass
