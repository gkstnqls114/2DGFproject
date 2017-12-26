
import platform
import os

if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"

from Framwork import game_framework
from pico2d import *

from Scene import title_state

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


open_canvas(WINDOW_WIDTH , WINDOW_HEIGHT)
game_framework.run(title_state)
#game_framework.run(start_state)
close_canvas()