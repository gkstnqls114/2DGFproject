from Framwork import game_framework
from Scene import title_state
from pico2d import *


name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('kpu_credit.png')


def exit():
    global image
    del(image)


def update():
    global logo_time

    if(logo_time > 1.0):
        logo_time = 0
        # game_framework.quit()
        game_framework.change_state(title_state)
        #push_state 하면 pause가 실행 (갔다 올 때)
        #change_state 하면 exit가 실행 (내용 저장할 필요 없을 때)
    delay(0.01)
    logo_time += 0.01


def draw():
    global imgae
    clear_canvas()
    image.draw(400, 300)
    update_canvas()



def handle_events():
    events = get_events()
    pass


def pause(): pass
#다른 상태로 갔다가 다시 돌아왔을 때 저장하고 싶은 내용을 저장시켜놓음


def resume(): pass




