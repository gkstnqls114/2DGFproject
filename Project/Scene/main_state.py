import json
import os
import random
from pico2d import *

from Scene import pause_state
from Scene import title_state
from Framwork import game_framework

name = "MainState"

boy = None
grass = None
font = None


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



class Boy:
    def __init__(self):

        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('샘플 플레이어.png')
        self.dir = 1

        #움직임 bool
        self.Run = False
        self.Right = False
        self.Left = False
        self.Up = False
        self.Down = False

        self.runningTime = 0
        self.pause = (self.x, self.y, self.frame, self.dir)

    def update(self):
        self.frame = (self.frame + 1) % 8

        self.runningFunc()

        if(self.Right):
            self.x += self.dir
        if (self.Left):
            self.x -= self.dir

    def draw(self):
        #self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        self.image.draw( self.x, self.y)

    def handle_events(self, event):
            # key down

        if event.type == SDL_KEYDOWN:
            z = 122
            if event.key == z:
                self.Run = True
            elif event.key == SDLK_RIGHT:
                self.Right = True
            elif  event.key == SDLK_LEFT:
                self.Left = True
            elif event.key == SDLK_UP:
                self.Up = True
            elif event.key ==SDLK_DOWN:
                self.Down = True

            # key up

        if event.type == SDL_KEYUP:
            z = 122
            if event.key == z:
                self.Run = False
            elif event.key == SDLK_RIGHT:
                self.Right = False
            elif  event.key == SDLK_LEFT:
                self.Left = False
            elif event.key == SDLK_UP:
                self.Up = False
            elif event.key ==SDLK_DOWN:
                self.Down = False


    def runningFunc(self):
        if self.runningTime > 100:
            self.runningTime = 0
            if self.dir < 2.5:
               self.dir += 0.1



        if self.Run == True:
            self.runningTime += 1
        else:
            self.runningTime = 0
            self.dir = 1


def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()


def exit():
    global boy, grass
    del(boy)
    del(grass)


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
    boy.update()


def draw_scene():
    grass.draw()
    boy.draw()


def draw():
    clear_canvas()
    draw_scene()
    update_canvas()





