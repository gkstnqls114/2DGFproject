import json
import os
import random
from pico2d import *

class Treasure:
    image = None

    CLOSE, OPEN = 0, 1

    def __init__(self):
        if(self.image == None):
            self.image = load_image('Image/샘플 상자.png')
        self.width = 100
        self.height = 100

        #상대적인 카메라 위치
        self.x = self.width / 2
        self.y = 90 + self.height / 2
        self.move_x = 0
        self.move_y = 0

        self.state = self.CLOSE
        self.floor_num = 1

    def draw(self):
        self.image.clip_draw(0, self.state * self.height, self.width, self.height,
                             self.x - self.move_x, self.y - self.move_y)
        self.draw_bb()
        pass


    def moveX(self, dir):
        self.move_x += dir
        pass

    def moveY(self, dir):
        self.move_y += dir


    def open_box(self):
        self.state = self.OPEN
        pass


    def get_bb(self):
        return  self.x - self.width /2 - self.move_x,\
                 self.y - self.height / 2 - self.move_y,\
                 self.x + self.width / 2  - self.move_x,\
                 self.y + self.height / 2 - self.move_y


    def get_point(self):
        return self.x , self.y - self.height / 2

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


