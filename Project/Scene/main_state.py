import json
import os
import random
from pico2d import *

#Scene
from Scene import pause_state
from Scene import title_state
from Framwork import game_framework

#Object
from Object import player_object
from Object import stairs_object

name = "MainState"

boy = None
grass = None
stairs = None
font = None


class Grass:
    def __init__(self):
        self.image = load_image('샘플 바닥.png')
        self.width = 800
        self.height = 90

    def draw(self):
        self.image.draw(400, self.height / 2)


def enter():
    global boy, grass, stairs
    boy = player_object.Player()
    stairs = stairs_object.Stairs()
    grass = Grass()


def exit():
    global boy, grass, stairs
    del(boy)
    del(grass)
    del(stairs)


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
            boy.handle_events(event)

def update():
    boy.around_stairs(stairs)
    boy.update()


def draw_scene():
    grass.draw()
    stairs.draw()
    boy.draw()



def draw():
    clear_canvas()
    draw_scene()
    update_canvas()





