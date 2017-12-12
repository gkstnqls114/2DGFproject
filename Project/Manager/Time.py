import json
import os
import random
import time
from pico2d import *

from Framwork import game_framework
from Scene import over_state

name = "Time"

class Time:
    def __init__(self):
        self.font = load_font('ENCR10B.TTF',16)
        self.font2 = load_font('ENCR10B.TTF',16)
        self.startTime = time.time()
        self.elapsedTime = time.time() - self.startTime
        self.minutes = 1
        self.seconds = 20
        self.count = 1



    def update(self, frame_time):
        if self.minutes == 0 and self.seconds == 0:
            #print("화면이동")
            game_framework.change_state(over_state)

        self.elapsedTime = time.time() - self.startTime

        if(self.seconds < 0):
            self.minutes -= 1
            self.seconds = 59
        elif int(self.elapsedTime) - self.count == 0:
            self.count +=1
            self.seconds -= 1






    def draw(self):
        self.font.draw(10, 10, '%d 분 %d 초' %(self.minutes, self.seconds))
        self.font.draw(10, 30, '%f' %( self.elapsedTime ))


