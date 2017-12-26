from pico2d import *

from Framwork import game_framework
from Scene import main_state



name = "AskPauseState"

pauseimg = None

class Pause:
    def __init__(self):
        self.image = load_image('pause.png')
        self.x, self.y = 400, 300
        self.show = True
    def draw(self):
        if self.show == True:
            self.image.draw(self.x, self.y)
            delay(0.1)
            self.show = False
        elif self.show == False:
            delay(0.1)
            self.show = True


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


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()


def update():
    pass


def draw():
    clear_canvas()
    main_state.draw_scene()
    pauseimg.draw()
    update_canvas()





