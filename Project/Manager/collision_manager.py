import json
import os
import random
from pico2d import *

from play import Game

name = "Collision"
#부딪히는 것 체크만 한다.
player = None
map = None

class Collision:
    def __init__(self):
        self.stairs_move_index = -1
        self.collide_treasure_index = -1

        global player
        player = Game.player
        pass

    def update(self):
        #경비원과 플레이어 부딪힘
        for index in range (0, Game.map.get_guard_len()):
            if(self.collide_guard(index)):
                guard = Game.map.get_guard(index)
                guard.SeePlayer = True
                guard.SeePlayerTime = 1000

                if(guard.Hp > 0):
                    player.Aressted = True
                    player.ArrestGuard(guard)
                    if(player.x < guard.x):
                        guard.playerState = guard.ANI_LEFT
                    if(player.x > guard.x):
                        guard.playerState = guard.ANI_RIGHT
                return
            else:
                player.Aressted = False
            pass

        #경비원이 플레이어를 보았다
        for index in range (0, Game.map.get_guard_len()):
            if(self.collide_see_guard(index)):
                guard = Game.map.get_guard(index)
                guard.SeePlayer = True
                guard.SeePlayerTime = 1000
                guard.playerFloor = player.floor_at_present

                if(player.x < guard.x):
                    guard.playerState = guard.ANI_LEFT
                if(player.x > guard.x):
                    guard.playerState = guard.ANI_RIGHT
            pass

        #플레이어와 계단 충돌 확인
        self.player_stair_collision()

        if(player.Stairs_Move):
            stairs = Game.map.get_stairs(self.stairs_move_index)

        if(self.Reach_Top()):
            # 올라가다가 계단 위쪽에 전부 도달

            stairs = Game.map.get_stairs(self.stairs_move_index)
            fix_x = stairs.get_top_point()[0] + stairs.background.window_left
            fix_y = stairs.get_top_point()[1] + stairs.background.window_bottom

            player.x = fix_x
            player.y = fix_y + player.height / 2

            player.Stairs_Move = False
            player.Stairs_Can_Up = False
            player.Stairs_Can_Down = True
            player.Up = False
            player.state = player.ANI_STAND
            pass
        elif(self.Reach_Bottom()):
            print ("계단 아래 도달")

            print("수정전: ", player.x, " ", player.y)

            stairs = Game.map.get_stairs(self.stairs_move_index)
            fix_x = stairs.get_bottom_point()[0] + stairs.background.window_left
            fix_y = stairs.get_bottom_point()[1] + stairs.background.window_bottom

            player.x = fix_x
            player.y = fix_y + player.height / 2

            print("수정전: ", player.x, " ", player.y)

            player.Stairs_Move = False
            player.Stairs_Can_Up = False
            player.Stairs_Can_Down = True
            player.Down = False
            player.state = player.ANI_STAND
            pass

        #플레이어와 보물상자 충돌 확인
        self.player_treasure_collision()

        if(player.Treasure_Search):
            player.treasure_num += 1
            player.Treasure_Search = False
            player.Treasure_Can_Open = False
            treasure = Game.map.get_treasure(self.collide_treasure_index)
            treasure.open_box()


        pass

    def handle_events(self, event):
        pass

    def collide_bottom(self, index):
        #계단 아랫부분
        if player.Stairs_Move: return False
        b = Game.map.get_stairs(index)

        left_player, bottom_player, right_player, top_player = player.get_bb()
        left_b, bottom_b, right_b, top_b = b.get_bottom_bb()


        if left_player > right_b: return False
        if right_player < left_b: return False
        if top_player < bottom_b: return False
        if bottom_player > top_b: return False

        return True

    def collide_top(self, index):
        #계단 윗부분 (포인트로 판단)
        if player.Stairs_Move: return False
        t = Game.map.get_stairs(index)

        left_player, bottom_player, right_player, top_player = player.get_bb()
        left_t, bottom_t, right_t, top_t = t.get_top_bb()

        if left_player > right_t: return False
        if right_player < left_t: return False
        if top_player < bottom_t: return False
        if bottom_player > top_t: return False

        return True

    def player_stair_collision(self):
        #아래에 있다
        for index in range (0, Game.map.get_stairs_len()):
            if(self.collide_bottom(index)):
                stairs = Game.map.get_stairs(index)

                fix_top_x = stairs.get_top_point()[0] + stairs.background.window_left
                fix_top_y = stairs.get_top_point()[1] + stairs.background.window_bottom
                fix_bottom_x = stairs.get_bottom_point()[0] + stairs.background.window_left
                fix_bottom_y = stairs.get_bottom_point()[1] + stairs.background.window_bottom

                player.Set_stairsPoint(fix_top_x,fix_top_y,  fix_bottom_x,  fix_bottom_y)

                player.Stairs_Can_Up = True
                player.Stairs_Can_Down = False
                self.stairs_move_index = index

                return
            #  위에 있다
            elif(self.collide_top(index)):
                stairs = Game.map.get_stairs(index)

                fix_top_x = stairs.get_top_point()[0] + stairs.background.window_left
                fix_top_y = stairs.get_top_point()[1] + stairs.background.window_bottom
                fix_bottom_x = stairs.get_bottom_point()[0] + stairs.background.window_left
                fix_bottom_y = stairs.get_bottom_point()[1] + stairs.background.window_bottom

                print("위와 부딪힘")
                print(fix_top_x , " ", fix_top_y ," " , fix_bottom_x ," ", fix_bottom_y)

                player.Set_stairsPoint(fix_top_x,fix_top_y,  fix_bottom_x,  fix_bottom_y)

                player.Stairs_Can_Up = False
                player.Stairs_Can_Down = True
                self.stairs_move_index = index

                return

        player.Stairs_Can_Down = False
        player.Stairs_Can_Up = False
        pass

    def player_treasure_collision(self):
        for index in range(0, Game.map.get_treasure_len()):
            if self.collide_treasure(index):
                player.Treasure_Can_Open = True
                self.collide_treasure_index = index
                return

        player.Treasure_Can_Open = False
        pass

    def Reach_Top(self):
        if not player.Stairs_Move: return False
        if not player.Up: return False

        stairs = Game.map.get_stairs(self.stairs_move_index)
        stairs_x = stairs.get_top_point()[0]+ stairs.background.window_left
        staris_y = stairs.get_top_point()[1]+ stairs.background.window_bottom

        if player.x < stairs_x: return False
        if player.y - player.height /2 < staris_y: return False

        print("윗부분 도착")


        return True
        pass

    def Reach_Bottom(self):
        if not player.Stairs_Move: return False
        if not player.Down: return False

        stairs = Game.map.get_stairs(self.stairs_move_index)
        stairs_x = stairs.get_bottom_point()[0] + stairs.background.window_left
        staris_y = stairs.get_bottom_point()[1]+ stairs.background.window_bottom

        if player.x > stairs_x: return False
        if player.y - player.height /2 > staris_y: return False


        return True
        pass

    def collide_guard(self, index):
        if (player.state == player.ANI_CHANGE): return False
        if (player.state == player.ANI_STAIRS_MOVE_UP): return False
        if (player.state == player.ANI_STAIRS_MOVE_DOWN): return False

        guard = Game.map.get_guard(index)
        left_player, bottom_player, right_player, top_player = player.get_bb()
        left_b, bottom_b, right_b, top_b = guard.get_bb()
        # print(left_b, " , ", bottom_b," , ", right_b, " , ", top_b)

        if left_player > right_b: return False
        if right_player < left_b: return False
        if top_player < bottom_b: return False
        if bottom_player > top_b: return False
        return True

    def collide_see_guard(self, index):
        if(player.state == player.ANI_CHANGE): return False

        guard = Game.map.get_guard(index)
        left_player, bottom_player, right_player, top_player = player.get_bb()
        left_b, bottom_b, right_b, top_b = guard.get_see_bb()
        #print(left_b, " , ", bottom_b," , ", right_b, " , ", top_b)

        if left_player > right_b: return False
        if right_player < left_b: return False
        if top_player < bottom_b: return False
        if bottom_player > top_b: return False
        return True

    def collide_treasure(self, index):
        if (player.state == player.ANI_CHANGE): return False

        treasure = Game.map.get_treasure(index)
        if(treasure.state == treasure.OPEN) : return False

        left_player, bottom_player, right_player, top_player = player.get_bb()
        left_b, bottom_b, right_b, top_b = treasure.get_bb()

        if left_player > right_b: return False
        if right_player < left_b: return False
        if top_player < bottom_b: return False
        if bottom_player > top_b: return False
        return True
        pass


    def collide_guard_bottom(self):
        #계단 아랫부분 (포인트로 판단)
        guard = Game.guard
        b = Game.stairs

        center_x, center_y = guard.get_point()
        left_b, bottom_b, right_b, top_b = b.get_bottom_bb()

        print("Guard: ", center_x, " ", center_y)
        print("계단X: ", left_b, " ", right_b)
        print("계단Y: ", bottom_b, " ", top_b)


        if center_x > right_b: return False
        if center_x < left_b: return False
        if center_y < bottom_b: return False
        if center_y > top_b: return False

        return True

    def collide_guard_top(self):
        #계단 윗부분 (포인트로 판단)
        guard = Game.guard
        t = Game.stairs

        center_x = guard.get_point_x()
        center_y = guard.get_point_y()
        left_t, bottom_t, right_t, top_t = t.get_top_bb()

        if center_x > right_t: return False
        if center_x < left_t: return False
        if center_y < bottom_t: return False
        if center_y > top_t: return False

        return True

    





