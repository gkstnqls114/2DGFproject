import json
import os
import random
from pico2d import *

from play import Game

name = "Guard"

class Guard:
    font = None
    image = None

    #FRAME
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 50.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    # 한번 액션하는데 걸리는 시간 , 초
    TIME_PER_ACTION = 0.5

    # 액션 속도
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAME_PER_ACTION = 1

    #ANIMAITON
    ANI_STAND = 0
    ANI_RIGHT = 1
    ANI_LEFT = 2
    ANI_STAIRS_MOVE_UP = 3
    ANI_STAIRS_MOVE_DOWN = 4

    def __init__(self):
        if Guard.image == None:
            Guard.image = load_image('Image/샘플 경비원.png')
        if Guard.font == None:
            Guard.font = load_font('ENCR10B.TTF',16)

        self.name = None
        self.width = 70
        self.height = 90
        self.x = 500
        self.y = 50 + 85
        self.Map_x = self.x
        self.Map_y = self.y
        self.move_x = 0
        self.move_y = 0

        self.frame = 0
        self.total_frames =0.0
        self.dir = 5

        #움직임 bool
        self.Run = False
        self.Right = False
        self.Left = True
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

        #경비원 담당 플로어
        self.floor_num = 1
        #플레이어를 인식한 시간
        # 0 되면 다시 리셋
        self.SeePlayerTime = 1000
        #플레이어의 상태
        self.playerState = -1
        self.playerFloor = -1

        self.runningTime = 0
        self.pause = (self.x, self.y, self.frame, self.dir)

    def update(self, frame_time):
        distance = Guard.RUN_SPEED_PPS * frame_time
        self.total_frames += \
            Guard.FRAME_PER_ACTION * Guard.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 1

        self.runningFunc()

        if(self.SeePlayer):
            self.follow_player()
            pass
        else:
            if(self.Map_x + self.width / 2 > 1600):
                self.Right = False
                self.Left = True

            if (self.Map_x - self.width / 2 < 0):
                self.Right = True
                self.Left = False


        if (self.Up):
            self.move_y += self.dir
            self.move_x += self.dir
            self.Map_x += self.dir
            self.Map_y += self.dir
        if (self.Down):
            self.move_y -= self.dir
            self.move_x -= self.dir
            self.Map_x += self.dir
            self.Map_y += self.dir

        if(self.Up or self.Down): return
        if (self.Right):
            self.move_x += self.dir
            self.Map_x += self.dir
        if (self.Left):
            self.move_x -= self.dir
            self.Map_x -= self.dir


    def moveX(self, dir):
        self.move_x += dir
        pass

    def moveY(self, dir):
        self.move_y += dir
        pass



    def follow_player(self):
        # 쫓아간다
        self.dir = 5
        self.SeePlayerTime -= 1

        player = Game.player

        if (self.playerState == self.ANI_RIGHT):
            self.Right = True
            self.Left = False
        elif (self.playerState == self.ANI_LEFT):
            self.Right = False
            self.Left = True
        elif (self.playerState == self.ANI_STAIRS_MOVE_UP):
            stairs = Game.stairs

            pass
        elif (self.playerState == self.ANI_STAIRS_MOVE_DOWN):
            stairs = Game.stairs

            pass

        if (self.Map_x + self.width / 2 > 1600):
            self.playerState = self.ANI_LEFT

        if (self.Map_x - self.width / 2 < 0):
            self.playerState = self.ANI_RIGHT

        if (self.SeePlayerTime == 0):
            self.SeePlayerTime = 1000
            self.SeePlayer = False
        pass

    def draw(self):
        #self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        self.image.draw( self.x + self.move_x, self.y + self.move_y)

        self.draw_bb()

        if(self.SeePlayer):
            Guard.font.draw(self.x + self.move_x - 35 ,
                            self.y + self.move_y + 50, 'Time %d' %(self.SeePlayerTime))
        else:
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
        return  self.x - self.width /2 + self.move_x,\
                 self.y - self.height / 2 + self.move_y,\
                 self.x + self.width / 2  + self.move_x,\
                 self.y + self.height / 2 + self.move_y
        pass

    def get_see_bb(self):
        if(self.Right or self.Up):
            return self.get_right_bb()
        elif self.Left or self.Down:
            return self.get_left_bb()

        pass

    def get_right_bb(self):
        return  self.x - self.width /2 + 20 + self.move_x,\
                 self.y - self.height / 2 + self.move_y,\
                 self.x + self.width + 100  + self.move_x,\
                 self.y + self.height / 2 + self.move_y
        pass

    def get_left_bb(self):
        return  self.x - self.width - 100 + self.move_x,\
                 self.y - self.height / 2 + self.move_y,\
                 self.x + self.width / 2 - 20  + self.move_x,\
                 self.y + self.height / 2 + self.move_y
        pass

    def get_point(self):
        return self.Map_x , self.Map_y - self.height / 2


    def get_point_x(self):
        #pivot return

        return self.Map_x
        pass

    def get_point_y(self):
        return self.Map_y - self.height / 2
        pass

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
        draw_rectangle(*self.get_see_bb())
        pass



