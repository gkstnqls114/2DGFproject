import json
import os
import random
from pico2d import *

#만듬
from play import Game
from Framwork import game_framework
from Scene import title_state

name = "OverState"

game = None

def enter():

    pass

def exit():

    pass


def pause():
    pass

def resume():
    pass

def handle_events(frame_time):
    events = get_events()

    for event in events:
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_state(title_state)
        pass
    pass

def update(frame_time):

    pass


def draw_scene():

    pass



def draw():
    clear_canvas()
    draw_scene()
    update_canvas()
    pass





