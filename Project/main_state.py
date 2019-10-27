import random
import json
import os
import Select_state

from pico2d import *

import game_framework

name = "MainState"
x, y = 0, 0
Player = None


class CPlayer:
    def __init__(self):
        self.x, self.y = x, y
        self.Bullet_Stack=0
        self.image = load_image('Player0.png')

    def Update(self):
        global x, y
        self.x, self.y = x, y

    def Draw(self):
        self.image(self.x, self.y)


def enter():
    global Player
    Player=CPlayer()
    Select_state.CharNum
    i = 0

    pass


def exit():
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def update():
    pass


def draw():
    clear_canvas()

    update_canvas()
