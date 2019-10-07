from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    global handX, handy
    global ClickX, ClickY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN and SDL_BUTTON_LEFT:
            ClickX, ClickY = event.x, KPU_HEIGHT - 1 - event.y
            MovePlayer((x, y), (ClickX, ClickY))
        elif event.type == SDL_MOUSEMOTION:
            handX, handy = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def MovePlayer(p1, p2):
    global x, y
    global ClickY, ClickY
    global ResultX, ResultY
    global IsStop
    for i in range(0, 10000 + 1, 2):
        t = i / 10000
        x1 = ((1 - t) * p1[0] + t * p2[0]) * 0.001
        y1 = ((1 - t) * p1[1] + t * p2[1]) * 0.001
        if ClickX > x:
            if ClickY > y:
                x += x1
                y += y1
            elif ClickY < y:
                x += x1
                y -= y1
        elif ClickX < x:
            if ClickY > y:
                x -= x1
                y += y1
            elif ClickY < y:
                x -= x1
                y -= y1
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    ResultX = x
    ResultY = y


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png');

handX, handy = KPU_WIDTH // 2, KPU_HEIGHT // 2
ResultX, ResultY = KPU_WIDTH // 2, KPU_HEIGHT // 2

IsStop=False
ClickX, ClickY = 0, 0
Count = 0
running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100, 100, 100, ResultX, ResultY)
    hand.draw(handX + 22, handy - 20);
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()
