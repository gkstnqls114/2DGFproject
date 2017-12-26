import json
import os
import random
from pico2d import *

from Object import button_object


from Framwork import game_framework
from Scene import clear_state
from Scene import askpause_state

name = "Player"

class Player:
    font = None
    treasure_font = None
    image = None

    #FRAME
    PIXEL_PER_METER = (10.0 / 0.16)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 50.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    # 한번 액션하는데 걸리는 시간 , 초
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION


    #ANIMAITON
    ANI_STAND = 0
    ANI_RIGHT = 1
    ANI_LEFT = 2
    ANI_STAIRS_MOVE_UP = 3
    ANI_STAIRS_MOVE_DOWN = 4
    ANI_CHANGE = 5

    def __init__(self, bg):
        if Player.image == None:
            Player.image = load_image('Image/Sprite/2Dplayer_sprite.png')
        if Player.font == None:
            Player.font = load_font('ENCR10B.TTF',16)
        if Player.treasure_font == None:
            Player.treasure_font = load_font('ENCR10B.TTF', 16)

        self.button = button_object.Button(bg)
        self.button.set_player(self)

        self.background = bg
        self.background.set_center_object(self)

        self.width = 90
        self.height = 110

        # 액션 속도
        self.FRAME_PER_ACTION = 1

        #플레이어 카메라상 좌표
        self.x = 100
        self.y = self.height/2 + 100

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

        #문을 연다
        self.Door_Can_Open = False

        # 은신술
        self.Change = False

        #경비병에게 잡혔다
        self.Aressted = False

       #현재 플레이어가 있는 플로어
        self.floor_at_present = 1

        self.runningTime = 0
        #self.pause = (self.x, self.y, self.frame, self.dir)


    def MoveInBackground(self):
        self.y = clamp(0,
                       self.y,
                       self.background.height)
        self.x = clamp(self.width / 2,
                       self.x,
                       self.background.width - self.width /2)


    def ask_game_clear(self):
        game_framework.push_state(askpause_state)

    def update(self, frame_time):
        if(self.Change):
            self.state = self.ANI_CHANGE
            return

        distance = Player.RUN_SPEED_PPS * frame_time
        self.total_frames += \
            self.FRAME_PER_ACTION * Player.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 8

        self.runningFunc()

        self.MoveInBackground()

        self.button.update(frame_time)

        if (self.Aressted == True):
            return

        if(self.Up):
            self.state = self.ANI_STAIRS_MOVE_UP
            self.y += self.dir
            self.x += self.dir

        if (self.Down):
            self.state = self.ANI_STAIRS_MOVE_DOWN
            self.y -= self.dir
            self.x -= self.dir

        if(self.Stairs_Move): return
        if (self.Right):
            self.state = self.ANI_RIGHT
            self.x += self.dir

        if (self.Left):
            self.state = self.ANI_LEFT
            self.x -= self.dir

        self.button.update(frame_time)

    def draw(self):
        self.button.draw()
        if not self.Aressted:
            self.image.clip_draw(self.frame * self.width, self.state * self.height,\
                             self.width, self.height, \
                             self.x - self.background.window_left,\
                             self.y - self.background.window_bottom)
        else:
            pass

        self.draw_bb()

        Player.treasure_font.draw(self.background.canvas_width - 150, self.background.canvas_height - 100, "Get: %d" %(self.treasure_num))


    def ArrestGuard(self, guard):
        self.guard = guard


    def handle_events(self, event):
            # key down


        if event.type == SDL_KEYDOWN:
            a = 97 #아이템 얻기
            z = 122 #달리기
            x = 120 #둔갑술
            s = 115 #도망가기
            if event.key == z :
                if (self.Aressted == True): return
                self.Run = True

            if event.key == x:
                if(self.Aressted == True) : return
                if(self.state != self.ANI_STAND): return
                self.Change = True

            elif event.key == a:
                if (self.Aressted == True): return
                if not self.Treasure_Can_Open:return
                self.Treasure_Can_Open = False
                self.Treasure_Search = True

            elif event.key == s:
                if (self.Aressted == False): return
                self.guard.Hp -= 1
                if(self.guard.Hp <= 0):
                    self.Aressted = False

            elif event.key == SDLK_RIGHT:
                if (self.Aressted == True): return
                if self.Stairs_Move: return
                if self.Change: return
                self.Right = True
                self.state = self.ANI_RIGHT

            elif  event.key == SDLK_LEFT:
                if (self.Aressted == True): return
                if self.Stairs_Move: return
                if self.Change: return
                self.Left = True
                self.state = self.ANI_LEFT

            if event.key == SDLK_UP and self.Door_Can_Open:
                if (self.Aressted == True): return
                if (self.Change): return
                self.ask_game_clear()

            if event.key == SDLK_UP and self.Stairs_Can_Up:
                if (self.Aressted == True): return
                if (self.Change): return
                self.x = self.stairPoint[2]
                self.y = self.stairPoint[3]
                self.y += self.height / 2
                self.stairs_up()
                self.state = self.ANI_STAND
                self.floor_at_present +=1

            elif event.key == SDLK_UP and self.Stairs_Move:
                if (self.Aressted == True): return
                if (self.Change): return
                if (self.state == self.ANI_STAIRS_MOVE_DOWN):
                    self.floor_at_present += 1
                self.stairs_move_up()
                self.state = self.ANI_STAIRS_MOVE_UP

            elif event.key == SDLK_DOWN and self.Stairs_Can_Down:
                if (self.Aressted == True): return
                if (self.Change): return
                print(self.stairPoint[0], ", ", self.stairPoint[1])
                self.x = self.stairPoint[0]
                self.y = self.stairPoint[1]
                self.y += self.height / 2

                self.stairs_down()
                self.state = self.ANI_STAND
                self.floor_at_present -= 1

            elif event.key == SDLK_DOWN and self.Stairs_Move:
                if (self.Aressted == True): return
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
            self.FRAME_PER_ACTION = 4.5
        else:
            self.dir = 5
            self.FRAME_PER_ACTION = 2


    def get_bb(self):
        left_player = self.x - self.background.window_left - self.width / 2
        bottom_player = self.y - self.background.window_bottom - self.height /2
        right_player = self.x  - self.background.window_left + self.width / 2
        top_player = self.y - self.background.window_bottom + self.width / 2
        return left_player, bottom_player, right_player, top_player

    def get_point(self):
        #pivot return
        pivot_x = self.x - self.background.window_left
        pivot_y = self.y - self.background.window_bottom - self.height / 2
        return pivot_x, pivot_y

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def Set_stairsPoint(self, topx, topy, bottomx, bottomy):
        if(len(self.stairPoint) == 4):
            self.Reset_stairsPoint()

        self.stairPoint.append(topx)
        self.stairPoint.append(topy)
        self.stairPoint.append(bottomx)
        self.stairPoint.append(bottomy)

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

    def Reach_Bottom(self):
        if not self.Stairs_Move: return False
        if not self.Down: return False
        if self.get_point()[0] > self.stairPoint[2]: return False
        if self.get_point()[1] > self.stairPoint[3]: return False

        return True

        pass

