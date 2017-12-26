import json
import os
import random
from pico2d import *

#만듬
from play import Game
from Framwork import game_framework
from Scene import title_state

name = "OverState"

Image = None
gameover = None
pressanykey = None

def enter():
    global image, gameover, pressanykey
    image = load_image('Image/Scene/game_clear.png')
    gameover = load_font('Font/GILSANUB.TTF', 70)
    pressanykey = load_font('Font/GILSANUB.TTF', 30)

    pass

def exit():
    global image, gameover
    del(image)
    del(gameover)

    pass


def pause():
    pass

def resume():
    pass

def handle_events(frame_time):
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_state(title_state)
        pass
    pass

def update(frame_time):

    pass


def draw_scene():
    image.draw(400, 300)

    gameover.draw(170, 500, 'GAME CLEAR', (255, 0, 0))
    pressanykey.draw(500, 30, 'Press Any Key', (0, 0, 0))

    pass



def draw():
    clear_canvas()
    draw_scene()
    update_canvas()
    pass





