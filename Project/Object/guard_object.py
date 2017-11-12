import json
import os
import random
from pico2d import *


name = "Guard"

class Guard:
    font = None
    position_font = None
    image = None
    def __init__(self):
        if Guard.image == None:
            Guard.image = load_image('샘플 경비원.png')
        if Guard.font == None:
            Guard.font = load_font('ENCR10B.TTF',16)

        self.width = 70
        self.height = 90
        self.x = 0
        self.y = 50 + 85

        self.frame = 0
        self.dir = 1

        #움직임 bool
        self.Run = False
        self.Right = False
        self.Left = False
        self.Up = False
        self.Down = False

        #인식했는가 아닌가
        self.SeePlayer = False

        #계단을 올라 가는 bool
        self.top_range = 0
        self.bottom_range = 0
        self.Stairs_Can_Up = False
        self.Stairs_Can_Down = False
        self.Stairs_Move = False

        #현재 경비원이 있는 플로어
        self.floor_at_present = 1

        self.runningTime = 0
        self.pause = (self.x, self.y, self.frame, self.dir)

    def update(self):
        self.frame = (self.frame + 1) % 8

        self.runningFunc()

        if(self.SeePlayer):
            pass


    def draw(self):
        #self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        self.image.draw( self.x, self.y)
        self.draw_bb()

        if(self.Stairs_Can_Up):
            Guard.font.draw(self.x - 35, self.y + 50, 'Can_Up')
        elif(self.Stairs_Can_Down):
            Guard.font.draw(self.x - 35, self.y + 50, 'Can_Down')
        elif( self.Stairs_Move):
            Guard.font.draw(self.x - 35 , self.y + 50, 'Stairs_Move')

        #Guard.position_font.draw(self.x - 50, self.y -50, 'X: %d, Y: %d' % (self.x, self.y))

    def handle_events(self, event):
            # key down
        pass

    def stairs_up(self):
        self.Stairs_Can_Up = False
        self.Stairs_Move = True
        self.Right = False
        self.Left = False
        self.Up = True
        self.Down = False

        pass

    def stairs_down(self):
        self.Stairs_Can_Down = False
        self.Stairs_Move = True
        self.Right = False
        self.Left = False
        self.Up = False
        self.Down = True

    def stairs_move_down(self):
        self.Stairs_Can_Down = False
        self.Stairs_Move = True
        self.Right = False
        self.Left = False
        self.Down = True
        self.Up = False

    def stairs_move_up(self):
        self.Stairs_Can_Down = False
        self.Stairs_Move = True
        self.Right = False
        self.Left = False
        self.Down = False
        self.Up = True

    def runningFunc(self):
        if self.Run:
            self.dir = 3

        else:
            self.dir = 1




    def get_bb(self):
        return self.x - self.width / 2, self.y -self.height/ 2, self.x + self.width/2, self.y + self.width / 2
        pass


    def get_point(self):
        return self.x , self.y - self.height / 2

    def get_point_x(self):
        #pivot return

        return self.x
        pass

    def get_point_y(self):
        # pivot return

        return self.y - 45
        pass

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

