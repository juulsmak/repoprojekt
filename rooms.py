import pygame as pg
import random
import numpy as np
from main import Enemy, enemy_group
from copy import deepcopy


screen_size_x = 1000
screen_size_y = 600
screen = pg.display.set_mode((screen_size_x,screen_size_y))


class Map():
    def __init__(self):
        self.roomlist = random.choice(maplist)
        self.map = []
        self.maptypes = []
        self.maprooms = []
        self.position = 0
        for i in range(0, 4):
            for j in range(0, 4):
                if self.roomlist[i][j] == 1:
                    self.map.append([i, j])
                    self.maptypes.append('normal')
                elif self.roomlist[i][j] == 2:
                    self.map.append([i, j])
                    self.maptypes.append('start')
                    self.position = [i, j]
                elif self.roomlist[i][j] == 3:
                    self.map.append([i, j])
                    self.maptypes.append('boss')

        for el in self.maptypes:
            if el == 'normal':
                self.maprooms.append(random.choice(mapsnormal))
            elif el == 'boss':
                self.maprooms.append(random.choice(mapsboss))
            elif el == 'start':
                self.maprooms.append(random.choice(mapsstart))



class Door():
    def __init__(self, pokojdane):
        self.room = deepcopy(pokojdane)

    def right(self):
        self.room[5][19] = 6
        self.room[6][19] = 6
        return self.room

    def left(self):
        self.room[5][0] = 8
        self.room[6][0] = 8
        return self.room
    def up(self):
        self.room[0][9] = 5
        self.room[0][10] = 5
        return self.room
    def down(self):
        self.room[11][9] = 7
        self.room[11][10] = 7
        return self.room

pokojdane = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


map1 =np.array( [
    [1, 1, 0],
    [0, 2, 0],
    [1, 1, 0]
])
maplist = [map1]
mapsnormal= []
mapsstart = []
mapsboss = []
enemies = [Enemy(0,0,2,2,50)]

