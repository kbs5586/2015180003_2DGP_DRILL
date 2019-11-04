import game_framework
from pico2d import *
import Main_state
import Select_State.Cursor
import Select_State.Portrait

Name = "Select_State"
Logo_Image = None
Logo_Time = 0.0
cursor = None
CharNum=0

Portrait_Lst = []
State_Lst = []


def enter():
    global Logo_Image
    global cursor
    global Portrait_Lst
    global State_Lst
    if Logo_Image is None:
        Logo_Image = load_image('Resource//Logo0.png')
    if cursor is None:
        cursor = Select_State.Cursor.CCursor()

    for i in range(3):
        portrait = Select_State.Portrait.CPortrait(i)
        Portrait_Lst.append(portrait)
    State_Lst.append(Portrait_Lst)


def exit():
    global Logo_Image
    del Logo_Image


def pause():
    pass


def resume():
    pass


def handle_events():
    global cursor
    global CharNum
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 600 - 1 - event.y
            if cursor is not None:
                cursor.Mouse_Move(x, y)
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if 266 >= event.x >= 0:
                CharNum = 0
                game_framework.change_state(Main_state)
            elif 266 <= event.x <= 532:
                CharNum = 1
                game_framework.change_state(Main_state)
            elif 532 <= event.x <= 800:
                CharNum = 2
                game_framework.change_state(Main_state)
            pass


def update():
    global Logo_Time
    global cursor
    global State_Lst

    delay(0.01)
    Logo_Time += 0.01
    cursor.Update()
    for i in State_Lst:
        for j in i:
            j.Update()


def draw():
    global Logo_Image
    global cursor
    global State_Lst
    hide_cursor()

    clear_canvas()
    Logo_Image.draw(400, 300)

    for i in State_Lst:
        for j in i:
            j.Render()
    if cursor is not None:
        cursor.Render()
    update_canvas()
