import json
import os
import random
from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('Image/Background.png')

        self.speed = 0
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.width = self.image.w
        self.height = self.image.h

        self.window_left = 0
        self.window_bottom = 0

    def set_center_object(self, player):
        self.center_object = player
        pass

    def draw(self):
        # fill here
        self.image.clip_draw_to_origin(
            self.window_left, self.window_bottom,
            self.canvas_width, self.canvas_height,
            0, 0
        )

    def update(self, frame_time):
        # fill here
        #print("배경 업데이트")
        #pr#int(int(self.center_object.x) - self.canvas_width//2, " ", int(self.center_object.y) - self.canvas_height//2)
        self.window_left = clamp (0,
                                  int(self.center_object.x) - self.canvas_width//2,
                                  self.width - self.canvas_width
                                  )
        self.window_bottom = clamp(0,
                                   int(self.center_object.y) - self.canvas_height//2,
                                   self.height - self.canvas_height
                                   )


