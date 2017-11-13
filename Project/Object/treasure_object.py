import json
import os
import random
from pico2d import *

class Treasure:
    def __init__(self, y, floor_num):

        self.image = load_image('샘플 바닥.png')
        self.width = 800
        self.height = 90
        self.x = self.width / 2
        self.y = y + self.height / 2
        self.floor_num = floor_num

    def draw(self):
        self.image.draw(self.x, self.y ,self.width, self.height)

