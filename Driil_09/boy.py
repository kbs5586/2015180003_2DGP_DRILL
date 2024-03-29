from pico2d import *

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SHIFT_DOWN, SHIFT_UP = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_LSHIFT): SHIFT_DOWN,
    (SDL_KEYUP, SDLK_LSHIFT): SHIFT_UP
}


# Boy States

class IdleState:
    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity - 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        elif event == SHIFT_DOWN:
            pass
        elif event == SHIFT_UP:
            pass
        boy.timer = 1000

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(boy.frame * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 200, 100, 100, boy.x, boy.y)


class RunState:
    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        elif event == SHIFT_DOWN:
            boy.cur_state = DashState
        elif event == SHIFT_UP:
            pass
        boy.dir = boy.velocity

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8

        boy.timer -= 1
        boy.x += boy.velocity
        boy.x = clamp(25, boy.x, 800 - 25)

    @staticmethod
    def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)


class DashState:
    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        elif event == SHIFT_DOWN:
            boy.speed = 10
        elif event == SHIFT_UP:
            boy.speed = 1
            boy.cur_state = RunState
        boy.timer = 1000

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        boy.x += boy.velocity * boy.speed
        boy.x = clamp(25, boy.x, 800 - 25)
        boy.dashtime += 0.01
        if boy.dashtime >= 1:
            boy.speed = 1
            boy.cur_state = RunState


    @staticmethod
    def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)


next_state_table = \
    {
        IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState,
                    RIGHT_DOWN: RunState, LEFT_DOWN: RunState},

        RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
                   LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SHIFT_DOWN: DashState, SHIFT_UP: DashState},

        DashState: {RIGHT_UP: DashState, LEFT_UP: DashState,
                    RIGHT_DOWN: DashState, LEFT_DOWN: DashState, SHIFT_DOWN: DashState, SHIFT_UP: DashState}
    }


class Boy:
    def __init__(self):
        self.x, self.y = 800 // 2, 90
        self.image = load_image('animation_sheet.png')
        self.dir = 1
        self.velocity = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.frame = 0
        self.speed = 1
        self.dashtime = 0

    def change_state(self, state):
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self.event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self.event)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


def handle_events():
    global boy
    events = get_events()
    for event in events:
        boy.handle_event(event)


open_canvas()

boy = Boy()
running = True;
while running:
    handle_events()
    boy.update()

    clear_canvas()
    boy.draw()

    update_canvas()

    delay(0.05)

close_canvas()
