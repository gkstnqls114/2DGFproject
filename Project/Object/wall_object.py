import json
import os
import random
from pico2d import *

class Wall:
    def __init__(self):

        self.image = load_image('Image/샘플 벽.png')
        self.width = 1600
        self.height = 880
        self.x = self.width / 2
        self.y = self.height / 2
        self.move_x = 0
        self.move_y = 0

    def draw(self):
        self.image.draw(self.x - self.move_x, self.y - self.move_y)

