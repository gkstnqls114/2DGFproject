import json
import os
import random
from pico2d import *

from play import Game

name = "Camera"
#모든 오브젝트 받아와서 마지막에 위치 조정

player = None
map = None
wall = None

class Camera:
    def __init__(self):
        global player, map, wall
        player= Game.player
        map = Game.map
        wall = Game.wall
        pass

    def update(self):
        if not player.Up and not player.Down and not player.Right and not player.Left: return

        if self.player_right_move():
            player.x = 400
            wall.move_x += player.dir
            map.moveX(player.dir)
            pass

        if self.player_left_move():
            player.x = 400
            wall.move_x -= player.dir
            map.moveX(-player.dir)
            pass

        if self.player_up_move():
            player.y = 300
            wall.move_y += player.dir
            map.moveY(player.dir)
            pass


        if self.player_down_move():
            player.y = 300
            print(player.y - player.height, " , ", wall.move_y, " , ", wall.height / 4)
            wall.move_y -= player.dir
            map.moveY(-player.dir)
            pass

        pass

    def player_right_move(self):
        if not player.Right and not player.Up: return False

        if player.x < 400 and wall.move_x <= wall.width / 4: return False
        if wall.move_x > wall.width / 2: return False

        return True
        pass

    def player_left_move(self):
        if not player.Left and not player.Down: return False

        if player.x > 400 and wall.move_x >= wall.width / 2: return False
        if wall.move_x <= 0: return False

        return True
        pass

    def player_up_move(self):
        if not player.Up: return False
        print("Up")
        print(player.y ,", ", wall.move_y, ", ", wall.height)
        if player.y < 300 and wall.move_y <= wall.height / 4: return False
        if wall.move_y > wall.height / 4: return False

        return True
        pass

    def player_down_move(self):
        if not player.Down: return False
        if player.y > 300 and wall.move_x >= wall.height / 2: return False
        if wall.move_y <= 0: return False

        return True
        pass





