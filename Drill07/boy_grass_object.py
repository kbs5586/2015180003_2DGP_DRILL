from pico2d import *
import math
import random


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30);


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 6
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Small_Ball:
    def __init__(self):
        self.x, self.y = 0, 599
        self.x = random.randint(0, 800)
        self.image = load_image('ball21x21.png')
        self.Speed = random.randint(1, 10)
        self.Speed = self.Speed * 0.01;

        self.Time = 0
        self.g = 9.8
        self.h = 0

    def update(self):
        if self.y <= 70:
            pass
        else:
            self.h = 0.5 * self.g * math.pow(self.Time, 2);
            self.Time += self.Speed;
            self.y -= self.h

    def draw(self):
        self.image.draw(self.x, self.y);


class Big_Ball:
    def __init__(self):
        self.x, self.y = 0, 599
        self.x = random.randint(0, 800)
        self.image = load_image('ball41x41.png')
        self.Speed = random.randint(1, 10)
        self.Speed = self.Speed * 0.01;

        self.Time = 0
        self.g = 9.8
        self.h = 0

    def update(self):
        if self.y <= 80:
            pass
        else:
            self.h = 0.5 * self.g * math.pow(self.Time, 2);
            self.Time += self.Speed;
            self.y -= self.h

    def draw(self):
        self.image.draw(self.x, self.y);


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# initialization code
open_canvas()
NumOfBig = 20
NumOfSmall = random.randint(0, 20)

NumOfBig -= NumOfSmall;

team = [Boy() for i in range(11)]
grass = Grass()

Small_Balls = [Small_Ball() for i in range(NumOfSmall)]
Big_Balls = [Big_Ball() for i in range(NumOfBig)]


running = True

# game main loop code

while running:
    handle_events()

    for small in Small_Balls:
        small.update()
    for big in Big_Balls:
        big.update()
    for boy in team:
        boy.update()



    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for small in Small_Balls:
        small.draw()
    for big in Big_Balls:
        big.draw()


    update_canvas()

    delay(0.05)

# finalization code

close_canvas()
