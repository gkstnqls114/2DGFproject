import json
import os
import random
from pico2d import *

#Manager
from Manager import collision

#Scene
from Scene import pause_state
from Scene import title_state
from Framwork import game_framework

#Object
from Object import player_object
from Object import stairs_object
from Object import floor_object

name = "MainState"

player = None
floor = []
stairs = None
font = None
collisionManager = None


def enter():
    global player, floor, stairs, collisionManager
    player = player_object.Player()
    stairs = stairs_object.Stairs()
    collisionManager = collision.Collision()

    for i in range (0, 3):
        floor.append(floor_object.Floor(i * 300, i))
    pass

def exit():
    global player, floor, stairs, collision
    del(player)
    del(floor)
    del(stairs)
    del(collision)


def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state)
        else:
            collisionManager.handle_events(event, player, stairs)
            player.handle_events(event)

def update():
    collisionManager.update(player, stairs)
    collisionManager.player_stair_collision(player, stairs)
    player.update()


def draw_scene():
    for i in range (0, 3):
        floor[i].draw()
    stairs.draw()
    player.draw()



def draw():
    clear_canvas()
    draw_scene()
    update_canvas()





