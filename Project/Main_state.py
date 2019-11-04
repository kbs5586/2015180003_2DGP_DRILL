import random
import json
import os
import random

from pico2d import *
import game_framework

import Select_state
import Main_State.Player
import Main_State.Normal_Monster0

Back_Ground_Img = None

State_Lst = []
Player_Lst = []
Normal_Monster_Lst = []

Normal_Monster_Time = 0.0


def Create_Normal_Monster():
    global State_Lst
    global Normal_Monster_Time
    global Normal_Monster_Lst

    if Normal_Monster_Time > 2.0:
        for i in range(6):
            Monster = Main_State.Normal_Monster0.CNormal_Monster0(int(random.randint(1, 7)))
            Normal_Monster_Lst.append(Monster)
        State_Lst.append(Normal_Monster_Lst)
        Normal_Monster_Time = 0.0
    delay(0.01)
    Normal_Monster_Time += 0.01


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

    for i in State_Lst:
        for j in i:
            j.Update()

    Delete()
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
    global Normal_Monster_Lst
    global Player_Lst
    global State_Lst

    for i in Normal_Monster_Lst:
        if i.y <= 0:
            del Normal_Monster_Lst[Normal_Monster_Lst.index(i)]

    for i in Player_Lst[0].Bullet_Lst:
        if i.y >= 600:
            del Player_Lst[0].Bullet_Lst[Player_Lst[0].Bullet_Lst.index(i)]
