import game_framework
from pico2d import *
import main_state

name = "StartState"
image = None
logo_time = 0.0
Cur = None
x, y = 0, 0
PostCh0 = None
PostCh1 = None
PostCh2 = None
CharNum = 0


class Cursor:
    def __init__(self):
        self.x, self.y = 400, 300
        self.image = load_image('Resource//Cursor.png')

    def Update(self):
        global x, y
        self.x, self.y = x, y

    def draw(self):
        self.image.draw(self.x, self.y)


class PosterChar0:
    def __init__(self):
        self.x, self.y = 133, 300
        self.image = load_image('Resource//Char0.png')

    def Draw(self):
        self.image.draw(self.x, self.y)


class PosterChar1:
    def __init__(self):
        self.x, self.y = 400, 300
        self.image = load_image('Resource//Char1.png')

    def Draw(self):
        self.image.draw(self.x, self.y)


class PosterChar2:
    def __init__(self):
        self.x, self.y = 666, 300
        self.image = load_image('Resource//Char2.png')

    def Draw(self):
        self.image.draw(self.x, self.y)


def enter():
    global image
    global Cur
    global PostCh0, PostCh1, PostCh2

    PostCh0 = PosterChar0()
    PostCh1 = PosterChar1()
    PostCh2 = PosterChar2()

    Cur = Cursor()
    image = load_image('Resource//Logo0.png')


def exit():
    global image
    del image


def pause():
    pass


def resume():
    pass


def handle_events():
    global x, y
    global Cur, CharNum
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 600 - 1 - event.y
            if Cur is not None:
                Cur.Update()
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if 266 >= event.x >= 0:
                CharNum = 1
                game_framework.change_state(main_state)
            elif 266 <= event.x <= 532:
                j = 0
            elif 532 <= event.x <= 800:
                k = 0
            pass


def update():
    global logo_time

    delay(0.01)
    logo_time += 0.01


def draw():
    hide_cursor()
    global image
    global Cur, PostCh0, PostCh1, PostCh2
    clear_canvas()
    image.draw(400, 300)

    PostCh0.Draw()
    PostCh1.Draw()
    PostCh2.Draw()
    Cur.draw()
    update_canvas()
