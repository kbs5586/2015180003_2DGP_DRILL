from pico2d import *
from random import *


def handle_events():
    global running
    global v, u
    global x2, y2
    global Move
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def Random_Coordinate():
    global CoordiLst
    for i in range(0, 20):
        rx = randint(0, 1280)
        ry = randint(0, 1024)
        CoordiLst.append(rx)
        CoordiLst.append(ry)


def Move_Player(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
    global x, y
    global Move
    global frame
    global FrameY
    global CenterX
    global DirX
    DirX = x
    # draw p1-p2
    for i in range(0, 50, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
        y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]
        if x > CenterX:
            FrameY = 100
        else:
            FrameY = 0
        character.clip_draw(frame * 100, FrameY, 100, 100, x, y)
        frame = (frame + 1) % 8
        delay(0.05)
        update_canvas()
    # draw p2-p3
    for i in range(0, 100, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p2[0] + (-4 * t ** 2 + 4 * t) * p3[0] + (2 * t ** 2 - t) * p4[0]
        y = (2 * t ** 2 - 3 * t + 1) * p2[1] + (-4 * t ** 2 + 4 * t) * p3[1] + (2 * t ** 2 - t) * p4[1]
        if x > CenterX:
            FrameY = 100
        else:
            FrameY = 0
        character.clip_draw(frame * 100, FrameY, 100, 100, x, y)
        frame = (frame + 1) % 8
        delay(0.05)
        update_canvas()
    # draw p3-p4
    for i in range(50, 100, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p3[0] + (-4 * t ** 2 + 4 * t) * p4[0] + (2 * t ** 2 - t) * p5[0]
        y = (2 * t ** 2 - 3 * t + 1) * p3[1] + (-4 * t ** 2 + 4 * t) * p4[1] + (2 * t ** 2 - t) * p5[1]
        if x > CenterX:
            FrameY = 100
        else:
            FrameY = 0
        character.clip_draw(frame * 100, FrameY, 100, 100, x, y)
        frame = (frame + 1) % 8
        delay(0.05)
        update_canvas()

    # draw p4-p5
    for i in range(50, 100, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p4[0] + (-4 * t ** 2 + 4 * t) * p5[0] + (2 * t ** 2 - t) * p6[0]
        y = (2 * t ** 2 - 3 * t + 1) * p4[1] + (-4 * t ** 2 + 4 * t) * p5[1] + (2 * t ** 2 - t) * p6[1]
        if x > CenterX:
            FrameY = 100
        else:
            FrameY = 0
        character.clip_draw(frame * 100, FrameY, 100, 100, x, y)
        frame = (frame + 1) % 8
        delay(0.05)
        update_canvas()

    # draw p5-p6
    for i in range(50, 100, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p5[0] + (-4 * t ** 2 + 4 * t) * p6[0] + (2 * t ** 2 - t) * p7[0]
        y = (2 * t ** 2 - 3 * t + 1) * p5[1] + (-4 * t ** 2 + 4 * t) * p6[1] + (2 * t ** 2 - t) * p7[1]
        if x > CenterX:
            FrameY = 100
        else:
            FrameY = 0
        character.clip_draw(frame * 100, FrameY, 100, 100, x, y)
        frame = (frame + 1) % 8
        delay(0.05)
        update_canvas()

    # draw p6-p7
    for i in range(50, 100, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p6[0] + (-4 * t ** 2 + 4 * t) * p7[0] + (2 * t ** 2 - t) * p8[0]
        y = (2 * t ** 2 - 3 * t + 1) * p6[1] + (-4 * t ** 2 + 4 * t) * p7[1] + (2 * t ** 2 - t) * p8[1]
        if x > CenterX:
            FrameY = 100
        else:
            FrameY = 0
        character.clip_draw(frame * 100, FrameY, 100, 100, x, y)
        frame = (frame + 1) % 8
        delay(0.05)
        update_canvas()

    # draw p7-p8
    for i in range(50, 100, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p7[0] + (-4 * t ** 2 + 4 * t) * p8[0] + (2 * t ** 2 - t) * p9[0]
        y = (2 * t ** 2 - 3 * t + 1) * p7[1] + (-4 * t ** 2 + 4 * t) * p8[1] + (2 * t ** 2 - t) * p9[1]
        if x > CenterX:
            FrameY = 100
        else:
            FrameY = 0
        character.clip_draw(frame * 100, FrameY, 100, 100, x, y)
        frame = (frame + 1) % 8
        delay(0.05)
        update_canvas()
    # draw p8-p9
    for i in range(50, 100, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p8[0] + (-4 * t ** 2 + 4 * t) * p9[0] + (2 * t ** 2 - t) * p10[0]
        y = (2 * t ** 2 - 3 * t + 1) * p8[1] + (-4 * t ** 2 + 4 * t) * p9[1] + (2 * t ** 2 - t) * p10[1]
        if x > CenterX:
            FrameY = 100
        else:
            FrameY = 0
        character.clip_draw(frame * 100, FrameY, 100, 100, x, y)
        frame = (frame + 1) % 8
        delay(0.05)
        update_canvas()

    # draw p9-p10
    for i in range(50, 100, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p9[0] + (-4 * t ** 2 + 4 * t) * p10[0] + (2 * t ** 2 - t) * p1[0]
        y = (2 * t ** 2 - 3 * t + 1) * p9[1] + (-4 * t ** 2 + 4 * t) * p10[1] + (2 * t ** 2 - t) * p1[1]
        if x > CenterX:
            FrameY = 100
        else:
            FrameY = 0
        character.clip_draw(frame * 100, FrameY, 100, 100, x, y)
        frame = (frame + 1) % 8
        delay(0.05)
        update_canvas()


KPU_WIDTH, KPU_HEIGHT = 1280, 1024
open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True

x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
CenterX = KPU_WIDTH // 2
MovX, MovY = 0, 0;
DirX = 0
Move = True
frame = 0
CoordiLst = []

FrameY = 100;
Random_Coordinate()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    if Move:

        Move_Player((CoordiLst[0], CoordiLst[1]), (CoordiLst[2], CoordiLst[3]), (CoordiLst[4], CoordiLst[5]),
                    (CoordiLst[6], CoordiLst[7]),
                    (CoordiLst[8], CoordiLst[9]), (CoordiLst[10], CoordiLst[11]), (CoordiLst[12], CoordiLst[13]),
                    (CoordiLst[14], CoordiLst[15]),
                    (CoordiLst[16], CoordiLst[17]), (CoordiLst[18], CoordiLst[19]))

        handle_events()
    else:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)

    update_canvas()
    handle_events()

close_canvas()
