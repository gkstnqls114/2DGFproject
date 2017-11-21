import json
import os
import random
from pico2d import *

#아직 적용못함
class Coordination:
    def __init__(self, x, y):
        #x, y는 반드시 int
        self.Camera_x = x
        self.Camera_y = y
        self.Map_x = x
        self.Map_y = y

        print("좌표 설정: ")
        print("Camera: %d %d" %(self.Camera_x, self.Camera_y))
        print("Map: %d %d" %(self.Map_x, self.Map_y))

    pass

    def Get_MapXY(self):
        return self.Map_x, self.Map_y
        pass

    def Get_CameraXY(self):
        return self.Camera_x, self.Camera_y
        pass

    def Get_MapX(self):
        return self.Map_x

    def Get_MapY(self):
        return self.Map_y

    def Get_CameraX(self):
        return self.Camera_x

    def Get_CameraY(self):
        return self.Camera_y

    def MoveXY(self, dir):
        self.Map_move_x(dir)
        self.Map_move_y(dir)
        self.Camera_move_x(dir)
        self.Camera_move_y(dir)
        pass

    def MoveX(self, dir):
        self.Map_move_x(dir)
        self.Camera_move_x(dir)
        pass

    def MoveY(self, dir):
        self.Map_move_y(dir)
        self.Camera_move_y(dir)
        pass

    def CameraMove(self, dir):
        self.Camera_move_x(dir)
        self.Camera_move_x(dir)
        pass

    def Map_move_x(self, dir):
        self.Map_x += dir
        pass

    def Map_move_y(self, dir):
        self.Map_y += dir
        pass

    def Camera_move_x(self, dir):
        self.Camera_x += dir
        pass

    def Camera_move_y(self, dir):
        self.Camera_y += dir
        pass


