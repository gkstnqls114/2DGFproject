import json
import os
import random
from pico2d import *

from Object import background_object
from Object import background_object
from Object import floor_object
from Object import stairs_object
from Object import treasure_object
from Object import guard_object


name = "Map"

# 플레이어를 제외한 모든 오브젝트들의 위치가 있다.
class Map:
    background = None

    def __init__(self):
        if(self.background == None):
            self.background = background_object.Background()

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

        self.background.width = self.map_width
        self.background.height = self.map_height


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
        stairs_data_file = open('Data/stairs_data_text.txt', 'r')
        stairs_data = json.load(stairs_data_file)
        stairs_data_file.close()

        stairs_group = []
        for name in stairs_data:
            stairs = stairs_object.Stairs(self.background)
            stairs.name = name
            stairs.width = (self.floor_cell_height + self.floor_width)
            stairs.height = (self.floor_cell_height + self.floor_width)

            stairs.floor_num = stairs_data[name]['floor_num']
            stairs.x = stairs_data[name]['x']
            stairs.y = (stairs.floor_num - 1) * (self.floor_cell_height + self.floor_width)\
                       + self.floor_width + stairs.height / 2 - 10
            stairs_group.append(stairs)

        print("완료")

        return stairs_group
        pass
    def create_guard(self):
        # 파일을 받아 경비원 생성
        guard_data_file = open('Data/guard_data_text.txt', 'r')
        guard_data = json.load(guard_data_file)
        guard_data_file.close()

        guard_group = []
        for name in guard_data:
            guard = guard_object.Guard(self.background)
            guard.name = name
            guard.x = guard_data[name]['x']
            guard.Map_x = guard.x
            guard.floor_num = guard_data[name]['floor_num']
            guard.y = (guard.floor_num - 1) * (self.floor_cell_height + self.floor_width)\
                      + self.floor_width + guard.height / 2 - 10
            guard.Map_y = guard.y
            guard_group.append(guard)

        return guard_group
        pass
    def create_treasure(self):
        # 파일을 받아 경비원 생성
        treasure_data_file = open('Data/treasure_data_text.txt', 'r')
        treasure_data = json.load(treasure_data_file)
        treasure_data_file.close()

        treasure_group = []
        for name in treasure_data:
            treasure = treasure_object.Treasure(self.background)
            treasure.name = name
            treasure.x = treasure_data[name]['x']
            treasure.floor_num = treasure_data[name]['floor_num']
            treasure.y = (treasure.floor_num - 1) * (self.floor_cell_height + self.floor_width)\
                         + self.floor_width + treasure.height / 2 - 10
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

