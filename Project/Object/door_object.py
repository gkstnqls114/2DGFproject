import json
import os
import random
from pico2d import *

from Framwork import game_framework
from Scene import clear_state


name = "Door"

class door:


    def __init__(self, bg):
        self.name = None
        self.image = load_image('Image/door.png')
        self.width = self.image.w
        self.height =self.image.h
        self.x = self.width / 2
        self.y = self.height / 2

        self.background = bg

    def update(self, frame_time):
        pass

    def game_claer(self):
        game_framework.change_state(clear_state)


    def draw(self):
        self.image.draw(self.x - self.background.window_left,\
                             self.y - self.background.window_bottom)

    def get_bb(self):
        left = self.x - self.background.window_left - self.width / 2
        bottom = self.y - self.background.window_bottom - self.height /2
        right = self.x  - self.background.window_left + self.width / 2
        top = self.y - self.background.window_bottom + self.width / 2
        return left, bottom, right, top
        pass


    def draw_bb(self):
        draw_rectangle(*self.get_bb())





