import json
import os
import random
from pico2d import *


name = "Stairs"


class Stairs:
    image = None

    def __init__(self):
        if self.image == None:
            self.image = load_image('Image/2Dstairs_2.png')

        self.name = None
        self.x = 300
        self.y = 125 + 110
        self.move_x = 0
        self.move_y = 0
        self.width = 300
        self.height = 300
        self.flooar_num = 1

    def update(self):
        pass

    def draw(self):
        self.image.draw( self.x - self.move_x, self.y - self.move_y, self.width, self.height)
        self.draw_bb()


    def moveX(self, dir):
        self.move_x += dir

    def moveY(self, dir):
        self.move_y += dir

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
        top_x = self.x + self.width / 2 - self.move_x
        top_y = self.y + self.height / 2 - self.move_y

        #print ("top X Y : %d %d" %(top_x, top_y))

        return top_x - 30, top_y - 30, top_x + 30, top_y + 30
        pass

    def get_top_point(self):
        top_x = self.x + self.width / 2 - self.move_x
        top_y = self.y + self.height / 2 - self.move_y

        return top_x, top_y

    def draw_bb(self):
        draw_rectangle(*self.get_bottom_bb())
        draw_rectangle(*self.get_top_bb())






