import json
import os
import random
from pico2d import *

import Game

name = "Camera"

#모든 오브젝트 받아와서 카메라 조절

class Camera:
    def __init__(self):

        pass

    def update(self):
        # 반을 넘는다 (이동)
        # 플레이어 이동후에 실행해야함
        player = Game.player

        if not player.Up and not player.Down and not player.Right and not player.Left: return

        wall = Game.wall

        if self.player_right_move(player, wall):
            player.x = 400

            #print("Right Camera")
            stairs = Game.stairs
            wall.move_x += player.dir
            stairs.move_x += player.dir

            pass

        if self.player_left_move(player, wall):
            player.x = 400

            #print("Left Camera")
            stairs = Game.stairs
            wall.move_x -= player.dir
            stairs.move_x -= player.dir

            pass

        if self.player_up_move(player, wall):
            player.y = 300

            print(player.y - player.height, " , ", wall.move_y, " , ", wall.height / 4)

            print("Up Camera")
            stairs = Game.stairs
            floor = Game.floor
            wall.move_y += player.dir
            stairs.move_y += player.dir
            floor[0].move_y += player.dir
            floor[1].move_y += player.dir
            floor[2].move_y += player.dir

            pass


        if self.player_down_move(player, wall):
            player.y = 300

            print(player.y - player.height, " , ", wall.move_y, " , ", wall.height / 4)

            print("Up Camera")
            stairs = Game.stairs
            floor = Game.floor
            wall.move_y -= player.dir
            stairs.move_y -= player.dir
            floor[0].move_y -= player.dir
            floor[1].move_y -= player.dir
            floor[2].move_y -= player.dir

            pass

        pass

    def player_right_move(self, player, wall):
        if not player.Right and not player.Up: return False
        if player.x < 400 and wall.move_x <= wall.width / 4: return False
        if wall.move_x > wall.width / 2: return False

        return True
        pass

    def player_left_move(self, player, wall):
        if not player.Left and not player.Down: return False
        if player.x > 400 and wall.move_x >= wall.width / 2: return False
        if wall.move_x <= 0: return False

        return True
        pass

    def player_up_move(self, player, wall):
        if not player.Up: return False
        if player.y < 300 and wall.move_y <= wall.height / 4: return False
        if wall.move_y > wall.height / 2: return False

        return True
        pass

    def player_down_move(self, player, wall):
        if not player.Down: return False
        if player.y > 300 and wall.move_x >= wall.height / 2: return False
        if wall.move_y <= 0: return False

        return True
        pass





