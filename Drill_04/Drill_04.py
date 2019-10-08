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
    global IsStop
    IsStop=False



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
    if not IsStop:
        for i in range(0, 100 + 1, 2):
            clear_canvas()
            kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
            arrow.draw(v, u)

            t = i / 100
            x = (1 - t) * x1 + t * x2
            y = (1 - t) * y1 + t * y2

            if x2 > x1:
                character.clip_draw(frame * 100, 0, 100, 100, x, y)
            elif x2 < x1:
                character.clip_draw(frame * 100, 0, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            delay(0.05)
            handle_events()
            if x == x2 and y == y2:
                x1 = x2
                y1 = y2
                i = 0
                IsStop = True
    else:
        character.clip_draw(frame * 100, 0, 100, 100, x1, y1)
    update_canvas()
    handle_events()

close_canvas()
