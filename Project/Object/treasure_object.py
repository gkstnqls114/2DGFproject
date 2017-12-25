import json
import os
import random
from pico2d import *

class Treasure:
    image = None

    CLOSE, OPEN = 0, 1
    BOX, ART, JEWEL, SCULPTURE = 0, 1, 2, 3

    def __init__(self, bg):
        if(self.image == None):
            self.image = load_image('Image/Sprite/treasure_sprite.png')
        self.background = bg

        #상대적인 카메라 위치
        self.x = 0
        self.y = 0
        self.state = self.CLOSE
        self.floor_num = 1

        treasure_data_file = open('Data/treasure_object_data.txt', 'r')
        treasure_data = json.load(treasure_data_file)
        treasure_data_file.close()

        self.sort = random.randrange(0,2)

        if (self.sort == self.BOX):
            self.width = treasure_data["BOX"]["width"]
            self.height = treasure_data["BOX"]["height"]
            self.sprite_height = 0

        if (self.sort == self.ART):
            self.width = treasure_data["ART"]["width"]
            self.height = treasure_data["ART"]["height"]
            self.sprite_height = treasure_data["BOX"]["width"]

        if (self.sort == self.JEWEL):
            self.width = 120
            self.height = 120

        if (self.sort == self.SCULPTURE):
            self.width = 120
            self.height = 120




    def draw(self):

        self.image.clip_draw(self.state * self.width , self.sprite_height
                             , self.width, self.height,
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


