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
import Main_State.Normal_Monster2
import Main_State.MidBoss
import Main_State.Meteor
import Main_State.Boss

import Main_State2

Back_Ground_Img = None

State_Lst = []
Player_Lst = []

Normal_Monster_Time = 0.0
Mid_Boss_Time = 0.0
Boss_Time = 0.0
Meteor_Time = 0.0
Meteor_Term = 7.0

IsStage1_End = False
IsStage2_End = False

Game_Time = 0.0
MainFont = 0
Score = 0.0


def Create_Meteor():
    global State_Lst
    global Meteor_Time
    global Meteor_Term
    Meteor_Lst = []
    Meteor_Time += game_framework.frame_time
    if IsStage1_End:
        Meteor_Term = 5.0

    if Meteor_Time > Meteor_Term:
        for i in range(6):
            Meteor = Main_State.Meteor.CMeteor(int(random.randint(1, 7)))
            Meteor_Lst.append(Meteor)
        State_Lst.append(Meteor_Lst)
        Meteor_Time = 0.0
    pass


def Create_Normal_Monster():
    global State_Lst
    global Normal_Monster_Time
    Normal_Monster_Lst = []
    Normal_Monster_Time += game_framework.frame_time
    if Normal_Monster_Time > 4.0:
        for i in range(6):
            rnd = random.randint(0, 10)
            if rnd <= 7:
                Monster = Main_State.Normal_Monster0.CNormal_Monster0(int(random.randint(1, 7)))
            else:
                Monster = Main_State.Normal_Monster1.CNormal_Monster1(int(random.randint(1, 7)))
            Normal_Monster_Lst.append(Monster)
        State_Lst.append(Normal_Monster_Lst)
        Normal_Monster_Time = 0.0


def Create_MidBoss():
    global State_Lst
    global Mid_Boss_Time
    Mid_Monster_Lst = []
    Mid_Boss_Time += game_framework.frame_time
    if Mid_Boss_Time > 10.0:
        MidBoss = Main_State.MidBoss.CMidBoss()
        Mid_Monster_Lst.append(MidBoss)
        State_Lst.append(Mid_Monster_Lst)
        Mid_Boss_Time = -100000000.0
    pass


def Create_Boss():
    global State_Lst
    global Boss_Time
    global IsStage1_End
    Boss_Lst = []
    if IsStage1_End:
        Boss_Time += game_framework.frame_time
        if Boss_Time > 40.0:
            Boss = Main_State.Boss.CBoss()
            Boss_Lst.append(Boss)
            State_Lst.append(Boss_Lst)
            Boss_Time = -1090000000000


def Create_Normal_Monster_Phase2():
    global State_Lst
    global Normal_Monster_Time
    Normal_Monster_Lst = []
    Normal_Monster_Time += game_framework.frame_time
    if Normal_Monster_Time > 3.0:
        for i in range(6):
            rnd = random.randint(0, 10)
            if rnd <= 7:
                Monster = Main_State.Normal_Monster2.CNormal_Monster2(int(random.randint(1, 7)))
            else:
                Monster = Main_State.Normal_Monster2.CNormal_Monster2(int(random.randint(1, 7)))
            Normal_Monster_Lst.append(Monster)
        State_Lst.append(Normal_Monster_Lst)
        Normal_Monster_Time = 0.0


def enter():
    global Back_Ground_Img
    global Player_Lst
    global State_Lst
    global MainFont
    MainFont = load_font('ENCR10B.TTF', 50)

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
    global State_Lst
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_1:
            for i in State_Lst:
                for j in i:
                    if j.Type == 'Player':
                        j.Change_Player(0)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            for i in State_Lst:
                for j in i:
                    if j.Type == 'Player':
                        j.Change_Player(1)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_3:
            for i in State_Lst:
                for j in i:
                    if j.Type == 'Player':
                        j.Change_Player(2)
            pass
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 600 - 1 - event.y
            for i in Player_Lst:
                i.Mouse_Move(x, y)
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            pass


def update():
    global IsStage1_End
    global BgmSound
    if not IsStage1_End:
        Create_Normal_Monster()
    else:
        Create_Normal_Monster_Phase2()
    Create_Meteor()
    Create_MidBoss()
    Create_Boss()

    for i in State_Lst:
        for j in i:
            j.Update()

    Delete()
    Collision()
    pass


def draw():
    global Back_Ground_Img
    global State_Lst
    global IsStage2_End
    global MainFont
    global Score

    if not IsStage2_End:
        Score += game_framework.frame_time
    clear_canvas()
    Back_Ground_Img.draw(400, 300)

    for i in State_Lst:
        for j in i:
            j.Render()

    if IsStage2_End:
        MainFont.draw(200, 300, 'Game_Over: %d' % Score, (255, 255, 255))

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
            if j.Type == "MidBoss":
                if j.y <= 0:
                    IsMidBossDead = True
                    del i[i.index(j)]
                for k in j.Bullet_Lst:
                    if k.LifeTime >= 5.0:
                        del j.Bullet_Lst[j.Bullet_Lst.index(k)]
            if j.Type == "Meteor":
                if j.y <= 0:
                    del i[i.index(j)]


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
                            if h.Type == "MidBoss":
                                k.Collision(l)
                            if h.Type == "Boss":
                                k.Collision(l)
                # if j.Type == "Meteor":
                # for k in State_Lst:
                # for l in k:
                # if l.Type == "Player":
                # j.Collision(k)
                pass
        pass

    pass
