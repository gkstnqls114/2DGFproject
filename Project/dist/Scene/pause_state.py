from pico2d import *

from Framwork import game_framework
from Scene import main_state



name = "PauseState"

pauseimg = None

class Pause:
    def __init__(self):
        self.image = load_image('Image/Scene/pause.png')
        self.x, self.y = 400, 300

    def draw(self):
        self.image.draw(self.x, self.y)

def enter():
    global pauseimg
    pauseimg = Pause()

def exit():
    global pauseimg
    del(pauseimg)


def pause():
    pass


def resume():
    pass


def handle_events(frame_tome):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_state()


def update(frame_time):
    pass


def draw():
    clear_canvas()
    main_state.draw_scene()
    pauseimg.draw()
    update_canvas()





