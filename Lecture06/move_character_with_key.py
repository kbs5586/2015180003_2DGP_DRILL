from pico2d import *


def handle_events():
    global running
    global Dir
    Events = get_events()
    for event in Events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                Dir += 1
            elif event.key == SDLK_LEFT:
                Dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                Dir -= 1
            elif event.key == SDLK_LEFT:
                Dir += 1


open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
frame = 0
Dir = 0

while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, 90)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += Dir * 5
    # delay(0.05)

close_canvas()
