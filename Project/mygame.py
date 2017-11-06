from Framwork import game_framework
from pico2d import *

from Scene import start_state
from Scene import main_state

open_canvas(800 , 600)
game_framework.run(main_state)
close_canvas()