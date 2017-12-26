import json
import os
import random
from pico2d import *

from play import Game

name = "Guard"

class Guard:
    font = None
    image = None
    bump_image = None
    icon = None
    time_image = None
    hp_image = None
    light_image = None

    #FRAME
    PIXEL_PER_METER = (10.0 / 0.16)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    # 한번 액션하는데 걸리는 시간 , 초
    TIME_PER_ACTION = 0.5

    # 액션 속도
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

    #ANIMAITON
    ANI_RIGHT = 0
    ANI_LEFT = 1
    ANI_BLACKOUT_RIGHT = 2
    ANI_BLACKOUT_LEFT = 3

    MaxHp = 10.0
    MaxSeeTime = 300

    def __init__(self, bg):
        if Guard.image == None:
            Guard.image = load_image('Image/Sprite/guard_sprite.png')
        if Guard.bump_image == None:
            Guard.bump_image = load_image('Image/Sprite/bump_sprite.png')
        if Guard.icon == None:
            Guard.icon = load_image('Image/guard see player.png')
        if Guard.hp_image == None:
            Guard.hp_image = load_image('Image/guard_hp.png')
        if Guard.time_image == None:
            Guard.time_image = load_image('Image/guard_time.png')
        if Guard.light_image == None:
            Guard.light_image = load_image('Image/Sprite/guard_light_sprite.png')

        self.background = bg


        self.name = None
        self.width = 90
        self.height = 110
        self.x = 500
        self.y = 50 + 85

        self.FRAME_PER_ACTION = 2

        self.frame = 0
        self.total_frames =0.0
        self.dir = 5

        #움직임 bool
        self.state = self.ANI_RIGHT
        self.Run = False
        self.Right = False
        self.Left = True
        self.Up = False
        self.Down = False

        #인식했는가 아닌가
        self.SeePlayer = False
        self.PrevPlayerState = -1
        self.SeePlayerChange = False
        self.Hp = 10.0
        self.BlackOut = False

        self.Arresting = False

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
        self.SeePlayerTime = self.MaxSeeTime

        #플레이어의 상태
        self.playerState = -1
        self.playerFloor = -1

        self.runningTime = 0

    def MoveInBackground(self):
        min_y = 0
        self.y = clamp(min_y,
                       self.y,
                       self.background.height)
        min_x = 0
        self.x = clamp(min_x,
                       self.x,
                       self.background.width)

    def update(self, frame_time):

        if(self.Hp <= 0):
            self.BlackOut = True

        if(self.BlackOut):
            if self.state == self.ANI_RIGHT:
                self.state = self.ANI_BLACKOUT_RIGHT
                self.width = 110
                self.frame = 0
            elif self.state == self.ANI_LEFT:
                self.state = self.ANI_BLACKOUT_LEFT
                self.width = 110
                self.frame = 0

            self.Hp += 0.1
            self.Arresting = False

            if self.Hp >= self.MaxHp:
                if self.state == self.ANI_BLACKOUT_RIGHT:
                    self.state = self.ANI_RIGHT
                elif self.state == self.ANI_BLACKOUT_LEFT:
                    self.state = self.ANI_LEFT

                self.BlackOut = False
                self.Hp = self.MaxHp
                self.width = 90
            return

        self.runningFunc()

        distance = Guard.RUN_SPEED_PPS * frame_time
        self.total_frames += \
            self.FRAME_PER_ACTION * Guard.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 8

        if(self.SeePlayer):
            self.Run = True
            self.follow_player()
            pass
        else:
            self.Run = False
            if(self.x + self.width / 2 > self.background.width):
                self.Right = False
                self.Left = True

            if (self.x - self.width / 2 < 0):
                self.Right = True
                self.Left = False

        if (self.Right):
            self.state = self.ANI_RIGHT
            self.x += self.dir
        if (self.Left):
            self.state = self.ANI_LEFT
            self.x -= self.dir

        self.MoveInBackground()


    def follow_player(self):
        # 쫓아간다
        self.SeePlayerTime -= 1

        if (self.SeePlayerTime <= 0):
            self.SeePlayerTime = 0
            self.SeePlayer = False

        if self.x + self.width / 2 > 1600:
            self.playerState = self.ANI_LEFT
            self.Right = False
            self.Left = True
        if (self.x - self.width / 2 < 0):
            self.playerState = self.ANI_RIGHT
            self.Right = True
            self.Left = False

        player = Game.player
        if player.Stairs_Move: return

        if (self.playerState == self.ANI_RIGHT):
            self.Right = True
            self.Left = False
        elif (self.playerState == self.ANI_LEFT):
            self.Right = False
            self.Left = True

        pass

    def draw(self):
        if not self.Arresting:
            if self.state == self.ANI_RIGHT:
                self.light_image.opacify(0.5)
                self.light_image.clip_draw(self.frame * 235, self.state * 110,\
                            235, 110,\
                            self.x - self.background.window_left + self.width / 2 + 30,\
                             self.y - self.background.window_bottom)
            elif self.state == self.ANI_LEFT:
                self.light_image.opacify(0.5)
                self.light_image.clip_draw(self.frame * 235, self.state * 110,\
                            235, 110,\
                            self.x - self.background.window_left - self.width / 2 - 30,\
                             self.y - self.background.window_bottom)

            self.image.clip_draw(self.frame * self.width, self.state * self.height,\
                             self.width, self.height, \
                             self.x - self.background.window_left,\
                             self.y - self.background.window_bottom)
        else:
            self.bump_image.clip_draw(self.frame * 120, 0,\
                             120, 120, \
                             self.x - self.background.window_left,\
                             self.y - self.background.window_bottom)
            self.hp_image.draw(self.x - self.background.window_left,
                                self.y - self.background.window_bottom - self.height / 2 - 10,
                               (self.Hp) * 9, 10)


        if(self.SeePlayer):
            if not self.Arresting:
                self.icon.draw(self.x - self.background.window_left,
                           self.y - self.background.window_bottom + self.height / 2 + 25)

            if self.BlackOut:
                self.hp_image.draw(self.x - self.background.window_left,
                                self.y - self.background.window_bottom - self.height / 2 - 10,
                               (self.Hp) * 9, 10)
            elif self.Arresting == False:
                 self.time_image.draw(self.x - self.background.window_left,
                                     self.y - self.background.window_bottom - self.height / 2 - 10,
                                     self.SeePlayerTime / self.MaxSeeTime * 90, 10)
        else:
            pass


    def runningFunc(self):
        if self.Run:
            self.dir = 7
            self.FRAME_PER_ACTION = 4
        else:
            self.dir = 3
            self.FRAME_PER_ACTION = 2.5

    def get_bb(self):
        return  self.x  - self.background.window_left- self.width /2 ,\
                 self.y  - self.background.window_bottom- self.height / 2,\
                 self.x  - self.background.window_left+ self.width / 2,\
                 self.y  - self.background.window_bottom+ self.height / 2
        pass

    def get_see_bb(self):
        if(self.Right or self.Up):
            return self.get_right_bb()
        elif self.Left or self.Down:
            return self.get_left_bb()

        pass

    def get_right_bb(self):
        return  self.x  - self.background.window_left - self.width /2 + 20 ,\
                 self.y  - self.background.window_bottom- self.height / 2 ,\
                 self.x  - self.background.window_left+ self.width + 100,\
                 self.y  - self.background.window_bottom + self.height / 2
        pass

    def get_left_bb(self):
        return  self.x - self.background.window_left- self.width - 100 ,\
                 self.y  - self.background.window_bottom - self.height / 2 ,\
                 self.x  - self.background.window_left+ self.width / 2 - 20 ,\
                 self.y - self.background.window_bottom + self.height / 2
        pass

    def get_point(self):
        return self.x - self.background.window_left , self.y - self.background.window_bottom


    def get_point_x(self):
        return self.x - self.background.window_left
        pass

    def get_point_y(self):
        return self.y - self.background.window_bottom
        pass

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
        draw_rectangle(*self.get_see_bb())
        pass



