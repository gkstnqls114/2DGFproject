import json
import os
import random
from pico2d import *

#만듬
from play import Game
from Framwork import game_framework
from Scene import pause_state

name = "MainState"

game = None

def enter():
    global game
    game = Game.Game()
    game.enter()
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
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.push_state(pause_state)
        else:
            game.handle_events(event)
            pass
    pass

def update(frame_time):
    game.update(frame_time)
    pass


def draw_scene():
    game.draw_scene()
    pass


def draw():
    clear_canvas()
    draw_scene()
    update_canvas()
    pass





