import random
import json
import os
import random
import Select_state

from pico2d import *

import game_framework

Monster_BulletTime = 0.0
MidBoss_BulletTime = 0.0
Player_BulletTime = 0.0
Monster_time = 0.0
Total_time = 0.0

name = "MainState"
x, y = 0, 0
Player = None
Back_Ground_Img = None
Item = None
MidBoss = None

Bullet_Lst = []
MonsterBullet_Lst = []
MidBossBullet_Lst = []
Monster_Lst = []
MidBoss_Lst = []
Player_Lst = []
Item_Lst = []


class CPlayer:
    def __init__(self):
        self.x, self.y = x, y
        self.Bullet_Stack = 0
        self.ImgX, self.ImgY = 115, 110
        self.Hp = 1
        if Select_state.CharNum == 1:
            self.image = load_image('Resource//Player0.png')
        elif Select_state.CharNum == 2:
            self.image = load_image('Resource//Player1.png')
        elif Select_state.CharNum == 3:
            self.image = load_image('Resource//Player2.png')

    def Update(self):
        global x, y
        global Player_BulletTime
        global Bullet_Lst
        if Player_BulletTime > 0.05:
            Bullet = CBullet()
            Bullet_Lst.append(Bullet)
            Player_BulletTime = 0
        delay(0.01)
        Player_BulletTime += 0.01
        self.x, self.y = x, y

    def Draw(self):
        global Bullet_Lst
        self.image.clip_draw(0, 0, 155, 110, self.x, self.y)


class CMiBossBullet:
    image = None

    def __init__(self, x, y, Cnt):
        self.x, self.y = x, y - 30
        self.ImgX, self.ImgY = 45, 45
        self.Cnt = Cnt
        if CMiBossBullet.image is None:
            CMiBossBullet.image = load_image('Resource//BossBullet0.png')

    def Update(self):
        if self.Cnt % 4 == 1:
            self.x -= 2
            self.y -= 5
        elif self.Cnt % 4 == 2:
            self.x -= 1
            self.y -= 5
        elif self.Cnt % 4 == 3:
            self.x += 1
            self.y -= 5
        elif self.Cnt % 4 == 0:
            self.x += 2
            self.y -= 5
        pass

    def Draw(self):
        CMiBossBullet.image.clip_draw(0, 0, self.ImgX, self.ImgY, self.x, self.y)
        pass

    def Collision(self, Unit):
        pass


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
                        CBullet.image = load_image('Resource//Bullet_Ch0_0.png')
                elif Player.Bullet_Stack == 1:
                    if CBullet.image is None:
                        CBullet.image = load_image('Resource//Bullet_Ch0_1.png')

    def Update(self):
        self.y += 30

    def Draw(self):
        CBullet.image.clip_draw(0, 0, 64, 64, self.x, self.y)

    def Collision(self, Unit):
        for i in Unit:
            if self.x - 34 < i.x + i.ImgX / 2 \
                    and self.y + 34 > i.y - i.ImgY / 2 \
                    and self.x + 34 > i.x - i.ImgX / 2 \
                    and self.y - 34 < i.y + i.ImgY / 2:
                i.Hp -= 1
                if i.Hp <= 0:
                    rand = random.randint(0, 10)
                    if rand % 5 == 0:
                        i.Drop()
                    del Unit[Unit.index(i)]
                return True


class CMonster_Bullet:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y - 10
        self.ImgX, self.ImgY = 25, 25
        if CMonster_Bullet.image is None:
            CMonster_Bullet.image = load_image('Resource//Circle0.png')
        pass

    def Update(self):
        self.y -= 5
        pass

    def Draw(self):
        CMonster_Bullet.image.clip_draw(0, 0, self.ImgX, self.ImgY, self.x, self.y)
        pass

    def Collision(self, Unit):
        for i in Unit:
            if self.x - 12.5 < i.x + i.ImgX / 2 \
                    and self.y + 12.5 > i.y - i.ImgY / 2 \
                    and self.x + 12.5 > i.x - i.ImgX / 2 \
                    and self.y - 12.5 < i.y + i.ImgY / 2:
                i.Hp -= 1
                if i.Hp <= 0:
                    del Unit[Unit.index(i)]
                return True
        pass


