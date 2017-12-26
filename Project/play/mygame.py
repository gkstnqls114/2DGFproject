from Framwork import game_framework
from pico2d import *

import platform
from Scene import start_state
from Scene import main_state
from Scene import title_state
from Scene import askpause_state

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"


open_canvas(WINDOW_WIDTH , WINDOW_HEIGHT)
game_framework.run(main_state)
#game_framework.run(start_state)
close_canvas()