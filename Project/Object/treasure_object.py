import json
import os
import random
from pico2d import *

class Treasure:
    image = None

    CLOSE, OPEN = 0, 1

    def __init__(self, bg):
        if(self.image == None):
            self.image = load_image('Image/샘플 상자.png')
        self.width = 100
        self.height = 100
        self.background = bg

        #상대적인 카메라 위치
        self.x = self.width / 2
        self.y = 90 + self.height / 2

        self.state = self.CLOSE
        self.floor_num = 1

    def draw(self):

        self.image.clip_draw(0, self.state * self.height, self.width, self.height,
                             self.x - self.background.window_left,
                             self.y - self.background.window_bottom)
        self.draw_bb()
        pass


    def update(self, frame_time):
        min_y = 0
        self.y = clamp(min_y,
                       self.y,
                       self.background.height)

        min_x = 0
        self.x = clamp(min_x,
                       self.x,
                       self.background.width)

    def open_box(self):
        self.state = self.OPEN
        pass


    def get_bb(self):
        return  self.x  - self.background.window_left - self.width /2 ,\
                 self.y  - self.background.window_bottom - self.height / 2,\
                 self.x  - self.background.window_left+ self.width / 2 ,\
                 self.y  - self.background.window_bottom + self.height / 2


    def get_point(self):
        return self.x  - self.background.window_left, self.y  - self.background.window_bottom- self.height / 2

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


