from pico2d import *

from Framwork import game_framework
from Scene import main_state
from Scene import clear_state



name = "AskPauseState"

class Ask:
    def __init__(self):
        self.image = load_image('Image/Scene/ask.png')
        self.x, self.y = 400, 300
    def draw(self):
        self.image.draw(self.x, self.y)


pauseimg = None
YES = None
YESColor = None
NO = None
NOColor = None
YESstate, NOstate = 0, 1
arrow = YESstate

def enter():
    global pauseimg
    global YES, YESColor
    global NO, NOColor

    pauseimg = Ask()
    YES =load_font('Font/GILSANUB.TTF', 40)
    YESColor = [255, 0, 0]
    NO = load_font('Font/GILSANUB.TTF', 40)
    NOColor = [0, 0, 0]

def exit():
    pass


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    global arrow
    global YESstate, NOstate
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                arrow -= 1
                if arrow < YESstate: arrow = NOstate
                pass
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                arrow += 1
                if arrow > NOstate: arrow = YESstate
                pass
            elif (event.type, event.key) == (SDL_KEYDOWN,13):
                if (arrow == YESstate):
                    game_framework.push_state(clear_state)
                    pass
                elif (arrow == NOstate):
                    game_framework.pop_state()
                    pass
                pass

    change_font_color()


def change_font_color():
    global NOColor, YESColor
    global arrow
    NOColor = [0, 0, 0]
    YESColor = [0, 0, 0]
    if (arrow == YESstate):
        YESColor = [255, 0, 0]
    elif (arrow == NOstate):
        NOColor = [255, 0, 0]

def update(frame_time):
    pass


def draw():
    clear_canvas()
    main_state.draw_scene()
    pauseimg.draw()
    YES.draw(250, 250, 'YES', YESColor)
    NO.draw(470, 250, 'NO', NOColor)
    update_canvas()





