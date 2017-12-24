import json
import os
import random
from pico2d import *


name = "Button"

class Button:

    #ANIMAITON
    ANI_A_GET_TREASURE = 0
    ANI_S_AVOID_GUARD = 1
    ANI_CAN_MOVE_DOWN = 2
    ANI_CAN_MOVE_UP = 3
    ANI_NOTHING = 4

    def __init__(self, bg):
        self.name = None
        self.image = load_image('Image/Sprite/Button_sprite.png')
        self.width = self.image.w
        self.height = 50
        self.x = self.width / 2
        self.y = self.height / 2
        self.state = self.ANI_NOTHING

        self.background = bg

    def set_player(self, player):
        self.player = player

    def update(self, frame_time):
        if self.player.Stairs_Can_Down:
            self.state = self.ANI_CAN_MOVE_DOWN
        elif self.player.Stairs_Can_Up:
            self.state = self.ANI_CAN_MOVE_UP
        elif self.player.Treasure_Can_Open:
            self.state = self.ANI_A_GET_TREASURE
        elif self.player.Aressted :
            self.state = self.ANI_S_AVOID_GUARD
        else:
            self.state = self.ANI_NOTHING

        self.x = self.player.x
        self.y = self.player.y + self.height/2 + self.player.height/2 + 10


    def draw(self):
        self.image.clip_draw(0, self.state * self.height,\
                             self.width, self.height, \
                             self.x - self.background.window_left,\
                             self.y - self.background.window_bottom)

