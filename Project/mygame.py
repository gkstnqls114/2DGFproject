from Framwork import game_framework
from pico2d import *

from Scene import start_state
from Scene import main_state

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

open_canvas(WINDOW_WIDTH , WINDOW_HEIGHT)
game_framework.run(main_state)
close_canvas()