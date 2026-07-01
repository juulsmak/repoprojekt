import pygame as pg
import random
import numpy as np
from copy import deepcopy


screen_size_x = 1000
screen_size_y = 600
screen = pg.display.set_mode((screen_size_x,screen_size_y))


class Map():
    def __init__(self):
        self.roomlist = map1
        self.mapvar = []
        self.maptypes = []
        self.maprooms = []
        self.position = 0
        self.startingroom = []
        for i in range(0, 4):
            for j in range(0, 4):
                if self.roomlist[i][j] == 1:
                    self.mapvar.append([i, j])
                    self.maptypes.append('normal')
                    self.maprooms.append(deepcopy(random.choice(mapsnormal)))
                elif self.roomlist[i][j] == 2:
                    self.mapvar.append([i, j])
                    self.maptypes.append('start')
                    self.maprooms.append(deepcopy(random.choice(mapsnormal)))
                    self.position = [i, j]
#                elif self.roomlist[i][j] == 3:
#                    self.mapvar.append([i, j])
#                    self.maprooms.append(random.choice(mapsboss))
#                    self.maptypes.append('boss')


        for el in self.mapvar:
            ind = self.mapvar.index(el)
            room = self.maprooms[ind]
            if [el[0], el[1]+1] in self.mapvar:
                room = Door(room).right()
            if [el[0], el[1]-1] in self.mapvar:
                room = Door(room).left()
            if [el[0] + 1, el[1]] in self.mapvar:
                room = Door(room).down()
            if [el[0] - 1, el[1]] in self.mapvar:
                room = Door(room).up()
            self.maprooms[ind] = room

        self.startingroom = self.maprooms[self.mapvar.index(self.position)]



class Door():
    def __init__(self, pokojdane):
        self.room = pokojdane

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
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


map1 =np.array( [
    [0, 0, 1, 0],
    [0, 1, 2, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
])
maplist = [map1]
mapsnormal= [pokojdane]
mapsstart = []
mapsboss = []