class CItem:
    image = None

    def __init__(self, xPos=400):
        self.x = xPos
        self.y = 600
        if CItem.image is None:
            CItem.image = load_image('Resource//Item0.png')

    def Update(self):
        self.y -= 6
        pass

    def Draw(self):
        CItem.image.clip_draw(0, 0, 46, 46, self.x, self.y)
        pass


class CBossMonster:
    def __init__(self, BossNum):
        self.x, self.y = 400, 600
        self.ImgX, self.ImgY = 300, 300
        self.Hp = 100
        self.BulletCnt = 0
        if BossNum == 0:
            self.image = load_image('Resource//Boss0.png')
        elif BossNum == 1:
            pass

    def Update(self):
        global MidBoss_BulletTime
        global MidBossBullet_Lst
        if self.y <= 450:
            pass
        else:
            self.y -= 1

        if MidBoss_BulletTime > 0.5:
            for i in range(4):
                self.BulletCnt += 1
                MonsterBullet = CMiBossBullet(self.x, self.y, self.BulletCnt)
                MidBossBullet_Lst.append(MonsterBullet)
            MidBoss_BulletTime = 0.0
        MidBoss_BulletTime += 0.01

    def Drop(self):
        item = CItem()
        Item_Lst.append(item)
        pass

    def Draw(self):
        self.image.clip_draw(0, 0, self.ImgX, self.ImgY, self.x, self.y)


class CMonster:
    global MonsterBullet_Lst

    def __init__(self, xPos=1):
        self.x = xPos * 100
        self.y = 600
        self.image = load_image('Resource//Monster0.png')
        self.ImgX = 116
        self.ImgY = 120
        self.Hp = 1
        self.random = 0

    def Update(self):
        global Monster_BulletTime
        self.y -= 1
        if Monster_BulletTime > 1.0:
            MonsterBullet = CMonster_Bullet(self.x, self.y)
            MonsterBullet_Lst.append(MonsterBullet)

            Monster_BulletTime = 0.0
        Monster_BulletTime += 0.01
        pass

    def Drop(self):
        item = CItem()
        Item_Lst.append(item)

        pass

    def Draw(self):
        self.image.clip_draw(0, 0, self.ImgX, self.ImgY, self.x, self.y)


def enter():
    global Player
    global Back_Ground_Img
    global Player_Lst
    global MidBoss_Lst
    Back_Ground_Img = load_image('Resource//BackGround.png')
    Player = CPlayer()
    Player_Lst.append(Player)

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
    global Monster_Lst, Bullet_Lst, MidBoss_Lst, Player_Lst
    global MidBoss
    global MonsterBullet_Lst

    if Monster_time > 2.0:
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
    if Total_time >= 6:
        MidBoss = CBossMonster(0)
        MidBoss_Lst.append(MidBoss)
        Total_time = -60

    # 몬스터 충돌
    for j in Bullet_Lst:
        if j.Collision(Monster_Lst):
            del Bullet_Lst[Bullet_Lst.index(j)]
    for i in Bullet_Lst:
        if i.Collision(MidBoss_Lst):
            del Bullet_Lst[Bullet_Lst.index(i)]

    # 플레이어 충돌
    # for i in MonsterBullet_Lst:
    # i.Collision(Player_Lst)

    if len(Player_Lst) <= 0:
        pass


def draw():
    global Back_Ground_Img
    global Monster_Lst
    global Bullet_Lst
    global MidBoss_Lst
    global Player_Lst
    global MidBossBullet_Lst
    clear_canvas()
    Back_Ground_Img.draw(400, 300)

    for i in Player_Lst:
        i.Update()
        i.Draw()

    for i in Monster_Lst:
        i.Update()
        i.Draw()
        if i.y <= 0:
            del Monster_Lst[Monster_Lst.index(i)]

    for i in Bullet_Lst:
        i.Update()
        i.Draw()
        if i.y >= 600:
            del Bullet_Lst[Bullet_Lst.index(i)]

    for i in MidBoss_Lst:
        i.Update()
        i.Draw()

    for i in MonsterBullet_Lst:
        i.Update()
        i.Draw()

    for i in MidBossBullet_Lst:
        i.Update()
        i.Draw()

    for i in Item_Lst:
        i.Update()
        i.Draw()
    update_canvas()
