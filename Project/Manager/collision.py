import json
import os
import random
from pico2d import *


name = "Collision"


class Collision:
    def __init__(self):
        pass

    def update(self, player, stairs):
        if(player.Stairs_Move and player.Up):
            # 올라가다가 계단 위쪽에 전부 도달
            if (player.x > stairs.x + stairs.width / 2):
                player.x, player.y = stairs.get_top_point()
                player.y += player.height / 2

                player.Stairs_Move = False
                player.Stairs_Can_Up = False
                player.Stairs_Can_Down = True
                player.Up = False
        elif(player.Stairs_Move and player.Down):
            if (player.x < stairs.x - stairs.width / 2):
                player.x, player.y = stairs.get_bottom_point()
                player.y += player.height / 2

                player.Stairs_Move = False
                player.Stairs_Can_Up = False
                player.Stairs_Can_Down = True
                player.Down = False

        pass

    def handle_events(self, event, player, stairs):

        if event.key == SDLK_UP and player.Stairs_Can_Up:
            player.x , player.y = stairs.get_bottom_point()
            player.y += player.height/2
            pass
        elif event.key == SDLK_UP and player.Stairs_Move:

            pass

        elif event.key == SDLK_DOWN and player.Stairs_Can_Down:
            player.x , player.y = stairs.get_top_point()
            player.y += player.height/2
        elif event.key == SDLK_DOWN and player.Stairs_Move:
            pass


    def collide_bottom(self, player, b):
        #계단 아랫부분 (포인트로 판단)
        center_x, center_y = player.get_point()
        left_b, bottom_b, right_b, top_b = b.get_bottom_bb()

        if center_x > right_b: return False
        if center_x < left_b: return False
        if center_y < bottom_b: return False
        if center_y > top_b: return False

        return True

    def collide_top(self, player, t):
        #계단 윗부분 (포인트로 판단)
        center_x= player.get_point_x()
        center_y = player.get_point_y()
        left_t, bottom_t, right_t, top_t = t.get_top_bb()

        if center_x > right_t: return False
        if center_x < left_t: return False
        if center_y < bottom_t: return False
        if center_y > top_t: return False

        return True


    def player_stair_collision(self, player, stairs):
        #아래에 있다
        if(self.collide_bottom(player, stairs)):
            player.Stairs_Can_Up = True
            player.Stairs_Can_Down = False
            pass
        #위에 있다
        elif(self.collide_top(player, stairs)):
            player.Stairs_Can_Up = False
            player.Stairs_Can_Down = True
        else:
            player.Stairs_Can_Down = False
            player.Stairs_Can_Up = False
            pass



    def collide(player, b):

        left_player, bottom_player, right_player, top_player = player.get_bb()
        left_b, bottom_b, right_b, top_b = b.get_bb()

        if left_player > right_b: return False
        if right_player < left_b: return False
        if top_player < bottom_b: return False
        if bottom_player > top_b: return False

        return True


    





