import json
import os
import random
from pico2d import *

#만듬
import Game

from Framwork import game_framework

name = "MainState"

game = None

def enter():
    global game
    game = Game.Game()
    game.enter()
    pass

def exit():
    game.exit()
    pass


def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state)
        else:
            game.handle_events(event)
            pass
    pass

def update():
    game.update()
    pass


def draw_scene():
    game.draw_scene()
    pass



def draw():
    clear_canvas()
    draw_scene()
    update_canvas()
    pass





