import json
import os
import random
from pico2d import *


name = "Stairs"


class Stairs:
    image = None

    def __init__(self, bg):
        if self.image == None:
            self.image = load_image('Image/2Dstairs_2.png')

        self.background = bg

        self.name = None
        self.x = 300
        self.y = 125 + 110
        self.width = 300
        self.height = 300
        self.flooar_num = 1

    def update(self, frame_time):
        min_y = 0
        self.y = clamp(min_y,
                       self.y,
                       self.background.height)

        min_x = 0
        self.x = clamp(min_x,
                       self.x,
                       self.background.width)
        pass

    def draw(self):
        self.image.draw(self.x - self.background.window_left,
                        self.y - self.background.window_bottom,
                        self.width,
                        self.height)

        self.draw_bb()


    def get_bottom_bb(self):
        bottom_x = self.x  - self.background.window_left- self.width / 2
        bottom_y = self.y  - self.background.window_bottom- self.height / 2

        return bottom_x - 30, bottom_y - 30, bottom_x + 30, bottom_y + 30
        pass

    def get_top_bb(self):
        top_x = self.x  - self.background.window_left+ self.width / 2
        top_y = self.y  - self.background.window_bottom+ self.height / 2

        return top_x - 30, top_y - 30, top_x + 30, top_y + 30
        pass

    def get_bottom_point(self):
        bottom_x = self.x  - self.background.window_left - self.width / 2
        bottom_y = self.y  - self.background.window_bottom- self.height / 2

        return bottom_x, bottom_y

    def get_top_point(self):
        top_x = self.x  - self.background.window_left + self.width / 2
        top_y = self.y  - self.background.window_bottom + self.height / 2

        return top_x, top_y

    def draw_bb(self):
        draw_rectangle(*self.get_bottom_bb())
        draw_rectangle(*self.get_top_bb())






