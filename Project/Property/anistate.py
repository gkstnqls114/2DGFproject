import json
import os
import random
from pico2d import *

#아직 적용못함
class AniState:
    #ANIMAITON
    ANI_STAND = 0
    ANI_RIGHT = 1
    ANI_LEFT = 2
    ANI_STAIRS_MOVE_UP = 3
    ANI_STAIRS_MOVE_DOWN = 4
    ANI_CHANGE = 5

    def __init__(self):
        self.state = self.ANI_STAND
        pass

    def STAND(self):
        self.state = self.ANI_STAND
        pass

    def RIGHT(self):
        self.state = self.ANI_RIGHT
        pass

    def LEFT(self):
        self.state = self.ANI_LEFT
        pass

    def STAIRS_MOVE_UP(self):
        self.state = self.ANI_STAIRS_MOVE_UP
        pass

    def STAIRS_MOVE_DOWN(self):
        self.state = self.ANI_STAIRS_MOVE_DOWN
        pass

    def CHANGE(self):
        self.state = self.ANI_CHAGE
        pass

    def Get_state(self):
        return self.state
        pass

