import json
import os
import random
from pico2d import *

from Object import background_object
from Object import floor_object
from Object import stairs_object
from Object import treasure_object
from Object import guard_object
from Object import door_object

name = "Map"

# 플레이어를 제외한 모든 오브젝트들의 위치가 있다.
class Map:
    background = None
    door = None

    def __init__(self):
        if(self.background == None):
            self.background = background_object.Background()
        if(self.door == None):
            self.door = door_object.door(self.background)

        self.unit = 0
        self.map_width = 0
        self.map_height = 0
        self.floor_cell_height = 0
        self.number_of_floor = 0

        self.create_map()

        self.floor_group = self.create_floor()
        self.stairs_group = self.create_stairs()
        self.guard_group = self.create_guard()
        self.treasure_group = self.create_treasure()

        pass

    def create_map(self):
        map_data_file = open('Data/map_data_text.txt', 'r')
        map_data = json.load(map_data_file)
        map_data_file.close()

        self.unit = map_data["Unit (cm per 1px)"]
        self.map_width = int(map_data["Map Width (cm)"] / self.unit)
        self.floor_cell_height = int(map_data["Map Celling (cm)"] / self.unit)
        self.floor_width = int(map_data["Floor Width (cm)"] / self.unit)
        self.number_of_floor =  map_data["Number Of Floor"]
        self.map_height = int((self.floor_cell_height + self.floor_width)* self.number_of_floor)

        self.door.y = self.floor_width + self.door.height / 2
        self.background.width = self.map_width
        self.background.height = self.map_height
        print (self.background.width ," ", self.background.height)


    def create_floor(self):
        #파일을 받아 플로어 생성
        floor_group = []
        for i in  range(1, self.number_of_floor):
            floor = floor_object.Floor(self.background)
            floor.floor_num = i
            floor.height = self.floor_width
            floor.width = self.map_width
            floor.x = floor.width / 2
            floor.y = (floor.floor_num - 1) * (self.floor_cell_height + self.floor_width) + self.floor_width / 2
            floor_group.append(floor)


        return floor_group
        pass

    def create_stairs(self):
        #파일을 받아 계단 생성
        stairs_group = []
        for i in range(1, self.number_of_floor - 1):
            stairs = stairs_object.Stairs(self.background)
            stairs.width = (self.floor_cell_height + self.floor_width)
            stairs.height = (self.floor_cell_height + self.floor_width)

            stairs.floor_num = i

            if(stairs.floor_num % 2 == 1):
                stairs.x = self.map_width - stairs.width / 2 - 100
            else:
                stairs.x =  stairs.width / 2 + 100

            stairs.y = (stairs.floor_num - 1) * (self.floor_cell_height + self.floor_width)\
                       + self.floor_width + stairs.height / 2 - 10
            stairs_group.append(stairs)

        return stairs_group
        pass

    def create_guard(self):
        # 파일을 받아 경비원 생성

        guard_group = []
        for i in range(2, self.number_of_floor):
            guard = guard_object.Guard(self.background)
            guard.x = random.randrange(guard.width / 2, self.map_width - guard.width / 2)
            guard.floor_num = i
            guard.y = (guard.floor_num - 1) * (self.floor_cell_height + self.floor_width)\
                      + self.floor_width + guard.height / 2 - 10
            guard_group.append(guard)

        return guard_group
        pass

    def create_treasure(self):

        treasure_group = []
        for floornum in range(1, self.number_of_floor):
            for i in range(0, 8):
                treasure = treasure_object.Treasure(self.background)

                if floornum == 1:
                    if i >= 7:
                        continue
                    treasure.x = 300 + i * 130
                elif floornum % 2 == 1:
                    treasure.x = 150 + i * 130
                else:
                    treasure.x = self.map_width - 150 -i * 130

                treasure.floor_num = floornum
                treasure.y = (treasure.floor_num - 1) * (self.floor_cell_height + self.floor_width)\
                         + self.floor_width + treasure.height / 2 - 10
                if(treasure.sort == treasure.ART):
                    treasure.y += 70

                treasure_group.append(treasure)

        return treasure_group
        pass

    def get_stairs(self, index):
        if(len(self.stairs_group) <= index): return 0
        return self.stairs_group[index]

    def get_stairs_len(self):
        return len(self.stairs_group)

    def get_guard(self, index):
        return self.guard_group[index]
        pass

    def get_guard_len(self):
        return len(self.guard_group)

    def get_treasure(self, index):
        return self.treasure_group[index]
        pass

    def get_treasure_len(self):
        return len(self.treasure_group)

    def draw(self):
        self.background.draw()

        for floor in self.floor_group:
            floor.draw()
        for stairs in self.stairs_group:
            stairs.draw()
        for treasure in self.treasure_group:
            treasure.draw()
        for guard in self.guard_group:
            guard.draw()
            pass

        self.door.draw()
        pass

    def update(self, frame_time):
        self.background.update(frame_time)

        for guard in self.guard_group:
            guard.update(frame_time)
            pass
        for floor in self.floor_group:
            floor.update(frame_time)
            pass
        for treasure in self.treasure_group:
            treasure.update(frame_time)
            pass
        for stairs in self.stairs_group:
            stairs.update(frame_time)
            pass
        pass

