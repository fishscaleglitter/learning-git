## Penny's Adventure (Text Adventure Game) ##

## Define Map of Floors -- starting with first floor ##

import os

first_floor = [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19]]

second_floor = []

basement = []

## Item List ##

items = {0: None, 1: 'toy', 2: 'catnip', 3: 'treat'}

## Name Rooms ##
roomnum =[(n for n in first_floor)]
rooms = [n for n in first_floor]
#first_floor_rooms = {num: name for num, name in zip (roomnum, rooms)}

print(roomnum)
## Create Room ##

class Room():
    rm_name = "Test Room"

    def __init__(self, map_number=7, name=rm_name, item='', characters=[]):
        self.name = name
        self.map = map_number
        self.item = item
        self.npc = characters

    

class Player():
    pass

def createFloorMap(index, room):
   floor_map = []
   room_names = []
   
   for i in range(0,4):
       for x in range(0,5):
           floor_map.append(index[i][x])
    
    for i in range(0,4):
        for x in range(0,5):
            room_names.append(room[i][x])

    ff_map_dict = {num: room for num, room in zip (floor_map, room_names)}
   
   return ff_map_dict
   

    