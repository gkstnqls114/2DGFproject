import json
import os
import random
from pico2d import *

from Scene import main_state

name = "Camera"

class Camera:
    def __init__(self):

        pass

    def update(self):
        pass

    def handle_events(self, event):
        player = main_state.player
        stairs = main_state.stairs

        if player.x > 800 / 2:
            stairs.y -= player.dir

        pass




