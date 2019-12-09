import random
import json
import os
import random

from pico2d import *
import game_framework
import Main_state

Back_Ground_Img = None
State_Lst = []

def enter():
    global State_Lst
    State_Lst.append(Main_state.Player_Lst)
    pass


def exit():
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    pass


def update():
    for i in State_Lst:
        for j in i:
            j.Update()

def draw():
    for i in State_Lst:
        for j in i:
            j.Render()


def Delete():
    pass


def Collision():
    pass
