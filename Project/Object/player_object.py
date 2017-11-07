import json
import os
import random
from pico2d import *


name = "Player"


class Player:
    def __init__(self):
        self.width = 70
        self.heigth = 100
        self.x, self.y = 0, self.heigth

        self.frame = 0
        self.image = load_image('샘플 플레이어.png')
        self.dir = 1

        #움직임 bool
        self.Run = False
        self.Right = False
        self.Left = False
        self.Up = False
        self.Down = False

        #계단을 올라 가는 bool
        self.top_range = 0
        self.bottom_range = 0
        self.Stairs_Can_Up = False
        self.Stairs_Can_Down = False
        self.Stairs_Move = False

        #현재 플레이어가 있는 플로어
        self.floor_at_present = 1

        self.runningTime = 0
        self.pause = (self.x, self.y, self.frame, self.dir)

    def update(self):
        self.frame = (self.frame + 1) % 8

        self.runningFunc()


        if(self.Right):
            self.x += self.dir
        if (self.Left):
            self.x -= self.dir
        if(self.Up):
            if(self.top_range < self.y - self.heigth / 2):
                self.Up = False
                self.Stairs_Move = False
                self.y = self.top_range + self.heigth / 2
            else:
                self.x += self.dir
                self.y += self.dir
        if (self.Down):
            if(self.bottom_range > self.y - self.heigth / 2):
                self.Down = False
                self.Stairs_Move = False
                self.y = self.bottom_range + self.heigth / 2
            else:
                self.x -= self.dir
                self.y -= self.dir


    def draw(self):
        #self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
         self.image.draw( self.x, self.y)


    def handle_events(self, event):
            # key down

        if event.type == SDL_KEYDOWN:
            z = 122
            if event.key == z :
                self.Run = True
            elif event.key == SDLK_RIGHT and (not self.Stairs_Move):
                self.Right = True
            elif  event.key == SDLK_LEFT and (not self.Stairs_Move):
                self.Left = True
            elif event.key == SDLK_UP and (self.Stairs_Can_Up or self.Stairs_Move):
                self.Stairs_Can_Up = False
                self.Stairs_Move = True
                self.Up = True
            elif event.key == SDLK_DOWN and (self.Stairs_Can_Down or self.Stairs_Move):
                self.Stairs_Can_Down = False
                self.Stairs_Move = True
                self.Down = True

        # key up

        if event.type == SDL_KEYUP:
            z = 122
            if event.key == z:
                self.Run = False
            elif event.key == SDLK_RIGHT:
                self.Right = False
            elif  event.key == SDLK_LEFT:
                self.Left = False
            elif event.key == SDLK_UP:
                self.Up = False
            elif event.key ==SDLK_DOWN:
                self.Down = False


    def runningFunc(self):
        if self.Run:
            print ("run")
            self.dir = 3

        else:
            self.dir = 1


    def around_stairs(self, stairs):
        #바닥 계단 존재하는 부분

        #임시
        stairs_bottom_range = [ stairs.x - stairs.width/2 - 30, stairs.x - stairs.width/2 + 30
            , stairs.y - stairs.height/2 - 30, stairs.y - stairs.height/2 + 30 ]

        stairs_top_range = [stairs.x + stairs.width / 2 - 30, stairs.x + stairs.width / 2 + 30
            , stairs.y + stairs.height / 2 - 30, stairs.y + stairs.height / 2 + 30]

        You_Are_Bottom_Stairs = (self.x > stairs_bottom_range[0]) and (self.x <= stairs_bottom_range[1])\
                and (self.y - self.heigth / 2 > stairs_bottom_range[2]) and (self.y - self.heigth / 2 <= stairs_bottom_range[3])
        if You_Are_Bottom_Stairs:
            self.Stairs_Can_Up = True
            self.Stairs_Can_Down = False
            self.top_range = stairs.y + stairs.height / 2
            self.bottom_range = stairs.y - stairs.height / 2
            print("당신은 계단 아래 쪽에 있다.")

        You_Are_Bottom_Stairs = (self.x > stairs_top_range[0]) and (self.x <= stairs_top_range[1]) \
               and (self.y - self.heigth / 2 > stairs_top_range[2]) and (self.y - self.heigth / 2 <= stairs_top_range[3])
        if You_Are_Bottom_Stairs:
            self.Stairs_Can_Up = False
            self.Stairs_Can_Down = True
            self.top_range = stairs.y + stairs.height / 2
            self.bottom_range = stairs.y - stairs.height / 2
            print("당신은 계단 위 쪽에 있다.")



        print ("     나: ", self.x," , ", self.y)



