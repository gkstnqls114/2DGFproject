import json
import os
import random
from pico2d import *



name = "Floor"

class Floor:
    def __init__(self, bg):
        self.name = None
        self.image = load_image('Image/Floor.png')
        self.width = self.image.w
        self.height = self.image.h
        self.x = self.width / 2
        self.y =  90 + self.height / 2
        self.move_x = 0
        self.move_y = 0
        self.floor_num = 1

        self.background = bg


    def update(self, frame_time):
        self.y = clamp(0,
                      self.y,
                      self.background.height)

        self.x = clamp(0,
                       self.x,
                       self.background.width)

    def draw(self):
        self.image.draw( self.x - self.background.window_left,
                         self.y - self.background.window_bottom)

