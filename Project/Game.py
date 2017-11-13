import json
import os
import random
from pico2d import *

#Manager
from Manager import collision_manager
from Manager import mediator_manager
from Manager import camera_manager

#Scene
from Scene import pause_state
from Scene import title_state
from Framwork import game_framework

#Object
from Object import player_object
from Object import guard_object
from Object import stairs_object
from Object import floor_object
from Object import wall_object

name = "Game"

player = None
floor = []
stairs = None
wall = None
font = None

collisionManager = None
guard = None
mediatorManager = None
cameraManager = None

class Game:
    def enter(self):
        global player, floor, wall, stairs, guard
        global collisionManager, mediatorManager,cameraManager

        player = player_object.Player()
        stairs = stairs_object.Stairs()
        wall = wall_object.Wall()
        collisionManager = collision_manager.Collision()
        guard = guard_object.Guard()
        cameraManager = camera_manager.Camera()

        for i in range (0, 3):
            floor.append(floor_object.Floor(i * 300, i))
        pass

    def exit(self):
        #일단 나중에 꼭 추가하기!
        global player, floor, stairs
        del(player)
        del(floor)
        del(stairs)
        pass


    def pauses(self):
        pass

    def resume(self):
        pass

    def handle_events(self, event):
            player.handle_events(event)
            collisionManager.handle_events(event, player, stairs)

    def update(self):
        player.update()
        cameraManager.update()
        collisionManager.update(player, stairs)
        collisionManager.player_stair_collision(player, stairs)


    def draw_scene(self):
        wall.draw()
        for i in range (0, 3):
            floor[i].draw()
        stairs.draw()
        player.draw()
        guard.draw()







