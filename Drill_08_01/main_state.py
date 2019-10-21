import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state

name = "MainState"

boy = None
grass = None
font = None
iX = 0
iY = 0
Dir = 0


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self, i, iX, iY, iDir):
        if i == 0:
            self.x, self.y = 0, 90
            self.dir = 1
        elif i != 0:
            self.x, self.y = iX, iY
            self.dir = iDir
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def enter():
    global boy, grass
    global iX
    global iY
    global Dir
    if pause_state.CheckNum == 1:
        boy = Boy(pause_state.CheckNum, iX, iY, Dir)
    elif pause_state.CheckNum == 0:
        boy = Boy(pause_state.CheckNum, iX, iY, Dir)
        grass = Grass()


def exit():
    global boy, grass
    del boy
    del grass


def pause():
    global boy
    global iX
    global iY
    global Dir
    iX = boy.x
    iY = boy.y
    Dir = boy.dir
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state)


def update():
    boy.update()


def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()
