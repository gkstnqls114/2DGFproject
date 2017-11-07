import json
import os
import random
from pico2d import *


name = "Stairs"



class Stairs:
    def __init__(self):
        self.x, self.y = 200, 125 + 90
        self.image = load_image('샘플 계단2.png')
        self.width = 250
        self.height = 250

    def update(self):
        pass

    def draw(self):
        self.image.draw( self.x, self.y)

    def handle_events(self, event):
        pass





