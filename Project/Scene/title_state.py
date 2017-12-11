from Framwork import game_framework
from Scene import main_state
from pico2d import *

from Scene import main_state
from Framwork import game_framework

name = "TitleState"
image = None
running = True
arrow = 0

GAME_START, GAME_QUIT = 0, 1

def enter():
    global image
    image = load_image('Image/샘플 타이틀.png')


def exit():
    global image
    del(image)


def handle_events(frame_time):
    global running
    global arrow
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
                if(arrow == GAME_START): arrow = GAME_QUIT
                else: arrow -= 1
                pass
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
                arrow += 1
                arrow %= 2
                pass
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                if (arrow == GAME_START):
                    game_framework.change_state(main_state)
                    pass
                if (arrow == GAME_QUIT):
                    running = False
                    pass
                pass


def draw():
    clear_canvas()
    image.draw(400, 300)

    if(arrow == GAME_START):
        #일단 하드코딩
        draw_rectangle(250, 150, 270, 170)
        pass
    if (arrow == GAME_QUIT):
        draw_rectangle(250, 100, 270, 120)
        pass

    update_canvas()

def update(frame_time):
    if not running:
        game_framework.quit()   #quit은 exit를 호출한다. 앞 상태의 resume을 수행한다.


def pause():
    pass


def resume():
    pass






