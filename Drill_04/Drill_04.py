from pico2d import *
open_canvas()
ch = load_image('animation_sheet.png')
gr = load_image('grass.png')
test
x = 0
frameX = 0
frameY = 100
turn = False;

while True:
    if not turn:
        clear_canvas()
        gr.draw(400, 30)
        ch.clip_draw(frameX * 100, frameY, 100, 100, x, 90)
        # ch.draw(x,90)
        update_canvas()
        frameX = (frameX + 1) % 8
        x += 5
        delay(0.05)
        get_events()
        if x >= 800:
            turn = True
            frameX = 0
            frameY = 0

    if turn:
        clear_canvas()
        gr.draw(400, 30)
        ch.clip_draw(frameX * 100, frameY, 100, 100, x, 90)
        # ch.draw(x,90)
        update_canvas()
        frameX = (frameX + 1) % 8
        x -= 5
        delay(0.05)
        get_events()
        if x <= 0:
            turn = False
            frameX = 0
            frameY = 100
