import json
import os
import random
from pico2d import *

#만듬
from play import Game
from Framwork import game_framework
from Scene import title_state

from Scene import main_state
from play import Game

name = "HOWTOState"

Image = None
gameclear = None
pressanykey = None
font_get_treasure = None

playerInfo = None


def enter():
    global image, gameclear, pressanykey, font_get_treasure
    global playerInfo
    image = load_image('Image/Scene/howtoplay.png')
    pressanykey = load_font('Font/GILSANUB.TTF', 30)
    font_get_treasure = load_font('Font/GILSANUB.TTF', 50)

    playerInfo = Game.player
    pass

def exit():
    global image, gameclear, font_get_treasure
    del(image)
    del(gameclear)
    del(font_get_treasure)

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
        elif (event.type) == (SDL_KEYDOWN):
            game_framework.change_state(title_state)
        pass
    pass

def update(frame_time):

    pass


def draw_scene():
    image.draw(400, 300)

    pressanykey.draw(500, 30, 'Press Any Key', (0, 0, 0))

    pass



def draw():
    clear_canvas()
    draw_scene()
    update_canvas()
    pass





