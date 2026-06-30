import pygame as pg

#start pygame
pg.init()
clock = pg.time.Clock()
fps = 60
screen_size_x = 1000
screen_size_y = 600
screen = pg.display.set_mode((screen_size_x,screen_size_y))

#setup okna
pg.display.set_caption('isaac')
icon = pg.image.load('hiclipart.com.png')
pg.display.set_icon(icon)

tilesz = 50

class Player():

    def __init__(self, x, y,speed = 1.75):
        self.img = pg.image.load('slime.png')
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.speed = speed

    def update(self):
        dx = 0
        dy = 0
        key = pg.key.get_pressed()
        if key[pg.K_w]:
            dy -= self.speed
        if key[pg.K_s]:
            dy += self.speed
        if key[pg.K_d]:
            dx += self.speed
        if key[pg.K_a]:
            dx -= self.speed
        if key[pg.K_UP]:
            bullet = Bullet(self.rect.x, self.rect.y)
            bullet.shot('up')


    #collisions
        for tile in pokoj.tilelist:
            #for y
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                dy = 0
            #for x
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx= 0

        self.rect.x += dx
        self.rect.y += dy

        screen.blit(self.img, self.rect)
        pg.draw.rect(screen, (0, 0, 0), self.rect, 2)



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
            pg.draw.rect(screen, (0,0,0), tile[1], 2)

# bullet jako sprote.Sprite i caly czas w gameloop rysowana ta grupa i jak koniec range
# to zabijam sprite
class Bullet():
    def __init__(self, x, y, range = 150, speed = 3):
        self.img = pg.image.load('bullet.png')
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.range = range
        self.speed = speed
        self.shooting = False

    def shot(self, dir: str):
        self.shooting = True
        if dir == 'up':
            self.rect.y -= self.speed
        if dir == 'dwn':
            self.rect.y += self.speed
        if dir == 'rght':
            self.rect.x += self.speed
        if dir == 'lft':
            self.rect.x -= self.speed

        self.range -= self.speed
        if self.range == 0:
            self.shooting = False
        screen.blit(self.img, self.rect)


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

pokoj = Pokoj(pokojdane)
player = Player(300,300)
#game loop
gamerun = True
while gamerun == True:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gamerun = False
    screen.fill((100,0,100))
    pokoj.draw()
    player.update()
    pg.display.update()