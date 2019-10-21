import game_framework
from pico2d import *
import main_state

name = "PauseState"
image = None
logo_time = 0.0
CheckNum=0

def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del image


def pause():
    pass


def resume():
    pass


def handle_events():
    global CheckNum
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.push_state(main_state)
                CheckNum=1


def update():
    pass


def draw():
    clear_canvas()
    image.draw(400, 300, 100, 100)
    update_canvas()
