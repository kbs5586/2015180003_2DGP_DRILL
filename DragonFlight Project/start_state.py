import game_framework
from pico2d import *
import Select_state

name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('Logo0.png')


def exit():
    global image
    del image


def pause():
    pass


def resume():
    pass


def handle_events():
    pass


def update():
    global logo_time
    if logo_time > 1.0:
        logo_time = 0
        game_framework.change_state(Select_state)
    delay(0.01)
    logo_time += 0.01


def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
