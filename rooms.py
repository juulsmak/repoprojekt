import pygame as pg
import random
import numpy as np


screen_size_x = 1000
screen_size_y = 600
screen = pg.display.set_mode((screen_size_x,screen_size_y))

tilesz = 50


class Map():
    def __init__(self):
        self.roomlist = random.choice(maplist)
        self.map = []
        self.maptypes = []
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





class Pokoj():
    def __init__(self, dane):
        kamienob = pg.image.load('kamien.png')
        self.tilelist = []

        rows = 0
        for row in dane:
            cols = 0
            for tile in row:
                if tile == 1:

                    kamien_rect = kamienob.get_rect()
                    kamien_rect.x = cols * tilesz
                    kamien_rect.y = rows * tilesz
                    tile = (kamienob,kamien_rect)
                    self.tilelist.append(tile)
                cols +=1
            rows +=1

    def draw(self):
        for tile in self.tilelist:
            screen.blit(tile[0], tile[1])

pokojdane = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
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
