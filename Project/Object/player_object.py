import json
import os
import random
from pico2d import *

from Property import coordination
from Property import anistate

name = "Player"


class Player:
    font = None
    position_font = None
    treasure_font = None
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
    FRAME_PER_ACTION = 2

    #ANIMAITON
    ANI_STAND = 0
    ANI_RIGHT = 1
    ANI_LEFT = 2
    ANI_STAIRS_MOVE_UP = 3
    ANI_STAIRS_MOVE_DOWN = 4
    ANI_CHANGE = 5

    def __init__(self):
        if Player.image == None:
            Player.image = load_image('2Dplayer_sprite_2.png')
        if Player.font == None:
            Player.font = load_font('ENCR10B.TTF',16)
        if Player.position_font == None:
            Player.position_font = load_font('ENCR10B.TTF', 16)
        if Player.treasure_font == None:
            Player.treasure_font = load_font('ENCR10B.TTF', 16)

        self.width = 90
        self.height = 110

        #플레이어 카메라상 좌표
        #self.XY = coordination.Coordination(100, 50 + 90)
        self.x = 100
        self.y = 50 + 90


        #플레이어 맵상 좌표
        self.Map_x = self.x
        self.Map_y = self.y

        self.frame = 0
        self.dir = 4
        self.state = 0

        self.total_frames = 0.0


        #움직임 bool
        self.Run = False
        self.Right = False
        self.Left = False
        self.Up = False
        self.Down = False

        #계단의 bottom, top 좌표
        self.stairPoint = list()

        #계단을 올라 가는 bool
        self.Stairs_Can_Up = False
        self.Stairs_Can_Down = False
        self.Stairs_Move = False

        #보물상자 터는 bool
        self.Treasure_Can_Open = False
        self.Treasure_Search = False
        self.treasure_num = 0
        # 은신술
        self.Change = False

        #현재 플레이어가 있는 플로어
        self.floor_at_present = 1

        self.runningTime = 0
        #self.pause = (self.x, self.y, self.frame, self.dir)

    def showstairPoint(self):
        if(len(self.stairPoint) == 0):
            print("없다")
            return

        print("top, bottom: ")

        print("%d %d, %d %d"
                  %(self.stairPoint[0],
                    self.stairPoint[1],
                    self.stairPoint[2],
                    self.stairPoint[3]))
        pass

    def update(self, frame_time):
        if(self.Change):
            self.state = self.ANI_CHANGE
            return

        distance = Player.RUN_SPEED_PPS * frame_time
        self.total_frames += \
            Player.FRAME_PER_ACTION * Player.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 2

        self.runningFunc()

        wall_last = 1600
        if(self.Map_x + self.width / 2 > wall_last):
            self.x = 800 - self.width / 2
            self.Map_x = 1600 - self.width / 2
            print("안돼", self.Map_x, "   ", self.x)
            return

        wall_first = 0
        if (self.Map_x - self.width / 2 < wall_first):
            self.x = 0 + self.width / 2
            self.Map_x = 0 + self.width / 2
            print("안돼", self.Map_x, "   ", self.x)
            return

        if(self.Up):
            self.state = self.ANI_STAIRS_MOVE_UP
            self.y += self.dir
            self.x += self.dir
            self.Map_x += self.dir
            self.Map_y += self.dir
        if (self.Down):
            self.state = self.ANI_STAIRS_MOVE_DOWN
            self.y -= self.dir
            self.x -= self.dir
            self.Map_x -= self.dir
            self.Map_y -= self.dir

        if(self.Stairs_Move): return
        if (self.Right):
            self.state = self.ANI_RIGHT
            self.x += self.dir
            self.Map_x += self.dir
        if (self.Left):
            self.state = self.ANI_LEFT
            self.x -= self.dir
            self.Map_x -= self.dir

    def draw(self):
        self.image.clip_draw(self.frame * self.width, self.state * self.height,\
                             self.width, self.height,\
                             self.x , self.y)
        #self.image.draw( self.x, self.y)
        self.draw_bb()

        if(self.Stairs_Can_Up):
            Player.font.draw(self.x - 35, self.y + 50, 'Can_Up')
        elif(self.Stairs_Can_Down):
            Player.font.draw(self.x - 35, self.y + 50, 'Can_Down')
        elif( self.Stairs_Move):
            Player.font.draw(self.x - 35 , self.y + 50, 'Stairs_Move')
        elif (self.Treasure_Can_Open):
            Player.font.draw(self.x - 35 , self.y + 50, 'Treasure_Can_Open')


        Player.position_font.draw(self.x - 50, self.y -60, "FLOOR: %d" %(self.floor_at_present))
        Player.treasure_font.draw(self.x - 50, self.y - 80, "Get: %d" %(self.treasure_num))
        #print(self.x , " , " , self.y , " , " ,  self.Map_x , " , ", self.Map_y)



    def handle_events(self, event):
            # key down


        if event.type == SDL_KEYDOWN:
            a = 97
            z = 122 #달리기
            x = 120 #둔갑술
            if event.key == z :
                self.Run = True
            if event.key == x:
                if(self.state != self.ANI_STAND): return
                self.Change = True
            elif event.key == a:
                if not self.Treasure_Can_Open:return
                self.Treasure_Can_Open = False
                self.Treasure_Search = True
            elif event.key == SDLK_RIGHT:
                if self.Stairs_Move: return
                if self.Change: return
                self.Right = True
                self.state = self.ANI_RIGHT
            elif  event.key == SDLK_LEFT:
                if self.Stairs_Move: return
                if self.Change: return
                self.Left = True
                self.state = self.ANI_LEFT

            if event.key == SDLK_UP and self.Stairs_Can_Up:
                if (self.Change): return
                self.x = self.stairPoint[2]
                self.y = self.stairPoint[3]
                self.y += self.height / 2
                self.stairs_up()
                self.state = self.ANI_STAND
                self.floor_at_present +=1
            elif event.key == SDLK_UP and self.Stairs_Move:
                if (self.Change): return
                if (self.state == self.ANI_STAIRS_MOVE_DOWN):
                    self.floor_at_present += 1
                self.stairs_move_up()
                self.state = self.ANI_STAIRS_MOVE_UP
            elif event.key == SDLK_DOWN and self.Stairs_Can_Down:
                if (self.Change): return
                self.x = self.stairPoint[0]
                self.y = self.stairPoint[1]
                self.y += self.height / 2
                self.stairs_down()
                self.state = self.ANI_STAND
                self.floor_at_present -= 1
            elif event.key == SDLK_DOWN and self.Stairs_Move:
                if (self.Change): return
                if(self.state == self.ANI_STAIRS_MOVE_UP):
                    self.floor_at_present -= 1
                self.stairs_move_down()
                self.state = self.ANI_STAIRS_MOVE_DOWN

        # key up
        if event.type == SDL_KEYUP:
            z = 122
            x = 120
            if event.key == z:
                self.Run = False
            if event.key == x:
                if self.Stairs_Move: return
                self.Change = False
                self.state = self.ANI_STAND
            elif event.key == SDLK_RIGHT:
                if self.Stairs_Move: return
                self.state = self.ANI_STAND
                self.Right = False
            elif  event.key == SDLK_LEFT:
                if self.Stairs_Move: return
                self.state = self.ANI_STAND
                self.Left = False
            elif event.key == SDLK_UP:
                self.Up = False
            elif event.key ==SDLK_DOWN:
                self.Down = False


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
            self.dir = 10

        else:
            self.dir = 5


    def get_bb(self):
        left_player = self.x - self.width / 2
        bottom_player = self.y - self.height /2
        right_player = self.x + self.width / 2
        top_player = self.y + self.width / 2
        return left_player, bottom_player, right_player, top_player

    def get_point(self):
        #pivot return
        pivot_x = self.x
        pivot_y = self.y - self.height / 2
        return pivot_x, pivot_y


    def get_pointX(self):
        #pivot return
        pivot_x = self.x
        return pivot_x

    def get_pointY(self):
        #pivot return
        pivot_y = self.y - self.height / 2
        return pivot_y

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def Set_stairsPoint(self, top, bottom):
        if(len(self.stairPoint) == 4):
            self.Reset_stairsPoint()

        #val은 튜플로 받는다
        topX = top[0]
        topY = top[1]
        bottomX = bottom[0]
        bottomY = bottom[1]
        self.stairPoint.append(topX)
        self.stairPoint.append(topY)
        self.stairPoint.append(bottomX)
        self.stairPoint.append(bottomY)
        #내가 원하는 것
        #stairPoint = [topX, topY, bottomX, bottomY]

        pass

    def Reset_stairsPoint(self):
        #나중에 수정
        if(len(self.stairPoint) != 4):
            print("오류")
            return

        self.stairPoint.pop()
        self.stairPoint.pop()
        self.stairPoint.pop()
        self.stairPoint.pop()

        pass

    def Reach_Top(self):

        if not self.Stairs_Move: return False
        if not self.Up: return False

        print ("%d < %d" %(self.get_pointX(), self.stairPoint[0]))
        print ("%d < %d" % (self.get_pointY(), self.stairPoint[1]))

        if self.get_pointX() < self.stairPoint[0]: return False
        if self.get_pointY() < self.stairPoint[1]: return False


        return True

        pass

    def Reach_Bottom(self):
        if not self.Stairs_Move: return False
        if not self.Down: return False
        if self.get_pointX() > self.stairPoint[2]: return False
        if self.get_pointY() > self.stairPoint[3]: return False

        return True

        pass

