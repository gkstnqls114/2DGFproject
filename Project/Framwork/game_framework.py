
from pico2d import *

class GameState:
    def __init__(self, state):
        self.enter = state.enter
        self.exit = state.exit
        self.pause = state.pause
        self.resume = state.resume
        self.handle_events = state.handle_events
        self.update = state.update
        self.draw = state.draw


running = None
stack = None
current_time = 0.0

def change_state(state):
    global stack
    pop_state()
    stack.append(state)
    state.enter()

def push_state(state):
    global stack
    if (len(stack) > 0):
        stack[-1].pause()
    stack.append(state)
    state.enter()

def pop_state():
    global stack
    if (len(stack) > 0):
        # execute the current state's exit function
        stack[-1].exit()
        # remove the current state
        stack.pop()

    # execute resume function of the previous state
    if (len(stack) > 0):
        stack[-1].resume()

def quit():
    global running
    running = False

def get_frame_time():
    global current_time
    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

def run(start_state):
    global running, stack, current_time
    current_time = get_time()

    running = True
    stack = [start_state]
    start_state.enter()
    while (running):
        frame_time = get_frame_time()

        stack[-1].handle_events(frame_time)
        stack[-1].update(frame_time)
        stack[-1].draw()

        delay(0.01)
    # repeatedly delete the top of the stack
    while (len(stack) > 0):
        stack[-1].exit()
        stack.pop()



if __name__ == '__main__':
    test_game_framework()