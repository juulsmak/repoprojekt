import pygame as pg

#start pygame
pg.init()
screen_size_x = 1000
screen_size_y = 600
screen = pg.display.set_mode((screen_size_x,screen_size_y))

#setup okna
pg.display.set_caption('isaac')
icon = pg.image.load('hiclipart.com.png')
pg.display.set_icon(icon)

tilesz = 100



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
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

pokoj = Pokoj(pokojdane)

#game loop
gamerun = True
while gamerun == True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gamerun = False

    screen.fill((100,0,100))
    pokoj.draw()
    pg.display.update()