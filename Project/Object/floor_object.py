import json
import os
import random
from pico2d import *

class Floor:
    def __init__(self, y, floor_num):

        self.image = load_image('샘플 바닥.png')
        self.width = 800
        self.height = 90
        self.x = self.width / 2
        self.y = y + self.height / 2
        self.move_x = 0
        self.move_y = 0
        self.floor_num = floor_num

    def draw(self):
        self.image.draw(self.x - self.move_x, self.y - self.move_y,self.width, self.height)

