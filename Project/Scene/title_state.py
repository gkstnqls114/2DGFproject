from Framwork import game_framework
from Scene import main_state
from pico2d import *

from Scene import main_state
from Scene import howto_state
from Framwork import game_framework

name = "TitleState"
image = None
running = True
arrow = 0

GAME_START, GAME_HOW, GAME_QUIT = 0, 1, 2
START = None
EXIT = None
HOW = None
STARTColor = None
EXITColor = None
HOWColor = None

SelectColor = None
NotSelectColor = None

def enter():
    global image, START, EXIT, HOW
    global STARTColor, EXITColor, HOWColor
    global SelectColor, NotSelectColor

    image = load_image('Image/Scene/title.png')
    START = load_font('Font/GILSANUB.TTF', 40)
    EXIT = load_font('Font/GILSANUB.TTF', 40)
    HOW = load_font('Font/GILSANUB.TTF', 40)

    SelectColor = [255, 0, 0]
    NotSelectColor = [0, 0, 0]

    STARTColor = SelectColor
    HOWColor = NotSelectColor
    EXITColor = NotSelectColor


def exit():
    global image, START, EXIT, HOW
    del(image)
    del(START)
    del(EXIT)
    del(HOW)


def handle_events(frame_time):
    global running
    global arrow
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
                arrow -= 1
                if arrow < GAME_START: arrow = GAME_QUIT
                pass
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
                arrow += 1
                if arrow > GAME_QUIT: arrow = GAME_START
                pass
            elif (event.type, event.key) == (SDL_KEYDOWN, 13):
                if (arrow == GAME_START):
                    game_framework.change_state(main_state)
                    pass
                elif (arrow == GAME_HOW):

                    game_framework.change_state(howto_state)
                    pass
                elif (arrow == GAME_QUIT):
                    running = False
                    pass
                pass

    change_font_color()

def change_font_color():
    global STARTColor, EXITColor, HOWColor
    STARTColor = NotSelectColor
    HOWColor = NotSelectColor
    EXITColor = NotSelectColor

    if (arrow == GAME_START):
        STARTColor = SelectColor
    elif (arrow == GAME_HOW):
        HOWColor = SelectColor
    elif (arrow == GAME_QUIT):
        EXITColor = SelectColor


def draw():
    clear_canvas()
    image.draw(400, 300)

    START.draw(430, 210, 'GAME START', STARTColor)
    HOW.draw(430, 140, 'HOW TO PLAY', HOWColor)
    EXIT.draw(430, 70, 'EXIT', EXITColor)

    update_canvas()

def update(frame_time):

    if not running:
        game_framework.quit()   #quit은 exit를 호출한다. 앞 상태의 resume을 수행한다.


def pause():
    pass


def resume():
    pass






