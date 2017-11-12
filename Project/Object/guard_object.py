import json
import os
import random
from pico2d import *

name = "Guard"

#현재 플레이어와 똑같음..
#

class Guard:
    def __init__(self):
        self.width = 70
        self.heigth = 100
        self.x, self.y = 0, self.heigth

        self.frame = 0
        self.image = load_image('샘플 플레이어.png')
        self.dir = 1

        # 움직임 bool
        self.Run = False
        self.Right = False
        self.Left = False

        # 계단을 올라 가는 bool
        self.Stairs_Can_Up = False
        self.Stairs_Can_Down = False
        self.Stairs_Move = False

        # 현재 플레이어가 있는 플로어
        self.floor_at_present = 1

        self.runningTime = 0
        self.pause = (self.x, self.y, self.frame, self.dir)

    def update(self):
        self.frame = (self.frame + 1) % 8

        self.runningFunc()

        # 계단 범위 넘어섰는가 확인


        if (self.Right):
            self.x += self.dir
        if (self.Left):
            self.x -= self.dir
        if (self.Stairs_Can_Up):
            self.x += self.dir
            self.y += self.dir
        if (self.Stairs_Can_Down):
            self.x -= self.dir
            self.y -= self.dir

    def draw(self):
        # self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        if (self.TopStair_range or self.BottomStair_range):
            self.image.draw(self.x, self.y)
            pass
        else:
            self.image.draw(self.x, self.y)
            pass

    def handle_events(self, event):
        # key down

        if event.type == SDL_KEYDOWN:
            z = 122
            if event.key == z:
                self.Run = True
            elif event.key == SDLK_RIGHT and not self.BottomStair_range:
                self.Right = True
            elif event.key == SDLK_LEFT and not self.BottomStair_range:
                self.Left = True
            elif event.key == SDLK_UP and self.BottomStair_range:
                self.Stairs_Can_Up = True
                self.Stairs_Move = True
            elif event.key == SDLK_DOWN and self.TopStair_range:
                self.Stairs_Can_Down = True
                self.Stairs_Move = True

        # key up

        if event.type == SDL_KEYUP:
            z = 122
            if event.key == z:
                self.Run = False
            elif event.key == SDLK_RIGHT:
                self.Right = False
            elif event.key == SDLK_LEFT:
                self.Left = False
            elif event.key == SDLK_UP:
                self.Stairs_Can_Up = False

            elif event.key == SDLK_DOWN:
                self.Stairs_Can_Down = False

    def runningFunc(self):
        if self.Run:
            print ("run")
            self.dir = 3

        else:
            self.dir = 1




