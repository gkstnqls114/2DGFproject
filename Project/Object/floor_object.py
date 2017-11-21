import json
import os
import random
from pico2d import *



name = "Floor"

class Floor:
    def __init__(self):
        self.name = None
        self.image = load_image('샘플 바닥.png')
        self.width = 800
        self.height = 90
        self.x = self.width / 2
        self.y =  90 + self.height / 2
        self.move_x = 0
        self.move_y = 0
        self.floor_num = 1

    def draw(self):
        self.image.draw(self.x - self.move_x, self.y - self.move_y,self.width, self.height)

    def moveX(self, dir):
        self.move_x += dir
        pass

    def moveY(self, dir):
        self.move_y += dir

