import json
import os
import random
from pico2d import *


name = "Stairs"



class Stairs:
    def __init__(self):
        self.x, self.y = 300, 125 + 110
        self.move_x = 0
        self.move_y = 0
        self.image = load_image('샘플 계단2.png')
        self.width = 300
        self.height = 300

    def update(self):
        pass

    def draw(self):
        self.image.draw( self.x - self.move_x, self.y - self.move_y, self.width, self.height)
        self.draw_bb()

    def get_bottom_bb(self):
        bottom_x = self.x - self.width / 2 - self.move_x
        bottom_y = self.y - self.height / 2 - self.move_y

        return bottom_x - 30, bottom_y - 30, bottom_x + 30, bottom_y + 30
        pass

    def get_bottom_point(self):

        bottom_x = self.x - self.width / 2 - self.move_x
        bottom_y = self.y - self.height / 2 - self.move_y

        return bottom_x, bottom_y

    def get_top_bb(self):
        bottom_x = self.x + self.width / 2 - self.move_x
        bottom_y = self.y + self.height / 2 - self.move_y

        return bottom_x - 30, bottom_y - 30, bottom_x + 30, bottom_y + 30
        pass

    def get_top_point(self):
        bottom_x = self.x + self.width / 2 - self.move_x
        bottom_y = self.y + self.height / 2 - self.move_y

        return bottom_x, bottom_y

    def draw_bb(self):
        draw_rectangle(*self.get_bottom_bb())
        draw_rectangle(*self.get_top_bb())






